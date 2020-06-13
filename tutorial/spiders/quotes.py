import scrapy
from urllib.parse import quote
import sys
from tutorial.items import TutorialItem
import os


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    allowed_domains = []

    # def __init__(self, category=None, *args, **kwargs):
    #     super(QuotesSpider, self).__init__(*args, **kwargs)
    #     print("+++++++++++++++++++++")
    #     print(category)

    def start_requests(self):
        urls = [
            'https://zhaoolee.com/ChineseBQB/002CuteGirl_%E5%8F%AF%E7%88%B1%E7%9A%84%E5%A5%B3%E5%AD%A9%E7%BA%B8%F0%9F%91%A7BQB/#more'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        h = response.xpath('/html/body/div/main/div/div/div/div/article/div/div[1]//h6//a[@rel=\'noopener\']/text()').extract()
        for i in h:
            item = TutorialItem()
            url = quote(i, encoding='utf-8').replace('https%3A', 'https:')
            index = i.rindex('/')
            item['name'] = i[index + 1:]
            item['url'] = url
            yield item


if __name__ == "__main__":
    # ssl._create_default_https_context = ssl._create_unverified_context
    # context = ssl._create_unverified_context()
    # url = 'https://raw.githubusercontent.com/zhaoolee/ChineseBQB/master/020TATAN%F0%9F%A4%B7%E2%80%8D%E2%99%82%EF%B8%8FBQB/0.gif'
    # response = request.urlopen(url)
    # print(response.)
    print(sys.argv[0])

    print(os.getcwd())  # 获取当前工作目录路径
    print(os.path.abspath('.'))  # 获取当前工作目录路径
    print(os.path.abspath('test.txt'))  # 获取当前目录文件下的工作目录路径
    print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
    print(os.path.abspath(os.curdir)) # 获取当前工作目录路径
