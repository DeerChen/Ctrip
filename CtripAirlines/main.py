'''
Description: 主入口
Author: Senkita
Date: 2020-10-22 12:48:11
LastEditors: Senkita
LastEditTime: 2020-10-22 20:09:40
'''
from utils.Cities import Cities
from utils.Crawl import Crawl
import time
from random import randint


def main():
    cities = Cities()
    cities_dict = cities.file2dict()

    cities_list = list(cities_dict.keys())
    for dcity_name in cities_list:
        for acity_name in cities_list:
            if dcity_name != acity_name:
                crawl = Crawl(cities_dict, dcity_name, acity_name)
                crawl.get_response()
                print("{}-{}".format(dcity_name, acity_name), end='\r')
                rd = randint(5, 10)
                time.sleep(rd)


if __name__ == "__main__":
    main()
