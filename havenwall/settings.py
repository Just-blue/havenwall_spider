# -*- coding: utf-8 -*-

# Scrapy settings for havenwall project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'havenwall'

SPIDER_MODULES = ['havenwall.spiders']
NEWSPIDER_MODULE = 'havenwall.spiders'

IMAGES_THUMBS = {
    'small': (50, 50),
    'big': (270, 270),
}

IMAGES_MIN_HEIGHT = 110
IMAGES_MIN_WIDTH = 110

IMAGES_STORE = '/Users/pokker/Pictures'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'havenwall (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    ':authority': 'alpha.wallhaven.cc',
    ':method': 'GET',
    ':path': '/',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #  'accept-encoding':'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d1b3e0ec4ee01bedc08f609cd93a709d51511108514; _gat=1; _ga=GA1.2.1156805805.1511228989; _gid=GA1.2.764876764.1511486227; wallhaven_session=eyJpdiI6InBQSUw1TjFncURLZldPblwvWExhZ3NTRytkaFFqTURqR0daUG9OYTRNVjdZPSIsInZhbHVlIjoiZERtdUxON0NRNUl5cWtMbVpVNWE2XC9wT0FGdUdxUFVcL3llTEJyaGh5cW5ScWRremQwdzBIXC9vSDBuajltbmc0U1VRMDBOSDFoV2NKalRBWmRpdmJEcXc9PSIsIm1hYyI6IjU4NjM4YTM5Zjg4ZDJjNzM0Mzg5MTdkMmNjZTExZDBhNWZiY2Y5NmE0MDc0MzM4ODM4ZDlmNTIzYmIzNWU4M2IifQ%3D%3D',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'havenwall.middlewares.HavenwallSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'havenwall.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'havenwall.pipelines.MyImagesPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
