# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
from scrapy import Spider, Request, FormRequest
from havenwall.items import UrlItem


class WallFavSpider(Spider):
    name = 'wall_fav'
    allowed_domains = ['alpha.wallhaven.cc']
    start_url = 'https://alpha.wallhaven.cc/search?q=&categories=110&purity=100&atleast=1920x1080&topRange=1M&sorting=favorites&order=desc&page={offset}'
    list_img = []

    def start_requests(self):
        for page in range(1,2):
            yield Request(self.start_url.format(offset=page),callback=self.get_parse)
        #yield Request(url='https://alpha.wallhaven.cc/search?' + urlencode(data),callback=self.get_parse)

    def get_parse(self, response):
        soup = BeautifulSoup(response.text,'lxml')
        results = soup.find_all('a',class_='preview')
        for result in results:
            yield Request( url = result.get('href'),callback = self.parse_pic)

    def parse_pic(self,response):
        item = UrlItem()
        soup = BeautifulSoup(response.text,'lxml')
        real_urls = soup.find_all('div',class_='scrollbox')
        for real_url in real_urls:
            url = 'https://' + re.compile(r'src="//(.*?)"').search(str(real_url)).group(1)
            num = re.search('\d+',url).group()
            item['image_urls'] = url
        yield item
