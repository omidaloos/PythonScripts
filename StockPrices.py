#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

def check_stock_price(ticker):
#    url = 'https://www.marketwatch.com/investing/stock/tsla?mod=search_symbol'
    url = 'https://www.marketwatch.com/investing/stock/' + ticker + '?mod=search_symbol'
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'lxml')
    price = html.find('bg-quote', class_ = 'value').text #inspect the price element on the webpage and put the tag first followed with the class

    print ("{} Price: ${}".format(ticker.upper(), price))

check_stock_price(input("Enter the stock ticker: "))

