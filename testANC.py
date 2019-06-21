import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup

outfile = open("test_table.csv", "w", newline='')
writer = csv.writer(outfile)

url = 'https://app.dcoz.dc.gov/Content/Schedule/PublicSearch.aspx?keyWord=anc1A'
page = requests.get(url)

#anc_table = {
#    "Date" : [],
#    "Board/Commission" : [],
#    "Case Number" : [],
#    "Case Name" : [],
#    "Result" : []
#}

tree = BeautifulSoup(page.text, 'lxml')

file = open("test_table.csv", 'w')

for row in tree.find_all('tr'):
    for col in row.find_all('td'):
        print(col.text)

#tree = BeautifulSoup(html,"lxml")
#table_tag = tree.select("table")[0]
#tab_data = [[item.text for item in row_data.select("th,td")]
#		for row_data in table_tag.select("tr")]
#
#for data in tab_data:
#    writer.writerow(data)
#    print(' '.join(data))
#
#url = 'https://app.dcoz.dc.gov/Content/Schedule/PublicSearch.aspx?keyWord=anc1A'
#page = requests.get(url)
#pagetext = page.text

#anc_table = {
   # "Date" : [],
   # "Board/Commission" : [],
   # "Case Number" : [],
   # "Case Name" : [],
   # "Result" : []
#}

#soup = BeautifulSoup(pagetext, 'html.parser')

#file = open("test_table.csv", 'w')

#for row in soup.find_all('tr'):
    #for col in row.find_all('td'):
        #print(col.text)




#for i in range(20):
   # url = 'https://app.dcoz.dc.gov/Content/Schedule/PublicSearch.aspx?keyWord=anc1A'
   # url_get = requests.get(url)
   # soup =  BeautifulSoup(url_get.content, 'lxml')


#url = 'http://CNN.com'
#url = 'https://app.dcoz.dc.gov/Calendar/Calendar.aspx'
#url_get = requests.get(url)

#lxml was slower than html.parser?

#soup =  BeautifulSoup(url_get.content, 'lxml')
#print(soup.find('title').text)





