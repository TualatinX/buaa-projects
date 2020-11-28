import scrapy
from pkx_flight.items import PkxFlightItem

class PkxFlightSpiderSpider(scrapy.Spider):
    name = 'pkx_flight_spider'
    allowed_domains = ['data.carnoc.com']
    start_urls = ['http://http://data.carnoc.com/corp/airport/nkg__airportflight.html/']

    def parse(self, response):
        items=[]
        item = PkxFlightItem()
        item['type'] = "进港"
        items.append(item)
        yield(item)

        node_list = response.xpath("//div[@id='icefable1']/li")
        
        for node in node_list:
            item = PkxFlightItem()

            number = node.xpath("./span[1]/text()").extract()
            city = node.xpath("./span[2]/text()").extract()
            terminal = node.xpath("./span[3]/text()").extract()
            expected = node.xpath("./span[4]/text()").extract()
            actual = node.xpath("./span[5]/text()").extract()
            state = node.xpath("./span[6]/text()").extract()

            item['number'] = number[0]
            item['city'] = city[0]
            item['terminal'] = terminal[0]
            item['expected'] = expected[0]
            item['actual'] = actual[0]
            item['state'] = state[0]
            items.append(item)
            yield(item)
        
        item = PkxFlightItem()
        item['seperate'] = "----------------------------------------------"
        items.append(item)
        yield(item)

        item = PkxFlightItem()
        item['type'] = "出港"
        items.append(item)
        yield(item)

        node_list = response.xpath("//div[@id='icefable2']/li")
        for node in node_list:
            item = PkxFlightItem()
            number = node.xpath("./span[1]/text()").extract()
            city = node.xpath("./span[2]/text()").extract()
            terminal = node.xpath("./span[3]/text()").extract()
            expected = node.xpath("./span[4]/text()").extract()
            actual = node.xpath("./span[5]/text()").extract()
            state = node.xpath("./span[6]/text()").extract()

            item['number'] = number[0]
            item['city'] = city[0]
            item['terminal'] = terminal[0]
            item['expected'] = expected[0]
            item['actual'] = actual[0]
            item['state'] = state[0]
            items.append(item)
            yield(item)