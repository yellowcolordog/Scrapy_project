# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import datetime

class KyzgPipeline(object):
    def process_item(self, item, spider):
        l=[]
        # print(3)
        for i in item:
            l.append(item[i])
        # print(l)
        # filepath='开源众包项目初步筛选%s.csv'%datetime.datetime.now().strftime('%m%d')
        csvname="开源众包项目初步筛选4月16日.csv"
        with open(csvname,'a') as f:
            writer = csv.writer(f)
            writer.writerow(l)

        return item
