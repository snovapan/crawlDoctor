# -*- coding: utf-8 -*-
import scrapy
import copy
from scrapy.spiders import CrawlSpider
from crawlDoctor.items import DoctorItem


class DoctorSpider(CrawlSpider):
    name = 'doctor'
    allowed_domains = ['guahao.com']
    # 医院链接
    start_urls = ['https://www.guahao.com/hospital/FF0153A8F0542010E0430F01A8C07495000',
                  'https://www.guahao.com/hospital/9868536f-c720-11e1-913c-5cf9dd2e7135000']

    def parse(self, response):
        # 医院名称
        hospitalname = response.xpath('//*[@id="g-cfg"]/div[2]/section/div[1]/div[2]/h1/strong/a/text()').extract()[0]
        for each in response.xpath("//*[@id='departments']/div[2]/ul/li"):
            # 大科室
            bigdept = each.xpath("./label/text()").extract()[0].strip()
            for line in each.xpath("./p/span"):
                item = DoctorItem()
                # 医院名称
                item['hospitalname'] = hospitalname
                # 科室链接
                item['deptlink'] = line.xpath('./a/@href').extract()[0].strip()
                # 大科室
                item['bigdept'] = bigdept
                # 小科室
                item['smalldept'] = line.xpath('./a/text()').extract()[0].strip()

                yield scrapy.Request(url=item['deptlink'], meta={'dept': item}, callback=self.doctor_parse)


    def doctor_parse(self, response):
        dept = response.meta['dept']
        for each in response.xpath('//*[@id="anchor"]/div[2]/div[@class="g-clear g-doc-info"]'):
            name = each.xpath('./dl/dt/a/text()').extract()[0].strip()
            title = each.xpath('./dl/dt/span/text()').extract()[0].strip()
            introduction = each.xpath('./dl/dd/p/text()').extract()[0].strip()
            item = copy.deepcopy(dept)
            item['name'] = name
            item['title'] = title
            item['introduction'] = introduction
            # 把数据交给管道文件
            yield item