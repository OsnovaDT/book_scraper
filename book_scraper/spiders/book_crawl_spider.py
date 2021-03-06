"""Book crawl spider"""

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from book_scraper.book_loader import BookLoader
from book_scraper.items import Book


class BookCrawlSpider(CrawlSpider):
    """Book crawl spider class"""

    name = 'book_crawl_spider'
    allowed_domains = ['www.labirint.ru']

    # start_urls = ['https://www.labirint.ru/authors/14550/']
    start_urls = ['https://www.labirint.ru/authors/152075/']

    rules = (
        Rule(
            # Get book with some number
            LinkExtractor(allow=(r'/books/\d+',)),
            callback='parse_book'
        ),
    )

    def parse_book(self, response):
        """Method for parsing book"""

        book_loader = BookLoader(
            item=Book(),
            response=response
        )

        # Book url
        book_loader.add_value(
            'book_url',
            response.url
        )

        # Book title
        book_loader.add_xpath(
            'title',
            "//div[@class='prodtitle']/h1/text()"
        )

        # Book price
        book_loader.add_xpath(
            'price',
            "//div[@class='buying-priceold-val']/span/text()"
        )

        # Book publishing house
        book_loader.add_xpath(
            'publishing_house',
            "//div[@class='publisher']/a/text()"
        )

        # Book series
        book_loader.add_xpath(
            'series_of_books',
            "//div[@class='series']/a/text()"
        )

        return book_loader.load_item()
