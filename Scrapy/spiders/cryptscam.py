import scrapy
from ..items import ReportItem
from scrapy.loader import ItemLoader

import pandas as pd
import re

class CryptscamSpider(scrapy.Spider):
    name = 'cryptscam'
    allowed_domains = ['cryptscam.com']
    start_urls = ['https://cryptscam.com/en?page=1']

    reports_list = []
    c = 1
    def parse(self, response):

        reports =  response.css('div.container div.card')

        for report in reports:

            il = ItemLoader(item=ReportItem(), selector=report)
            report_list = []

            il.add_css('wallet_address', 'a')
            il.add_css('date', 'mark')
            il.add_css('type', 'h5.card-text')
            il.add_css('description', 'small')
            il.add_css('source', 'small')
            il.add_css('scammer', 'h5.card-text')
            il.add_css('country', 'h5.card-text')
            il.add_css('site_url', 'small')

            # yield il.load_item()

            # print(dict(il.load_item())["date"])
            item_dict = dict(il.load_item())
            report_list.append(item_dict["wallet_address"])
            report_list.append(item_dict["date"])
            report_list.append(item_dict["type"])
            report_list.append(item_dict["description"])
            report_list.append(item_dict["source"])
            report_list.append(item_dict["scammer"])
            report_list.append(item_dict["country"])
            report_list.append(item_dict["site_url"])

            self.reports_list.append(report_list)
            # print(len(self.reports_list), '\n\n')

            # yield {                                                             # yielding a dictionary
            #     'date': report.css('mark::text').get(),
            #     'type': report.css('h5.card-text::text').extract()[0],
            #     # 'scammer/abuser': report.css('h5.card-text::text').extract()[1],
            #     # 'country': report.css('h5.card-text::text').extract()[2],
            #     'description': report.css('small::text').extract()[0],
            #     'source': report.css('small::text').extract()[1],
            #     # 'site_url': report.css('h5.card-text::text').extract()[5]
            # }


        next_page = response.css('ul.pagination a::attr(href)').extract()[-1]
        if self.c < 1000:
            self.c += 1
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            df = pd.DataFrame(self.reports_list, columns=['wallet_address', 'date', 'type', 'description', 'source', 'scammer', 'country', 'site_url'])
            df.to_json('cryptscam.json', orient='records')
            # df.to_csv('cryptscam.csv', index=False, sep=',')
        # pass
