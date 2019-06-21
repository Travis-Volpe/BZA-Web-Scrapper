import csv
import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

#outfile = open("test_table.txt", "w", newline='')
#writer = csv.writer(outfile)

url = 'https://app.dcoz.dc.gov/Content/Schedule/PublicSearch.aspx?keyWord=anc1A'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'lxml')

table = soup.find("div",id="Anthem_dgResults__")

df = pd.read_html(str(table))

print(tabulate(df, headers='keys', tablefmt='psql'))

#file = open("test_table.csv", 'w')

#for row in tag.find_all('tr'):
#    for col in row.find_all('td'):
#        print(col.text)

