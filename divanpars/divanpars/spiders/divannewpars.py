import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/perm/category/svet"]

    def parse(self, response):
        svets = response.css('div.LlPhw')
        for svet in svets:
            yield {
                'name' : svet.css('div.lsooF span::text').get(),
                'price' : svet.css('div.pY3d2 span::text').get(),
                'url' : svet.css('a').attrib['href']
            }
