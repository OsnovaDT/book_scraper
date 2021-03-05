"""Book loader"""

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class BookLoader(ItemLoader):
    """Book loader class that take only first suitable element"""

    # Our loader will take take only first suitable element
    default_output_processor = TakeFirst()
