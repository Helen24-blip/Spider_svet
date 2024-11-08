import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        lights = response.css('div.LlPhw')
        for light in lights:
            yield{
               'name' : light.css('div.lsooF span::text').get(),
               'price' : light.css('div.pY3d2 span::text').get(),
                'url' : light.css('a').attrib['href']
            }

