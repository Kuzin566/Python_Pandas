import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

order_details['Discount_fact'] = order_details['UnitPrice'] * order_details['Quantity'] * order_details['Discount']
order_details['Revenue'] = order_details['UnitPrice'] * order_details['Quantity'] - order_details['Discount_fact']

orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
orders['ShippedDate'] = orders['ShippedDate'].astype('datetime64[ns]')
orders['RequiredDate'] = orders['RequiredDate'].astype('datetime64[ns]')

"""df_od = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Order_details.csv', sep = ';')
Посчитайте для каждого заказа чистую выручку. 
Затем помощью метода .cut() разбейте столбец с чистой выручкой на 5 бинов.
Добавьте столбец с бинами в датафрейм. Далее в разрезе бинов посчитайте количество заказов. 
 Сопоставьте бин и количество заказов в бине."""
# products['bins'] = pd.cut(products['UnitPrice'], bins=4)
"""Можно разбивку делать следуюзим образом
bins=[0,10,20,30]"""
od = order_details.groupby('OrderID').Revenue.sum().reset_index()
od['bins'] = pd.cut(od['Revenue'], bins=5)
bd = od.groupby('bins').OrderID.count().reset_index
print(bd)

"""df_od = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Order_details.csv', sep = ';')
Посчитайте для каждого заказа чистую выручку. Затем с помощью метода .qcut() разбейте столбец с чистой выручкой на 5 бинов. 
Добавьте столбец с бинами в датафрейм. Далее в разрезе бинов посчитайте количество заказов. 
Выберите диапазон первого бина."""

od_2 = order_details.groupby('OrderID').Revenue.sum().reset_index()
od_2['bins'] = pd.qcut(od['Revenue'], 5)
od_2 = od.groupby('bins').OrderID.count().reset_index
print(od_2)
