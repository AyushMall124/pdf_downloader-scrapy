# 1. Clone this repository into a local Repository 


# 2. Find the spider code in:
```
"pdf_downloader-scrapy/pdf_extraction/spiders/pdf_spider.py"

```

# 3. Run the project:
Open the terminal in the folder containing the 'pdf_spider.py' and run the following command:
```
 scrapy crawl pdf_extractor -o Data_final.csv -t csv   
 
 ```


The above-mentioned code will enable the spider to crawl the web, find the PDF and download them to a folder called ` PDF_Directory `
and save relevant data into a CSV called `Data_final.csv` , both present in the same folder as the spider.
