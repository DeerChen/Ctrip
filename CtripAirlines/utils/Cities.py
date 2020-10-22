'''
Description: 读取城市简称并转为字典
Author: Senkita
Date: 2020-10-22 18:15:39
LastEditors: Senkita
LastEditTime: 2020-10-22 19:15:52
'''
from pathlib import Path
import json


class Cities:
    def __init__(self):
        self.filepath = Path.cwd().parent / Path('public') / 'cities.json'

    def file2dict(self):
        with open(self.filepath, encoding='utf-8') as f:
            return json.loads(f.read())
