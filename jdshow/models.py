from django.db import models
from mongoengine import *
# connect('jd',host='127.0.0.1',port=27017)
# Create your models here
class jdproduct(Document):
    #继承的是Document 不是models.model
    #参数如果required = Ture,必须要实例化，也就是不能为空，
    product_id = StringField(required=True,max_length=200)#商品的id
    price_url = StringField(required=True,max_length=200)#价格链接
    shop_name = StringField(required=True,max_length=200)#店铺名
    product_name = StringField(required=True,max_length=200)#商品名
    product_url = StringField(required=True,max_length=200)#商品链接
    product_price = StringField(required=True)#商品价格
    comment_num = StringField(required=True)
    good_comment_num = StringField(required=True)
    bad_comment_num  = StringField(required=True)
    comment_info = StringField(required=True)
    add_comment_num = StringField(required=True)
    gen_comment_num = StringField(required=True)

    meta ={
            'collection':'jdproduct'#指定要链接的集合
            #'ordering':['comment_count'],#默认评论进行评论
        }