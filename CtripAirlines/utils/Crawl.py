'''
Description: 爬虫
Author: Senkita
Date: 2020-10-22 16:59:29
LastEditors: Senkita
LastEditTime: 2020-10-22 20:07:48
'''
from utils.TokenGenerator import TokenGenerator
import datetime
import requests
import json
from fake_useragent import UserAgent
from pathlib import Path

ua = UserAgent(verify_ssl=False).random
headers = {
    'DNT': '1',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'User-Agent': ua
}


class Crawl:
    def __init__(self, cities_dict, dcityname, acityname):
        self.url = 'https://flights.ctrip.com/itinerary/api/12808/products'
        self.cities_dict = cities_dict
        self.dcityname = dcityname
        self.acityname = acityname
        self.dcity = self.cities_dict[self.dcityname]
        self.acity = self.cities_dict[self.acityname]

    def get_token(self):
        tg = TokenGenerator(self.dcity, self.acity)
        return tg.get_token()

    def assemble_json(self):
        date = str(datetime.date.today() + datetime.timedelta(days=1))
        token = self.get_token()

        return json.dumps({
            "flightWay": "Oneway",
            "classType": "ALL",
            "hasChild": False,
            "hasBaby": False,
            "searchIndex": 1,
            "airportParams": [{
                "dcity": self.dcity,
                "acity": self.acity,
                "dcityname": self.dcityname,
                "acityname": self.acityname,
                "date": date
            }],
            "selectedInfos": None,
            "army": False,
            "token": token
        })

    def get_response(self):
        data = self.assemble_json()
        response = requests.post(self.url, data=data, headers=headers)
        filepath = Path.cwd() / Path('results') / '{}.json'.format(self.dcity + self.acity)
        with open(filepath, 'w', encoding='utf-8') as fp:
            fp.write(response.text)
