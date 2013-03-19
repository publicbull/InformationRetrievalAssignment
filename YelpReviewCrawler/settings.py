# Scrapy settings for YelpReviewCrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'YelpReviewCrawler'

SPIDER_MODULES = ['YelpReviewCrawler.spiders']
NEWSPIDER_MODULE = 'YelpReviewCrawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'YelpReviewCrawler (+http://www.yourdomain.com)'
