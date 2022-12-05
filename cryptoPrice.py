import requests
from bs4 import BeautifulSoup


#The while loop will update the price every second

def check_stock_price(url):
    while True:
#        url = 'https://www.marketwatch.com/investing/cryptocurrency/btcusd'
        page = requests.get(url)
        html = BeautifulSoup(page.text, 'lxml')
        price = html.find('bg-quote', class_ = 'value').text #inspect the price element on the webpage and put the tag first followed with the class

        print ("Bitcoin Price: ${}".format(price))

check_stock_price('https://www.marketwatch.com/investing/cryptocurrency/btcusd')
