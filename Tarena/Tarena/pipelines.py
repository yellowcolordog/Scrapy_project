# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from Tarena.settings import BASEFILES
from scrapy.pipelines.files import FilesPipeline
import scrapy

class TarenaPipeline(object):
    def process_item(self, item, spider):
        # filepath = BASEFILES + item['path']
        # folder = "/".join(filepath.split('/')[:-1])
        # # 存文件位置是filepath+link, 但是可能缺文件夹,
        # # 首先需要创建文件夹folder 
        # if not os.path.exists(folder):
        #     os.makedirs(folder)
        # # 文件夹创建完毕,接下来存文件:
        # with open(filepath,"r") as f :
        #     f.write
        return item

class TarenaFilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return scrapy.Request(item['link'],meta=item)

    def file_path(self, request, response=None, info=None):  # 重写file_path 设置图片名字
        print(request.meta['path'] + request.meta['name'])
        return request.meta['path'] + request.meta['name']
