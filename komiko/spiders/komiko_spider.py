
from scrapy import Spider
from scrapy.selector import Selector
from komiko.items import KomikoItem
import urlparse

class KomikoSpider(Spider):
    name = "mangacan"
    def __init__(self, manga='', chapter=''):
        self.chapter = chapter
        self.manga = manga
        allowed_domains = ["http://mangacanblog.com/"]
        next_chapter = int(self.chapter) + 1
        self.start_urls = [
            "http://mangacanblog.com/baca-komik-"+str(self.manga)+"-"+str(self.chapter)+"-"+str(next_chapter)+"-bahasa-indonesia-"+str(self.manga)+"-"+str(chapter)+"-terbaru.html"
        ]

    def parse(self, response):
        items = []
        images = response.xpath("//div[@id='imgholder']")
        for image in images:
            item = KomikoItem()  
            item['chapter'] = '%s %s' %(self.manga,self.chapter)
            item['image_urls'] = [urlparse.urljoin(response.url, u) for u in images.xpath("center/a/div/img/@src").extract()]
            return item
