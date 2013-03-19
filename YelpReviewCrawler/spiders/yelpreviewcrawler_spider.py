# Scraping YELP!
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from YelpReviewCrawler.items import YelpreviewItem
from scrapy.http import Request

class YelpReviewSpider(BaseSpider):
	name = "yelp"
	allowed_domains = ["yelp.com"]
	start_urls = ["http://www.yelp.com/biz/pinks-hot-dogs-los-angeles-4"]

	def parse(self, response):
		xpathSelector = HtmlXPathSelector(response)
		reviews = xpathSelector.select('//*[@id="reviews-other"]/ul/li')
		reviewItems = []
		docID = 1 # Fix this shit!
		for li in reviews:
			reviewItem = YelpreviewItem()
			reviewItem['docID'] = docID
			docID += 1 # Fix this shit!
			reviewItem['stars'] = li.select('.//div[@class="rating"]/meta/@content').extract()[0]
			reviewItem['url'] = response.url
			reviewItem['date'] = li.select('.//div[@class="review-meta"]/meta[@itemprop="datePublished"]/@content').extract()[0]
			reviewItem['user'] = li.select('.//div[@class="user-passport"]//li[@class="user-name"]/a/text()').extract()[0]
			reviewItem['title'] = None
			reviewItem['review'] = li.select('.//div[@class="media-story"]/p[1]/text()').extract()[0]
			reviewItem['polarity'] = None
			reviewItem['confidence'] = None
			reviewItems.append(reviewItem)
		# finding the next page and adding it to the iterable reviewItems (This will cause it to be added as a)
		nextpage = xpathSelector.select('//*[@id="paginationControls"]/table/tr/td/span/following::a[1]/@href').extract()
		if len(nextpage) == 1
			nextpage = 'http://www.yelp.com' + nextpage[0]
			reviewItems.append(Request(nextpage, callback=self.parse))
		return reviewItems