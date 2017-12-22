# -*- coding: utf-8 -*-
import json
import pymongo
from.settings import MONGODB_HOST,MONGODB_PORT,MONGODB_DBNAME,MONGODB_DOCNAME
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JingdongPipeline(object):
    def __init__(self):
        self.file = open('Jd.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '/n'
        self.file.write(line)
        return item
#mongodb
class writer2MongoPipline(object):
    def __init__(self):
        connect = pymongo.MongoClient(
            host=MONGODB_HOST,
            port=MONGODB_PORT,
        )
        db = connect[MONGODB_DBNAME]
        self.coll = db[MONGODB_DOCNAME]
    def process_item(self,item,spider):
        data = dict(item)
        self.coll.insert(data)
        return item
