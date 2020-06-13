# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from urllib import request
import os


class TutorialPipeline(object):

    def process_item(self, item, spider):
        print("name:[%s] - url:[%s]" % (item.get("name"), item.get("url")))

        path = os.path.abspath('..') + "/gif/" + item['name']
        print("!!!path:" + path)
        response = request.urlopen(item['url'])
        chunk = 16 * 1024
        with open(path, "wb") as f:
            while True:
                chunk = response.read(chunk)
                if not chunk:
                    break
                f.write(chunk)
        return item