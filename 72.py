import matplotlib.pyplot as plt
import parser_01

yandex = parser_01.RateParser('https://yandex.ru/news/quotes/1.html')
usd_table_dict = yandex.site_processing('div', 'news-stock-table__cell')
dates = [i for i in reversed(usd_table_dict)]
value_usd = [usd_table_dict[i] for i in dates]
plt.plot(dates, value_usd)
plt.show()