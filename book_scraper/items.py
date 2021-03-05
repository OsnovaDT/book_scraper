import scrapy


class Book(scrapy.Item):
    book_url = scrapy.Field()
    image_url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    authors = scrapy.Field()
    series_of_books = scrapy.Field()
    publishing_house = scrapy.Field()
