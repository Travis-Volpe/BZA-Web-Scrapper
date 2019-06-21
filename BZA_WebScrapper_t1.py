#This is a test script for configuring scraply to work with the BZA Calendar website

#Create a virtual environment and install the necessary packages
import scrapy

# Create a Scrapy project for crawling the BZA Calendar using the folowing command line:
# $ scrapy startproject BZA_Calendar
# to create a crawler you will add a new file inside the spiders directory
# BZA_Calendar/BZA_Calendar/spiders/Calendar.py

class CalendarSpider(scrapy.spider):
    name='Calendar'

    def start_requests(self):
        urls = ['insert BZA_Calendar URL here']
        return [scrapy.Requests(url=url, callback=self.parse)
            for url in urls]

        def parse(self, response):
            url = response.url
            title = response.css('h1::text').extract_first()
            print('URL is: {}'.format(url))
            print('Title is: {}'.format(title))
