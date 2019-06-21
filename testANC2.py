import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup

#outfile = open("test_table.csv", "w", newline='')
#writer = csv.writer(outfile)

url = 'https://app.dcoz.dc.gov/Content/Schedule/PublicSearch.aspx?keyWord=anc1A'
html = requests.get(url)
#pagetext = page.text

#anc_table = {
#    "Date" : [],
#    "Board/Commission" : [],
#    "Case Number" : [],
#    "Case Name" : [],
#    "Result" : []
#}

soup  = BeautifulSoup(html, 'lxml')
table = soup.find('table')

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th", "td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

for item in list_of_rows:
    print(' '.join(item))

#file = open("test_table.csv", 'w')
#
#for row in tree.find_all('tr'):
#    for col in row.find_all('td'):
#        print(col.text)
#
#tree = BeautifulSoup(html,"lxml")
#table_tag = tree.select("table")[0]
#tab_data = [[item.text for item in row_data.select("th,td")]
#                for row_data in table_tag.select("tr")]
#
#for data in tab_data:
#    writer.writerow(data)
#    print(' '.join(data))


