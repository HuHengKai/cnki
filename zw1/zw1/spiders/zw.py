# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from zw1.items import Zw1Item
class ZwSpider(scrapy.Spider):
    name = 'zw'
    allowed_domains = ['cnki.net']
    start_urls = ['http://wap.cnki.net/touch/web/Article/SearchIndex']

    def __init__(self):
        self.bro = webdriver.Chrome()

    # def closed(self, spider):
    #     print("爬虫结束")
    #     self.bro.quit()

    def parse(self, response):
        print("*"*50)
        print(response.url)
        divs = response.xpath('//a[@class="c-company-top-link"]')
        for div in divs:
            href = div.xpath('./@href').get()
            # href = 'http://wap.cnki.net/touch/web/Journal/Article/JSYW201810037.html'
            href="http:"+href
            pass
            str1 = ""
            title = div.xpath('./div[1]//text()').getall()
            for i in title:
                str1 = str1 + i
            name=str1.strip()
            print(f"name is {name},href is {href}")
            pass
            yield scrapy.Request(url=href, callback=self.parse_detail)

    def parse_detail(self, response):
        item=Zw1Item()
        item["text"]=response.xpath('//div[@class="c-card__aritcle"]/text()').get().strip()
        item["titleName"]=response.xpath('//div[@class="c-card__title2"]/text()').get().strip()
        card=response.xpath('//div[@class="c-card__author"]/a/text()').getall()
        item["authorScholl"]=card[0]
        item["authorName"]=card[-1]
        item["jigou"]=response.xpath('//div[@class="c-card__paper-content"]/a/text()').get().strip()
        item["word"] = response.xpath('//div[@class="c-card__paper-content c-card__paper-content-normal"]/a/text()').getall()
        yield item

