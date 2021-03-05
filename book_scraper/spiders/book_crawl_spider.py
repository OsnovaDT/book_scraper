from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from book_scraper.product_loader import BookLoader
from book_scraper.items import Book


class BookCrawlSpider(CrawlSpider):
    name = 'book_crawl_spider'
    allowed_domains = ['www.labirint.ru']

    # start_urls = ['https://www.labirint.ru/authors/14550/']
    start_urls = ['https://www.labirint.ru/authors/152075/']

    rules = (
        Rule(
            LinkExtractor(allow=('/books/\d+',)),
            callback='parse_book'
        ),
    )

    def parse_book(self, response):
        book_loader = BookLoader(
            item=Book(),
            response=response
        )

        # Book url
        book_loader.add_value(
            'book_url',
            response.url
        )

        return book_loader.load_item()
