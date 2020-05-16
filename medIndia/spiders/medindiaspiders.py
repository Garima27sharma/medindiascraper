import scrapy

from medIndia.items import MedindiaItem


class MedindiaSpider(scrapy.Spider):
    name = "medIndia"
    allowed_domains = ["medindia.net"]
    start_urls="https://www.medindia.net/drug-price/brand-index.asp?alpha=a&page=1"

    def start_requests(self):
        start_urls = "https://www.medindia.net/drug-price/brand-index.asp?alpha=a&page=1"
                        


        # for url in urls:
        yield scrapy.Request(url=start_urls, callback=self.inititialize)


    def inititialize(self, response):
        for url in response.css('table.table-bordered.table > tr > td > a::attr(href)').extract():
            url = response.urljoin(url)
            yield response.follow(url, callback=self.parse_details)


        next_page_urls= response.css("a[title='Next Page']::attr(href)").extract()
        if len(next_page_urls) == 1:
               next_page_url = response.urljoin(next_page_urls[0])
               yield scrapy.Request(url=next_page_url, callback=self.inititialize)

    def parse_details(self, response):
        item = MedindiaItem()

        item['drug_name'] = response.css("td > h1::text").extract()
        item['drug_form'] = response.css("td > span::text")[0].extract()
        item['generic_name'] = response.css("td > span::text")[1].extract()
        item['price'] = response.css("div.ybox > b::text").extract()
        item['dosage'] = response.css("div.ybox > span > b::text")[0].extract()
        item['conditions'] = response.css("div.caption > b > a::text").extract()
        item['side_Effects'] = response.xpath('//p[@class="drug-content"][1]/text()').extract()
        item['indications'] = response.xpath('//p[@class="drug-content"][2]/text()').extract()
        item['how_To_Take'] = response.xpath('//p[@class="drug-content"][3]/text()').extract()
        item['contraindications'] = response.xpath('//p[@class="drug-content"][4]/text()').extract()
        item['warning'] = response.xpath('//p[@class="drug-content"][5]/text()').extract()
        item['other_Precautions'] = response.xpath('//p[@class="drug-content"][6]/text()').extract()
        item['storage'] = response.xpath('//p[@class="drug-content"][7]/text()').extract()

        yield item




