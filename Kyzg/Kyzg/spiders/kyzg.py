# -*- coding: utf-8 -*-
import scrapy
import json
from Kyzg.items import KyzgItem


class KyzgSpider(scrapy.Spider):
    name = 'kyzg'
    allowed_domains = ['zb.oschina.net/projects/list.html']
    # start_urls = ['https://zb.oschina.net/projects/list.html']

    def start_requests(self):
        # https://zb.oschina.net/project/contractor-browse-project-and-reward?pageSize=10&currentPage=3
        # 爬取开源众包所有数据, 找技能要求是python的工作
        print(1)
        for i in range(1,100):
            url = "https://zb.oschina.net/project/contractor-browse-project-and-reward?pageSize=10&currentPage=%s"%i 
            yield scrapy.Request(url,callback=self.parse_page,meta={'i':i})
        
    def parse_page(self,response):
        # 返回的是一堆json代码,需要从json代码中获取要的数据
        # 需要爬取
        # 项目名称, 报酬, 开发限时, 已竞标人数,
        # 发布时间, 页面加载地址/project/detail.html?id=13540374 id经过简单加密https://zb.oschina.net/project/detail.html?id=18549357
        # name = scrapy.Field()
        # price = scrapy.Field()
        # lim_time = scrapy.Field()
        # renshu = scrapy.Field()
        # pub_time = scrapy.Field()
        # link = scrapy.Field()
        datas = json.loads(response.text)['data']['data']
        print(response.meta[i])
        for data in datas: # 获取到了每个项目数据
            # 如果技能包含python才爬取这个项目:
            if "skillList" in data:
                for skill in data['skillList']:
                    if skill['value'] =="Python":
            
                        # print(data['id'])
                        item = KyzgItem()
                        item['name'] = data['name']
                        item['price'] = data['budgetMinByYuan']+'-'+data['budgetMaxByYuan']
                        item['lim_time'] = str(data['cycle']) +data['cycleName']
                        item['renshu'] = data['applyCount']
                        item['pub_time'] = data['publishTime']
                        item['link'] = 'https://zb.oschina.net/project/detail.html?id=%s'%'???'  # ???这里加密需要处理一下和data['id']有关
                    
                        yield item




