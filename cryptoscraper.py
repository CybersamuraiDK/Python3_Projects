#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CryptoCurrency Webscraper

@author: Cyber Samurai DK

"""

from bs4 import BeautifulSoup
import requests
import datetime
import termcolor
from art import *

date_time = datetime.datetime.now()

art = text2art("CRYPTO WEBSCRAPER", font='small', chr_ignore=True)
print(termcolor.colored(art, 'green'))
print(termcolor.colored('BY CYBERSAMURAI DK', 'green'))
print(termcolor.colored(date_time.strftime("%H:%M %d-%B-%Y"), 'green'))
print()

#Hardcoded websites
url = 'https://coinmarketcap.com/currencies/bitcoin/'
url2 = 'https://coinmarketcap.com/currencies/dogecoin/'
url3 = 'https://coinmarketcap.com/currencies/ethereum/'


page = requests.get(url)
page.text
soup = BeautifulSoup(page.text, 'lxml')

page2 = requests.get(url2)
page2.text
soup2 = BeautifulSoup(page2.text, 'lxml')

page3 = requests.get(url3)
page3.text
soup3 = BeautifulSoup(page3.text, 'lxml')


################################

btcname = "BitCoin" 

btcvalue = soup.find_all('div', class_='priceValue___11gHJ')[0]
btcvalue.text

btcmarket = soup.find_all('div',  class_= "statsValue___2iaoZ")[0]
btcmarket.text

print(btcname)
print('Value: ' + btcvalue.text)
print('Market Cap: ' + btcmarket.text + '\n')

###############################

dogename = "DogeCoin"
dogevalue = soup2.find_all('div', class_= 'priceValue___11gHJ')[0]
dogevalue.text

dogemarket = soup2.find_all('div', class_= 'statsValue___2iaoZ')[0]
dogemarket.text

print(dogename)
print('Value: ' + dogevalue.text)
print('Market Cap: ' + dogemarket.text + '\n')

##############################

ethname = "Ethereum"
ethvalue = soup3.find_all('div', class_= 'priceValue___11gHJ')[0]
ethvalue.text

ethmarket = soup3.find_all('div', class_= 'statsValue___2iaoZ')[0]
ethmarket.text

print(ethname)
print('Value: ' + ethvalue.text)
print('Market Cap: ' + ethmarket.text + '\n')

