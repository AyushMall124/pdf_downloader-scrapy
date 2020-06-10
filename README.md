# 1. Clone this repository into a local Repository 




# 2. [Optional] To make sure all the dependent libraries are present in your system , open the terminal in the repository and run the following code:
```
pip install -r requirements.txt

```

# 3. Find the spider code in:
```
"pdf_downloader-scrapy/pdf_extraction/spiders/pdf_spider.py"

```

# NOTE: Delete the pre-existing `Data_final.csv` and `PDF_Directory` in the folder to see the change


# 4. Run the project:
Open the terminal in the folder containing the 'pdf_spider.py' and run the following command:
```
 scrapy crawl pdf_extractor -o Data_final.csv -t csv   
 
 ```


The above-mentioned code will enable the spider to crawl the web, find the PDF and download them to a folder called ` PDF_Directory `
and save relevant data into a CSV called `Data_final.csv` , both present in the same folder as the spider.
