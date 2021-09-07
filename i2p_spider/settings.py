# -*- coding: utf-8 -*-

# Scrapy settings for i2p_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from datetime import datetime
from elasticsearch import Elasticsearch

#proxy
HTTP_PROXY = ["http://8.210.121.248:39904","http://47.56.197.215:39901","http://139.180.220.76:4000","http://139.180.220.76:4001","http://139.180.220.76:4002","http://139.180.220.76:4003","http://139.180.220.76:4004"]

# redis
REDIS_HOST = '172.16.30.65'
REDIS_PORT = '6379'
# REDIS_PARAMS = {
#     # 'password': '',
#     'db': 1
# }

# elasticsearch
e_host='172.16.30.68'
e_port=9200
es_conn = Elasticsearch(hosts=e_host, port=e_port, timeout=30, max_retries=10)


#seaweedfs
s_host='172.16.30.24'
s_port=8888
IMAGES_STORE =  f'weed://{s_host}:{s_port}/crawler'
ENABLE_IMAGE_SAVE = True
IMAGES_EXPIRES = 90

BOT_NAME = 'i2p_spider'

SPIDER_MODULES = ['i2p_spider.spiders']
NEWSPIDER_MODULE = 'i2p_spider.spiders'

#scrapy_redis
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 使用scrapy_redis 里的去重组件，不使用scrapy默认的去重方式
SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # 使用scrapy_redis 里的调度器组件，不使用默认的调度器
SCHEDULER_PERSIST = True    # 允许暂停，redis请求记录不丢失
# SCHEDULER_FLUSH_ON_START = True  # 自动清理redis里面的key

# 使用优先级调度请求队列 （默认使用）
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
# 可选的 按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# 可选的 按后进先出排序（LIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'i2p_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'
today = datetime.now()
log_file_path = "log/spiders-{}-{}-{}.log".format(today.year, today.month, today.day)
LOG_FORMAT='%(asctime)s [%(name)s] %(levelname)s: %(message)s'
LOG_DATEFORMAT='%Y-%m-%d %H:%M:%S'
#LOG_FILE = log_file_path    #日志保存为文件

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.01

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 0
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 3
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

#爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
DEPTH_LIMIT = 5

#0表示深度优先Lifo(默认)；1表示广度优先FiFo
# 后进先出，深度优先
# DEPTH_PRIORITY = 0
# SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleLifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.LifoMemoryQueue'
# 先进先出，广度优先
# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'

# MYEXT_ENABLED=True      # 开启扩展
IDLE_NUMBER=300         # 配置空闲持续时间单位为 300个 ，一个时间单位为5s

# 在 EXTENSIONS 配置，激活扩展
EXTENSIONS= {
            'i2p_spider.extensions.RedisSpiderSmartIdleClosedExensions': 500,
        }

# DOWNLOAD_TIMEOUT = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Connection':'keep-alive',
'Upgrade-Insecure-Requests': '1' ,
}
USER_AGENT_TYPE = 'random'   #fake_useragent

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'i2p_spider.middlewares.I2pWholeNetworkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'i2p_spider.middlewares.HttpProxyDownloadMiddleware': 156,
    'i2p_spider.middlewares.StickyDepthSpiderMiddleware' : 101
   # 'i2p_spider.middlewares.RandomUserAgentMiddleware': 200,
   # 'i2p_spider.middlewares.TorWholeNetworkDownloaderMiddleware': 543,
}


# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 100,
   # 'i2p_spider.pipelines.I2pWholeNetworkPipeline': 355,
   # 'i2p_spider.pipelines.DownloadImagesPipeline': 288,
}

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
