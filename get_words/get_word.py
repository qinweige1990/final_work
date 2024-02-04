import json

import requests


def get_hot_words():
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Origin': 'https://www.amzfish.cn',
        'Referer': 'https://www.amzfish.cn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'token': '2a7d80c371fe79ef25e4082fd360aabb-6ba3a6221bd085854d92372ecfcf9362',
    }

    params = {
        'page': '1',
        'limit': '50',
        'country': 'US',
        'day': '2024/01/13',
        'keyword': '',
        'length': '',
        'rankRange': '',
        'clickRange': '',
        'conversionRange': '',
        'rankRiseWeek': '',
        'rankRise': '',
        'rankRiseRateWeek': '1',
        'rankRiseRate': '50-0',
        'fields': '',
        'field': '',
        'sort': '',
        'isTopAsin': '1',
        'isWord': '0',
        'brand': '',
    }
    print("开始拉取飞鱼数据")
    print("----------------------------------")
    response = requests.get('https://api.amzfish.cn/api/v1.0/aba/keyword/potential.rise.list', params=params,
                            headers=headers)
    res = json.loads(response.content)
    print(res)
    words = []
    for item in res["data"]["list"]:
        words.append(item["keyword"])

    print("拉取到的关键词：", words)
    return words
# print(json.dumps(res, indent=2))
