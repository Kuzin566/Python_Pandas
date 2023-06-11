import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')

# print(customers)
customers_1 = customers[(customers['ContactTitle'] == 'Sales Representative') | (customers['ContactTitle'] == 'Owner')]
# print(customers_1.ContactTitle.count())

# print(orders['Freight'].agg(['min', 'max']).diff())

orders_1 = orders[orders['OrderDate'] == '1998-02-26']
print(orders_1.Freight.sum())
