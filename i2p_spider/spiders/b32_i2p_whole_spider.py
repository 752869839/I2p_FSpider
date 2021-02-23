# -*- coding: utf-8 -*-
import urllib
import langid
import chardet
import logging
from datetime import datetime
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from i2p_spider.items import I2pWholeNetworkItem

logger = logging.getLogger(__name__)

class I2pWholeSpider(RedisCrawlSpider):
    name = 'b32_i2p_whole_spider'
    redis_key = 'whole'
    # allowed_domains = ['i2p']

    rules = [
        Rule(LinkExtractor(allow=('\.*i2p.*'),
            restrict_xpaths=('//a[@href]')),
             callback='parse_item',
             follow=True)
    ]

    def __init__(self, *args, **kwargs):
        super(I2pWholeSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        item = I2pWholeNetworkItem()
        try:
            img_url_list = []
            img_urls = response.xpath('//img/@src').extract()
            for img_url in img_urls:
                img_url = response.urljoin(img_url)
                if '.jpg' in img_url or '.png' in img_url:
                    img_url_list.append(img_url)
            item['img_url'] = img_url_list
        except Exception as e:
            pass

        item['url'] = str(response.url)
        item['status'] = str(response.status)
        item['domain'] = urllib.parse.urlparse(response.url).netloc
        try:
            item['title'] = response.xpath('//html/head/title//text()').extract_first()
        except:
            item['title'] = ''
        try:
            item['description'] = response.xpath('//*[@name="description"]/@content').extract_first()
        except:
            item['description'] = ''
        try:
            item['keywords'] = response.xpath('//*[@name="keywords"]/@content').extract_first()
        except:
            item['keywords'] = ''
        try:
            item['html'] = str(response.body, encoding='utf-8')
        except:
            item['html'] = response.body.decode("utf", "ignore")
        item['language'] = langid.classify(response.body)[0]

        encoding = chardet.detect(response.body)
        for key, value in encoding.items():
            if key == 'encoding' and not value is None:
                item['encode'] = value

        item['crawl_time'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

        logger.info(response.url)
        yield item


