# -*- coding: utf-8 -*-
import scrapy
from Jiankang.items import JiankangItem

class JiankangSpider(scrapy.Spider):
    name = 'jiankang'
    # allowed_domains = ['www.pingan.com/official/insurance?firstclass=a6cd7dbd9051778b']
    start_urls = ['https://www.pingan.com/official/insurance?firstclass=a6cd7dbd9051778b']
        # https://www.pingan.com/official/insurance?firstclass=a6cd7dbd9051778b&pagenum=4

    # 起始页面,第一次请求
    # def parse(self,response):
    #     print(1)
    #     url = self.start_urls[0]
    #     yield scrapy.Request(url,callback=self.parse_page)
        
    # 获取每个浏览页
    def parse(self, response):
    # def start_requests(self):
        print(1)
        # 首先获取这个险种浏览界面有多少页:
        total_page = response.xpath('//div[@class="page-total"]/text()')[0].extract()
        # print(response.text)
        # print(total_page)

        # total_page = "共??页" 取出??
        total_page = int(total_page.replace("共","").replace("页",""))

        for i in range(1,5):
            url = self.start_urls[0]+"&pagenum=%s"%i
            print(url) 

            yield scrapy.Request(url,callback=self.parse_one)
            # 得到每个浏览页


    # 通过每个浏览页, 获取解析每个险种页面url.
    def parse_one(self,response):
        # print(3)
        # 先获取每页有多少个险种
        insurances = response.xpath('//div[@class="insurance-list-products"]//li')
        for insu in insurances:
            item = JiankangItem() # 创建每个险种信息对象

            item["name"] = insu.xpath('.//dt/text()')[0].extract()
            item["advantage"] = " ".join(insu.xpath('.//dl/dd/div/text()').extract())
            item['link'] = insu.xpath('./div[@class="prod-rt"]/a/@href')[0].extract()
            # print(item['link'])

            yield scrapy.Request(item['link'],callback=self.parse_two,meta={"item":item})
    
    def parse_two(self,response):
        item = response.meta['item']
        print(4)
        print(item)
        item['']


