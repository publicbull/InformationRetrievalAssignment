# Scraping YELP!
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from YelpReviewCrawler.items import YelpreviewItem
from scrapy.http import Request

class YelpReviewSpider(BaseSpider):
	name = "yelp"
	allowed_domains = ["yelp.com"]
	start_urls = ["http://www.yelp.com/biz/pinks-hot-dogs-los-angeles-4"]

	# The function that will parse the data from the page request and:
	# 1. find the data to use as input for the YelpreviewItem(s) we want to store (defined in items.py)
	# 2. find the next page to crawl, if any
	def parse(self, response):
		# Using XPath to get certain objects from the HTML found in response.
		xpathSelector = HtmlXPathSelector(response)
		# Zoom in on the part of the page that contains a list of reviews.
		reviews = xpathSelector.select('//*[@id="reviews-other"]/ul/li')
		reviewItems = []
		docID = 1 # Fix this to be a global variable which changes for every 
		# Parsing every review found in the select call above.
		for li in reviews:
			reviewItem = YelpreviewItem()
			reviewItem['docID'] = docID
			docID += 1 # See comment above.
			reviewItem['stars'] = li.select('.//div[@class="rating"]/meta/@content').extract()[0]
			reviewItem['url'] = response.url
			reviewItem['date'] = li.select('.//div[@class="review-meta"]/meta[@itemprop="datePublished"]/@content').extract()[0]
			reviewItem['user'] = li.select('.//div[@class="user-passport"]//li[@class="user-name"]/a/text()').extract()[0]
			reviewItem['title'] = None
			 # Gets a list of unicode strings based on <br> elements in the html
			reviewContent = li.select('.//div[@class="media-story"]/p[1]/text()').extract()
			# We convert the list into a single string
			reviewContent = u' '.join(reviewContent) # the "u' '" part is a unicode string which we use to delimit the joined list.
			reviewItem['review'] = reviewContent
			reviewItem['review'] = li.select('.//div[@class="media-story"]/p[1]/text()').extract()[0]
			reviewItem['polarity'] = None
			reviewItem['confidence'] = None
			# putting it into a list of YelpreviewItems
			reviewItems.append(reviewItem)
		# finding the next page and adding it to the iterable reviewItems (This will cause it to be added as a)
		nextpage = xpathSelector.select('//*[@id="paginationControls"]/table/tr/td/span/following::a[1]/@href').extract()
		if len(nextpage) == 1:
			nextpage = 'http://www.yelp.com' + nextpage[0]
			reviewItems.append(Request(nextpage, callback=self.parse))
		return reviewItems