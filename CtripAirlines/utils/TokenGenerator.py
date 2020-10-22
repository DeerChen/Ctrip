'''
Description: 密钥生成器
Author: Senkita
Date: 2020-10-22 16:45:45
LastEditors: Senkita
LastEditTime: 2020-10-22 18:00:26
'''
from pathlib import Path
import execjs


class TokenGenerator:
    def __init__(self, dcity, acity):
        self.filepath = Path.cwd().parent / Path('public') / 'token.js'
        self.flightWay = 'Oneway'
        self.dcity = dcity
        self.acity = acity

    def get_token(self):
        with open(self.filepath, encoding='utf-8') as f:
            ctx = execjs.compile(f.read())

        return ctx.call('getProductToken', self.dcity, self.acity, self.flightWay)
