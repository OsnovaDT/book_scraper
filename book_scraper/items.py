"""Items for parsing"""

from scrapy import Item, Field


class Book(Item):
    """Book item"""

    book_url = Field()
    image_url = Field()
    title = Field()
    price = Field()
    authors = Field()
    series_of_books = Field()
    publishing_house = Field()
