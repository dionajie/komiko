# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request

class KomikoPipeline(ImagesPipeline):
    #Name download version
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return '%s/%s' % (self.chapter,image_guid)

    def get_media_requests(self, item, info):
        print 'download images..'
        self.chapter = item['chapter']
        for image in item['image_urls']:
            yield Request(image)
