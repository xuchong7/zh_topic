# -*- coding: utf-8 -*-

# Scrapy settings for zh_topic project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'zh_topic'

SPIDER_MODULES = ['zh_topic.spiders']
NEWSPIDER_MODULE = 'zh_topic.spiders'

ITEM_PIPELINES = {
	'zh_topic.pipelines.TopicPipeline': 100
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zh_topic (+http://www.yourdomain.com)'
