import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
orders['ShippedDate'] = orders['ShippedDate'].astype('datetime64[ns]')
orders['RequiredDate'] = orders['RequiredDate'].astype('datetime64[ns]')

orders['year'] = orders['OrderDate'].dt.year
orders['month'] = orders['OrderDate'].dt.month
orders['day'] = orders['OrderDate'].dt.day
orders['week'] = orders['OrderDate'].dt.isocalendar().week
orders['quarter'] = orders['OrderDate'].dt.quarter

"""df_o = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Orders.csv', sep = ';')
С помощью метода .pivot_table() постройте сводную таблицу, в которой по вертикали будут годы, а по горизонтали кварталы. 
Посчитайте количество заказов. Сколько заказов было оформлено в 1 квартале 1998 года?"""

print(orders.pivot_table(index='year', columns='quarter', values='OrderID', fill_value=0, aggfunc='count').reset_index())
