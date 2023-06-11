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

# print(orders)
orders['year'] = orders['OrderDate'].dt.year
orders['month'] = orders['OrderDate'].dt.month
orders['week'] = orders['OrderDate'].dt.isocalendar().week

"""df_o = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Orders.csv', sep = ';')
В каком месяце было совершено рекордное количество заказов? Месяц запишите в формате 062022."""
# order_1 = orders.groupby(['year', 'month']).OrderID.count().reset_index()
# print(order_1.sort_values('OrderID', ascending=False))

"""df_o = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Orders.csv', sep = ';')
Сколько заказов было сделано на 43 неделе 1996 года?"""
# order_2 = orders.groupby(['week', 'year']).OrderID.count().reset_index()
# print(order_2[(order_2['week'] == 43) & (order_2['year'] == 1996)])

"""df_o = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Orders.csv', sep = ';')
df_od = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Order_details.csv', sep = ';')
Посчитайте рекордную чистую выручку, которую сделал один сотрудник в месяц?"""
# print(order_details)

new_db = orders.merge(order_details)

new_db = new_db.groupby(['EmployeeID', 'year', 'month']).Revenue.sum().reset_index()
print(new_db.sort_values('Revenue', ascending=False))
