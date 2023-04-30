
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

del date[6:]
del dollar [6:]



df = pd.DataFrame({'date ': np.array([datetime. datetime (2023, 4, i+1)
for i in range(12)]),
 'dollar' : [dollar] })


plt.plot (df.date , df.dollar , linewidth= 3 )
plt.title('currency')
plt.xlabel('date')
plt.ylabel('dollar')


#ata = pd.DataFrame({'date ': np.array([datetime. datetime (2020, 1, i+1)
 #for i in range(12)]),
#dollar = np.array(dollar)

#plt.hist(data, dollar, histtype='bar', rwidth=0.8)   
#plt.title("currency")
#plt.ylabel('data')
#plt.xlabel('dollar')
 
plt.show()

print(date)




        
        

