import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from lcscraper.spiders.solution import SolutionSpider


def main():
    process = CrawlerProcess(get_project_settings())
    process.crawl(SolutionSpider)
    process.start()

if __name__== "__main__":
    main()
