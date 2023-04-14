from matplotlib import pyplot as plt   
from matplotlib import pyplot as plt  
 
percentage = parser_01.RateParser('https://yandex.ru/news/quotes/1.html') 
Ruble = [0,10,20,30,40,50,60,70,80,90,100]   
plt.hist(USD, Ruble, histtype='bar', rwidth=0.8)   
plt.xlabel('USD')   
plt.ylabel('Ruble')   
plt.title('USD & Ruble')   
plt.show() 