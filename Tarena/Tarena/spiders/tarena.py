# -*- coding: utf-8 -*-
import scrapy
from  Tarena.items import TarenaItem


class TarenaSpider(scrapy.Spider):
    name = 'tarena'
    allowed_domains = ['code.tarena.com.cn']
    start_urls = ['http://code.tarena.com.cn/AIDCode/aid1811/']

    def parse(self, response):
        print(response.url)
        urls = response.xpath('//a[not(contains(@href,".."))]/@href').extract()
        for url in urls:
            if url[-1]=="/":
                # 说明是文件夹
                url = response.url+url
                

            else:
                # 说明是文件
                item = TarenaItem()
                item['name'] = url
                item['link'] = self.start_requests[0]+url 
                item['path'] = response.url.replace('http://code.tarena.com.cn/AIDCode/aid1811/','')
                yield item