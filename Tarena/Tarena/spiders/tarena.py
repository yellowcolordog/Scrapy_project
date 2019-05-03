# -*- coding: utf-8 -*-
import scrapy
from  Tarena.items import TarenaItem


class TarenaSpider(scrapy.Spider):
    name = 'tarena'
    allowed_domains = ['code.tarena.com.cn']
    start_urls = ['http://code.tarena.com.cn/AIDCode/aid1811/']

    def parse(self, response):
        # print(response.url)
        urls = response.xpath('//a[not(contains(@href,".."))]/@href').extract()
        for url in urls:
            if url[-1]=="/":
                # 说明是文件夹
                url = response.url+url
                yield scrapy.Request(url,callback=self.parse)
                
            else:
                # 说明是文件
                # print(2)
                item = TarenaItem()
                item['name'] = url
                item['link'] = response.url+url 
                item['path'] = response.url.replace('http://code.tarena.com.cn/AIDCode/aid1811/','')
                # print(item["path"]) 20_data/day02/
                yield item