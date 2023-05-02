
import requests 
from bs4 import BeautifulSoup 
from matplotlib import pyplot as plt   
from matplotlib import style
import numpy as np
import datetime
import pandas as pd


page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table',{'class':'mfd-table mfd-currency-table'})

rows = table.find_all('td')
rows = [i.text for i in rows]

date = rows[::3]
dollar = rows[1::3]
del dollar[0]
del date[0]
dollar_n = dollar.copy()
del dollar_n [2:]
del dollar_n [0]
dollar_now = ''
for i in dollar_n:
    dollar_now += str(i)


dollar1 = []
for i in dollar:
    float_i = float(i)
    dollar1.append(float_i)
dollar1.reverse()
date.reverse()


x = np.array(dollar1)
y = np.array([i for i in range(len(date))])
plt.plot(x, y)
plt.show()

print('доллар сейчас:', dollar_now)




        
        

