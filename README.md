# sohutv

learn scrapy

- create scrapy project : `scrapy startproject sohutv .`
- `scrapy shell 'http://so.tv.sohu.com/list_p1100_p2_p3_p4_p5_p6_p7_p8_p9_p101_p11_p12_p13.html'`
- fix forbidden by robots.txt: settings.py, `set ROBOTSTXT_OBEY=False`
- chrome console: `$x("//ul[contains(@class, 'st-list')]//li")`
- quick xpath by chrome 'Inspect Element'
- tutorial: [Web Scraping and Crawling With Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-and-crawling-with-scrapy-and-mongodb/)

usage:

- install mongodb; create database `sohutv` and add collection `movies`
- install virtualenv: `pip install virtualenv`
- create virtualenv: `virtualenv env; source env/bin/activate`
- install dependency: `pip install -r requirements.txt`
- run scrapy: `scrapy crawl movie`