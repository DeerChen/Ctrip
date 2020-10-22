'''
Description: 管道文件，用于处理数据输出
Author: Senkita
Date: 2020-10-22 12:18:15
LastEditors: Senkita
LastEditTime: 2020-10-22 19:11:10
'''
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from pathlib import Path


class CtripcitiesPipeline:
    def __init__(self):
        self.items = {}
        self.filepath = Path.cwd().parent / Path('public') / 'cities.json'

    def process_item(self, item, spider):
        self.items.update(dict(item))
        return item

    def close_spider(self, spider):
        with open(self.filepath, 'w', encoding='utf-8') as fp:
            json.dump(self.items, fp, ensure_ascii=False)
