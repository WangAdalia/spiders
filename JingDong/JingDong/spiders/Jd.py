# -*- coding: utf-8 -*-
import scrapy
from ..items import JingdongItem
import json

class JdSpider(scrapy.Spider):
    name = 'Jd'
    allowed_domains = ['jd.com','p.3.cn','sclub.jd.com']
    start_urls = ['https://list.jd.com/list.html?cat=9987,653,655']

    def parse(self, response):
        base_price_url = 'https://p.3.cn/prices/mqets?skuIds=J_%s'
        for i in response.xpath('//li[@class="gl-item"]'):
            item = JingdongItem()
            #匹配店铺
            item['shop_name'] = i.xpath('./div/div[@class="p-shop"]/@data-shop_name').extract_first()
            #商品名
            item['product_name'] = i.xpath('./div/div[@class="p-name"]/a/em/text()').extract_first().strip()
            #商品url
            item['product_url'] = 'https:'+i.xpath('./div/div[@class="p-img"]/a/@href').extract_first()
            # print(item['product_url'])
            #商品价格的id
            item['product_id'] = i.xpath('./div/@data-sku').extract_first()
            # 每个商品价格url
            price_url= base_price_url%(item['product_id'])
            yield scrapy.Request(url=price_url, meta={'item':item}, callback=self.parse_price)
    #商品价格
    def parse_price(self,response):
        items = response.meta['items']
        product_dict =response.text
        items['product_price']=json.loads(product_dict)[0]['p']
        # print(items['product_price'])
        yield scrapy.Request(url=items['product_url'], meta={"items": items}, callback=self.parse_detail,
                             dont_filter=True)
    #评论接口
    def parse_detail(self,response):
        items = response.meta['items']
        product_id = items['product_id']
        url = 'http://sclub.jd.com/comment/productPageComments.action?productId=%s&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'%(product_id)
        yield scrapy.Request(
            url=url,
            callback=self.get_all_comment,
            meta={'items': items},
            dont_filter=True
        )
    # 商品评论
    def get_all_comment(self,response):
        items = response.meta['items']
        commentinfo_list = []
        commentinfo_dict = {}
        data = json.loads(response.text)
        #商品的总评价
        pcs = data.get('productCommentSummary')
        if pcs:
            items['comment_num'] = pcs.get('commentCount') #评论数
            items['good_commt_num'] = pcs.get('goodCount')#好评
            items['gen_commt_num'] = pcs.get('generalCount')#中评
            items['bad_commt_num'] = pcs.get('poorCount')#差评
            items['add_commt_num'] = pcs.get('afterCount')#追加
        else:
            items['comment_num'] = None #评论数
            items['good_commt_num'] = None #好评
            items['gen_commt_num'] = None #中评
            items['bad_commt_num'] = None #差评
            items['add_commt_num'] = None #追加
            #用户信息
        comments = data.get('comments')#返回list
        for comment in comments:
            commentinfo_dict['user_name'] = comment['nickname']#用户名
            commentinfo_dict['jd_level'] = comment['userLevelName'] #京享值
            commentinfo_dict['content'] = comment['content']#喜欢
            commentinfo_dict['comment_star'] = comment['score']#评论星级
            commentinfo_dict['product_data'] = comment['creationTime'] #评论日期
            commentinfo_dict['comment_good'] = comment['usefulVoteCount']#点赞数
            commentinfo_list.append('commentinfo_dict')
        items['comment_info'] = commentinfo_list
        yield items









