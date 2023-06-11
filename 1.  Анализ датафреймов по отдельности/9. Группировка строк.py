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

# print(products.groupby('CategoryName').ProductID.count().reset_index())  # Напоминаю reset_index() переводит серию в Data Frame
# print('\n')
# print(products.groupby('CategoryName').UnitPrice.min().reset_index())
# print(products.groupby('CategoryName').UnitPrice.agg(['min', max]).reset_index())
# print(products.groupby('CategoryName').agg({'UnitPrice': 'min', 'ProductID': 'count'}).reset_index())
# print(orders.groupby('ShippedDate', dropna=False).OrderID.count().reset_index())

"""Группировка 2 и более столбцам"""
# order_3 = orders.groupby(['EmployeeID', 'CustomerID']).OrderID.count().reset_index()
# print(order_3)

order_details['Discount_fact'] = order_details['UnitPrice'] * order_details['Quantity'] * order_details['Discount']
order_details['Revenue'] = order_details['UnitPrice'] * order_details['Quantity'] - order_details['Discount_fact']

order_details_1 = order_details.groupby('OrderID').agg({'Discount_fact': 'sum', 'Revenue': 'sum'}).reset_index()
order_details_1 = order_details_1.rename(columns={'Discount_fact': 'Discount', 'Revenue': 'Clean_revenue'}) #Переименовать столбцы
print(order_details_1)
