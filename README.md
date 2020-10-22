# Ctrip

## Description

爬取携程网国内航线信息。

## Features

1. 使用 Scrapy 爬取城市简称(对！就是这么的大材小用！)
2. 分析携程网的Token生成，并直接使用Python运行JS代码生成Token(混淆代码看得头疼)
3. 好吧，爬取失败，前面爬太快，就被盯上了

## Installation

```bash
pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl
pip install Scrapy
pip install PyExecJS
pip install requests
```

## Usage

```bash
# 爬取城市简称
cd CtripCities && python3 main.py

# 爬取航线信息
cd CtripAirlines && python3 main.py
```

## Maintainers

[Senkita](https://github.com/Senkita)

## License

[MIT](https://github.com/Senkita/Ctrip/blob/main/LICENSE) © [Senkita](https://github.com/Senkita)
