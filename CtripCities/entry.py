'''
Description: 启动单个爬虫
Author: Senkita
Date: 2020-10-22 12:28:02
LastEditors: Senkita
LastEditTime: 2020-10-22 12:38:01
'''
from scrapy import cmdline

if __name__ == "__main__":
    cmdline.execute('scrapy crawl ctrip --nolog'.split())
