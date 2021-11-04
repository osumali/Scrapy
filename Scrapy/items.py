# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def TakeSecond(_list_):
    return _list_[1]

def TakeThird(_list_):
    return _list_[2]

def TakeFourth(_list_):
    return _list_[3]

def TakeFifth(_list_):
    return _list_[4]

# def remove_newline(text):
#     return float(text.replace("\n", ""))

class ReportItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    wallet_address = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())
    date = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())
    type = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeSecond)
    description = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFirst())
    source = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeSecond)
    scammer = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeThird)
    country = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeFourth)
    site_url = scrapy.Field(input_processor=MapCompose(remove_tags),
                        output_processor=TakeThird)

    pass
