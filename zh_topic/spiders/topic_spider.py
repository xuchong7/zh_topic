from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.shell import inspect_response

from zh_topic.items import TopicItem


class TopicSpider(Spider):
    name = 'topic'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'http://www.zhihu.com/topic/19776749'
    ]

    def parse(self, response):
        sel = Selector(response)
        child_topics = sel.xpath('//div[@class="zm-side-section-inner child-topic"]/div/a[@class="zm-item-tag"]')

        print child_topics
        items = []
        newUrls = []
        if(child_topics !=[]):
            for topic in child_topics:
                item = TopicItem()
                s = topic.xpath('.//text()').extract()
                for a in s:
                    item['topic_name'] = a.replace('\n', '')
                item['url'] = topic.xpath('.//@href').extract()
                newUrl = 'http://www.zhihu.com' + str(item['url']).replace('[','').replace(']', '').replace('\'', '').replace('u', '')
                print newUrl
                print ''
                newUrls.append(newUrl)
                items.append(item)

            items.extend(self.make_requests_from_url(url).replace(callback = self.parse) for url in newUrls)

        return items