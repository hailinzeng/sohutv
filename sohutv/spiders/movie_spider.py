# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from .. import items

class MovieSpider(scrapy.Spider):
    name = "movie"

    start_urls = [
                'http://so.tv.sohu.com/list_p1100_p2_p3_p4_p5_p6_p7_p8_p9_p101_p11_p12_p13.html'
                ]

    def parse(self, response):
        self.log ('>> parse')

        # yield item
        movie_names = response.selector.xpath("//ul[contains(@class, 'st-list')]//li//strong//a//text()").extract()
        movie_urls = response.selector.xpath("//ul[contains(@class, 'st-list')]//li//strong/a/@href").extract()
        movie_imgs = response.selector.xpath("//ul[contains(@class, 'st-list')]//li//img/@src").extract()
        movie_num = len(movie_names)
        for i in range(0, movie_num):
            yield items.SohutvItem(name=movie_names[i], page_url=movie_urls[i], img_url=movie_imgs[i])

        # yield next page
        nav_list = response.selector.xpath("//div[contains(@class, 'ssPages')]//a")
        nav_last_txt = nav_list.xpath("@title").extract()[-1]
        if nav_last_txt == u'\u4e0b\u4e00\u9875':
            yield response.follow(nav_list.xpath('@href').extract()[-1], callback=self.parse)
