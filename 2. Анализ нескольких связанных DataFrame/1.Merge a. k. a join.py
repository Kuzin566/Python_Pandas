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

order_details['Discount_fact'] = order_details['UnitPrice'] * order_details['Quantity'] * order_details['Discount']
order_details['Revenue'] = order_details['UnitPrice'] * order_details['Quantity'] - order_details['Discount_fact']
# print(order_details)
# print(orders)
# orders = orders.merge(order_details)
# print(orders)
# orders_1 = orders.groupby('EmployeeID').Revenue.sum().reset_index()
# print(orders_1)

# customers = customers[['CustomerID', 'ContactName']]
# orders = customers.merge(orders, how='left')
# print(orders[orders['OrderID'].isnull()])

"""Мержить явно по ключу"""
od = order_details.merge(products, left_on='ProductID', right_on='ProductID', suffixes=('_old', '_actual'))
print(od)
