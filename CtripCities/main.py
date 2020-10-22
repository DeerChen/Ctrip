'''
Description: 启动所有爬虫
Author: Senkita
Date: 2020-10-22 12:28:02
LastEditors: Senkita
LastEditTime: 2020-10-22 12:29:03
'''
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.spiderloader import SpiderLoader

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    spider_loader = SpiderLoader(get_project_settings())
    for spider_name in spider_loader.list():
        process.crawl(spider_name)

    process.start()
