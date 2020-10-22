'''
Description: 爬虫请求文件
Author: Senkita
Date: 2020-10-22 12:20:57
LastEditors: Senkita
LastEditTime: 2020-10-22 12:27:48
'''
import scrapy
from scrapy.http import Request
import json


class CtripSpider(scrapy.Spider):
    # * 爬虫名称
    name = 'ctrip'
    # * 允许爬取的域名列表
    allowed_domains = ['ctrip.com']
    # * 开始爬取的资源链接列表
    start_urls = ['http://ctrip.com/']

    def start_requests(self):
        yield Request(
            url='https://flights.ctrip.com/itinerary/api/poi/get',
            callback=self.parse_cities,
        )

    def traverse(self, alphabet_list):
        new_shortcuts_list = []
        for alphabet in alphabet_list:
            for a in alphabet_list[alphabet]:
                new_shortcuts_list.append({a['display']: a['data'].split('|')[-1]})
        return new_shortcuts_list

    def parse_cities(self, response):
        json_data = json.loads(response.body.decode(response.encoding))
        shortcuts_list = []

        for alphabet_list_name in json_data['data']:
            if (
                all(map(lambda x: '\u4e00' <= x <= '\u9fa5', alphabet_list_name))
                is False
            ):
                alphabet_list = json_data['data'][alphabet_list_name]

                shortcuts_list.extend(self.traverse(alphabet_list))

        for i in shortcuts_list:
            ((key, val),) = i.items()
            yield {key: val}
