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


# print(customers)
# print(customers.groupby('ContactTitle').CustomerID.count())

# order_1 = orders.groupby('EmployeeID').OrderID.count().reset_index()
# print(order_1.sort_values('OrderID'))

# order_2 = orders.groupby('OrderDate').OrderID.count().reset_index()
# print(order_2.sort_values('OrderID', ascending=False))

# order_3 = orders.groupby(['EmployeeID', 'CustomerID']).OrderID.count().reset_index()
# print(order_3.sort_values('OrderID', ascending=False))

order_details['Discount_fact'] = order_details['UnitPrice'] * order_details['Quantity'] * order_details['Discount']
order_details['Revenue'] = order_details['UnitPrice'] * order_details['Quantity'] - order_details['Discount_fact']
# print(order_details)

od_1 = order_details.groupby('OrderID').Discount_fact.sum().reset_index()
print(od_1[od_1['Discount_fact'] > 2000])
# od_2 = order_details.groupby('OrderID').Revenue.sum().reset_index()
# print(od_2.sort_values(by='Revenue', ascending=False))
