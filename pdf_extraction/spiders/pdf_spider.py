import urllib
import scrapy
import os
from datetime import datetime
from pdf_extraction.items import PdfExtractionItem
# from scrapy.crawler import CrawlerProcess

from scrapy.http import Request


class pdf_extractor(scrapy.Spider):
    name = "pdf_extractor"

    # allowed_domains = ["www.pwc.com"]
    start_urls = ["https://www.privacy.gov.ph/memorandum-circulars/",
                  "https://www.privacy.gov.ph/data-privacy-act-primer/",
                  "https://www.privacy.gov.ph/advisories/",
                  "https://www.privacy.gov.ph/advisory-opinion"]



    def parse(self, response):


        base = 'https://www.privacy.gov.ph'

        for a in response.xpath('//a[@href]/@href'):
            link = a.extract()
            # self.logger.info(link)

            if link.endswith('.pdf'):

                link = urllib.parse.urljoin(base, link)
                self.logger.info(link)
                # name_pdf =
                yield Request(link, callback=self.save_pdf)




    def save_pdf(self, response):
        item = PdfExtractionItem()

        dirName = 'PDF_Directory'



        try:
            os.mkdir(dirName)
        except FileExistsError:
            print("Directory exists")
        path1 = response.url.split('/')
        path = response.url.split('/')[-1]


        item['Name'] = path
        item['Time'] = datetime.now()
        item['URL'] = response.url


        path = os.path.join(dirName , path)
        self.logger.info('Saving PDF %s', path1)
        with open(path, 'wb') as f:
            f.write(response.body)


        yield(item)

# process = CrawlerProcess({
#     'FEED_FORMAT' :'CSV',
#     'FEED_URI':'./data.csv'
# })
# process.crawl(pdf_extractor)
# process.start()