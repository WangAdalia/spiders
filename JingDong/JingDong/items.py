# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #商品id
    product_id=scrapy.Field()
    #价格url
    price_url=scrapy.Field()
    #店铺
    shop_name = scrapy.Field()
    #商品名
    product_name = scrapy.Field()
    #商品网址
    product_url = scrapy.Field()
    #商品价格
    product_price = scrapy.Field()

    #商品评论的数量
    comment_num = scrapy.Field()
    #好评
    good_commt_num = scrapy.Field()
    #中评
    gen_commt_num = scrapy.Field()
    #差评
    bad_commt_num = scrapy.Field()
    #追加评论
    add_commt_num = scrapy.Field()

    #商品用户具体信息
    product_commentinfo = scrapy.Field()
    #客户名
    user_name = scrapy.Field()
    #京享值
    jd_level = scrapy.Field()
    #很喜欢
    content = scrapy.Field()
    #评论星级
    comment_star = scrapy.Field()
    #购买的型号
    product_data = scrapy.Field()
    #评论日期
    push_data = scrapy.Field()
    #点赞数
    comment_good = scrapy.Field()

