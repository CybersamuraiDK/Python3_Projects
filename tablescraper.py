#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
TableScraper

All code in here should be universal for all tables!

@author: Cyber Samurai DK

"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import termcolor
from art import *

date_time = datetime.datetime.now()

art = text2art("TABLE WEBSCRAPER", font='small', chr_ignore=True)
print(termcolor.colored(art, 'green'))
print(termcolor.colored('BY CYBERSAMURAI DK', 'green'))
print(termcolor.colored(date_time.strftime("%H:%M %d-%B-%Y"), 'green'))
print()


#Hardcoded website
url = 'https://www.cryptocurrencychart.com/'


page = requests.get(url)
page.text
soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table', class_= 'market-cap-list', id = 'currency-table')

##############################################
table.find_all('th')

headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(columns = headers)

############################################

table.find_all('tr')[1:]

for j in table.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [td.text for td in row_data]
    length = len(df)
    df.loc[length] = row

############################################

df.to_excel('C:/scraping/scraped.xls')



    