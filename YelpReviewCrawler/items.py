# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class YelpreviewItem(Item):
    # Defining the data we will collect
    docID = Field()
    stars = Field()
    url = Field()
    date = Field()
    user = Field()
    title = Field()
    review = Field()
    polarity = Field()
    confidence = Field()