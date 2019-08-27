import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from Erowid.items import ErowidItem
# -*- coding: utf-8 -*-


class ExperiencesSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["www.erowid.org"]
    start_urls = ['https://www.erowid.org/experiences/subs/exp_aPVP.shtml']
    rules = [
    Rule(LinkExtractor(allow=r'/experiences/exp\.php\?ID=\d+$'),
         callback='parse_item', follow=True)
]
    def parse_item(self, response):

        selectors = response.css('div')
        for selector in selectors:
            experience = ErowidItem()
            experience['Author'] = selector.xpath('//div[@class="author"]/a/text()').extract
            experience['Title'] = selector.xpath('//div[@class="title"]/text()').extract
            experience['Substance'] = selector.xpath('//div[@class="substance"]/text()').extract
            experience['Text'] = selector.xpath("//div[@class = 'report-text-surround']/text()").extract

        yield experience
