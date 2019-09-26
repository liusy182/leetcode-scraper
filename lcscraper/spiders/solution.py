# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import scrapy
from scrapy.exceptions import DropItem
from bs4 import BeautifulSoup
import os
import json

class SolutionSpider(scrapy.Spider):
    name = 'solution'
    allowed_domains = []

    def start_requests(self):
        with open(os.path.join('output', 'all.json'), 'r') as f:
            questions = json.load(f)
            for question in questions:
                if question['solution'] and question['solution']['canSeeDetail']:
                    yield scrapy.Request(
                        url='https://leetcode.com/articles/' + question['slug'],
                        callback=self.parse)
 


    def parse(self, response):
        print(response.css('.article-body').get())
        

