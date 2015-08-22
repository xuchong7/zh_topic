# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import sys
import MySQLdb
from pybloom import BloomFilter


class TopicPipeline(object):
    def process_item(self, item, topic):
        t_url = item['url'][0]
        t_name = item['topic_name']
        conn = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'mysqlpasswordtmac9232', db = 'scrapy')
        cursor = conn.cursor()

        conn.set_character_set('utf8')
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute(
            "insert into topic (url, title) values (%s, %s);", [t_url, t_name]
        )
        conn.commit()
        cursor.close()
        conn.close()
        return item