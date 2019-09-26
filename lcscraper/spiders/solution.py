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
            for question in questions[:100]:
                if not question['solution'] or not question['solution']['canSeeDetail']:
                    continue
                question_dir = os.path.join(
                    'output', question['id'] + '.' + question['title']).replace(' ', '')

                yield scrapy.Request(
                    url='https://leetcode.com/articles/' + question['slug'] + '/',
                    headers={
                        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7'
                    },
                    callback=self.parse,
                    meta={
                        'question': question,
                        'question_dir': question_dir
                    })
 

    def parse(self, response):
        question = response.meta['question']
        question_dir = response.meta['question_dir']

        content = response.css('.article-body').get()
        if not content:
            return
        with open(os.path.join(question_dir, 'solution.md'), 'w') as f:
            f.write(content)
        

