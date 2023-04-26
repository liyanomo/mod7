
import requests 
from bs4 import BeautifulSoup 

class Currency:

    link = 'http://mfd.ru/currency/?currency=USD'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    current_converted_price = {} 

    def get_currency_price1(self):

        full_page = requests.get(self.link, headers=self.headers)

        soup = BeautifulSoup(full_page.text, 'html.parser') 
        dollar = soup.findAll('table', {'class': 'mfd-table mfd-currency-table'}) 
        dollar_now = [usd.text for usd in dollar]

        for data in range(5, len(dollar_now), 5):
            current_converted_price[dollar_now[data]] = dollar_now[data + 1]
        for i in current_converted_price:
            current_converted_price[i] = float(current_converted_price.replace(',', '.'))
        return current_converted_price
c = Currency()
print(c.get_currency_price1())


        
        

