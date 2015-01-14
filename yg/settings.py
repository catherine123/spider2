# -*- coding: utf-8 -*-

# Scrapy settings for yg project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'yg'

SPIDER_MODULES = ['yg.spiders']
NEWSPIDER_MODULE = 'yg.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'yg (+http://www.yourdomain.com)'
SPIDER_MIDDLEWARES = {}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)'
Referer = 'http://www.lhmart.com/'
RETRY_TIMES = 30

RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 404, 408]
DOWNLOAD_DELAY = 0.4 # 5,000 ms of delay
CONCURRENT_REQUESTS =  50
LOG_LEVEL = 'INFO'
# DOWNLOAD_DELAY = 0.1
DUPEFILTER_CLASS = 'scrapy.dupefilter.RFPDupeFilter'

DOWNLOADER_MIDDLEWARES = {
                    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
                  #  'myspider.comm.rotate_useragent.RotateUserAgentMiddleware' : 100,

                    'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': 200,
                   # 'myspider.comm.random_proxy.RandomProxyMiddleware': 300,

                  #  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 400,
                }

ITEM_PIPELINES = {
    'yg.pipelines.DuplicatesPipeline': 300,
}
