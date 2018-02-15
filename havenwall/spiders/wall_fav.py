# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from scrapy import Spider, Request, FormRequest
from havenwall.items import UrlItem


class transCookie(object):
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')  # 记得去除空格
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict


class WallFavSpider(Spider):
    name = 'wall_fav'
    allowed_domains = ['alpha.wallhaven.cc']
    start_url = 'https://alpha.wallhaven.cc/search?q=&categories=111&purity=100&atleast=1920x1080&sorting=views&order=desc&page={offset}'
    list_img = []

    def start_requests(self):
        coo = "__cfduid=d1b3e0ec4ee01bedc08f609cd93a709d51511108514; _ga=GA1.2.1156805805.1511228989; remember_82e5d2c56bdd0811318f0cf078b78bfc=eyJpdiI6IlRobjFBSDRmaUp3ZlEreDJsVEYxWUpVRERUN0FGK3FpczU1KzVDK3J6ZXM9IiwidmFsdWUiOiJIb0dlXC9NVW1jYW42THhMK0ZqT1wvaDZEYUdxYWpmTzdcL0h2ODdGXC8xRHY2VjlRYU5cL01lckxVZjFJUnRWRU05MnJHZ2x4SnNYaExCTklCanBYeFB3bTduTlZBTnpIMGVhRE52bzM3UzRUMGtQY1l6QkhvUGJlaEk4MHo3VlwvaG5paCIsIm1hYyI6Ijk5MjFmOWI0YzFlODZmZmQ0MjI0OWVjM2VkMDAwMDg0MzlhNjczYzhjYWU0ODY0MjIwYTU5ZjJhMjY0OGI0ZmYifQ%3D%3D; wallhaven_session=eyJpdiI6Imlzb2ZSazBkYVwvNkZKXC9ObDY1S3BFc3NzNThFNW9IV09mN05CdUJQdGRKND0iLCJ2YWx1ZSI6IklMUExLNWVGK1BvM2tWN09ERjF4T0pUQmROenQrMkxxRlVzb1pVcW9xZWVReDZqcndPcWJHZ2RlT3Z0U0YwSG5VY3NEK3J0eGV3XC82RFFzYkM0S2M5QT09IiwibWFjIjoiNzM2NjYyYjhkNDFhZmU2MjRiYWYyMjJiN2FmYmU5NzcwNTYxODA4YTI2NmEzZDQ4NDU3ODYxYzkxMTUxZTZmNyJ9"
        trans = transCookie(coo)
        cookie = trans.stringToDict()
        for page in range(1, 20):
            yield Request(self.start_url.format(offset=page),cookies=cookie, callback=self.get_parse)
        # yield Request(url='https://alpha.wallhaven.cc/search?' + urlencode(data),callback=self.get_parse)

    def get_parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        results = soup.find_all('a', class_='preview')
        for result in results:
            yield Request(url=result.get('href'), callback=self.parse_pic)

    def parse_pic(self, response):
        item = UrlItem()
        soup = BeautifulSoup(response.text, 'lxml')
        real_urls = soup.find_all('div', class_='scrollbox')
        for real_url in real_urls:
            url = 'https://' + re.compile(r'src="//(.*?)"').search(str(real_url)).group(1)
            num = re.search('\d+', url).group()
            item['image_urls'] = url
        yield item
