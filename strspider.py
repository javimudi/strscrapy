# -*- coding: utf-8 -*-
import scrapy


class StrspiderSpider(scrapy.Spider):
    name = 'strspider'
    allowed_domains = ['www.stuttgart-airport.com']
    start_urls = ['http://www.stuttgart-airport.com/arrival-departure/arrivals/']

    def parse(self, response):
        for row in response.css('div.flight-list'):
            yield row
