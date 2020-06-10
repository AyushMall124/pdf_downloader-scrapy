import urllib
import scrapy
import os
from datetime import datetime
from pdf_extraction.items import PdfExtractionItem
# from scrapy.crawler import CrawlerProcess

from scrapy.http import Request


class pdf_extractor(scrapy.Spider):
    name = "pdf_extractor"


    start_urls = ["https://www.privacy.gov.ph/memorandum-circulars/",
                  "https://www.privacy.gov.ph/data-privacy-act-primer/",
                  "https://www.privacy.gov.ph/advisories/",
                  "https://www.privacy.gov.ph/advisory-opinion"]                #list of urls to be searched on



    def parse(self, response):


        base = 'https://www.privacy.gov.ph'                        #base url for the pdf link

        for a in response.xpath('//a[@href]/@href'):               #looking for <a> with 'href' , and then extracting the value of 'href'using xpath. Could have also used css.selection
            link = a.extract()                                   # gets all occurences
            # self.logger.info(link)

            if link.endswith('.pdf'):                                #finding links ending with .pdf"

                link = urllib.parse.urljoin(base, link)
                self.logger.info(link)
                # name_pdf =
                yield Request(link, callback=self.save_pdf)               #requesting from the url, and calling a function to operate on the response








    def save_pdf(self, response):
        item = PdfExtractionItem()                                       #creating an item to store relevant information

        dirName = 'PDF_Directory'



        try:
            os.mkdir(dirName)
        except FileExistsError:
            print("Directory exists")
        path1 = response.url.split('/')
        path = response.url.split('/')[-1]          #getting the name of the pdf file


        item['Name'] = path
        item['Time'] = datetime.now()
        item['URL'] = response.url


        path = os.path.join(dirName , path)
        self.logger.info('Saving PDF %s', path1)             #saving pdfs into the folder
        with open(path, 'wb') as f:
            f.write(response.body)


        yield(item)

# process = CrawlerProcess({
#     'FEED_FORMAT' :'CSV',
#     'FEED_URI':'./data.csv'
# })
# process.crawl(pdf_extractor)
# process.start()