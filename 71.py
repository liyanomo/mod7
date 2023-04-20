import requests 
from bs4 import BeautifulSoup 

class Currency:

    DOLLAR_RUB = 'http://mfd.ru/currency/?currency=USD'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}



    def __init__(self):
        self.current_converted_price = float(self.get_currency_price().replace(",", "."))

    def get_currency_price1(self):
        full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')
        return soup
    print (get_currency_price1)


