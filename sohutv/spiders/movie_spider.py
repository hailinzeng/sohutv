import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse

class MovieSpider(scrapy.Spider):
    name = "movie"

    start_urls = [
                'http://so.tv.sohu.com/list_p1100_p2_p3_p4_p5_p6_p7_p8_p9_p101_p11_p12_p13.html'
                ]

    def parse(self, response):
        self.log ('>> parse')
        movie_list = response.selector.xpath("//ul[contains(@class, 'st-list')]//li//strong//a//text()").extract()
        print (movie_list)
        return []
