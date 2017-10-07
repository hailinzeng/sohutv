# -*- coding: utf-8 -*-
import pymongo

from scrapy.conf import settings
from scrapy import log

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class SohutvPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
                settings['MONGODB_SERVER'],
                settings['MONGODB_PORT']
                )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        # write to MongoDB
        self.collection.update({'page_url': item['page_url']}, dict(item), upsert=True)
        # self.collection.insert(dict(item))
        return item
