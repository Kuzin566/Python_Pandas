import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")


# products.hist()
# plt.show()
# products['UnitPrice'].hist()
# plt.show()
# products['CategoryID'].hist()
# plt.show()
# products['ProductID'].hist(bins=80)
# plt.show()
# print(customers)
# customers['ContactTitle'].hist(xrot='vertical', bins=12)  # это тема
# plt.show()
"""Количество клиентов в разрезе должностей можно визуализировать с помощью метода .plot(), 
передав в него параметр kind= 'bar' (тип диаграммы - столбчатая). Мы получим ту же гистограмму."""
customers.groupby('ContactTitle').CustomerID.count().plot(kind='bar')
plt.show()
products['UnitPrice'].plot(kind='hist')
plt.show()
"""Также у метода .plot() среди типов диаграмм есть гистограмма kind= 'hist'. Построить гистограмму можно и так:
df_p['UnitPrice'].plot(kind ='hist')
Но если с помощью метода .hist() можно строить гистограммы для любых типов данных, 
то метод .plot(kind= 'hist') работает только числовыми типами данных."""
