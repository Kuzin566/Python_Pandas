import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

# print(orders.head())
# print(orders.dtypes)
orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')

# a = orders[orders.OrderDate > '1997-07-05']
# print(a.shape)

# print(orders.head())
# a = orders[orders.Freight <= 10.98]
# print(a.shape)

# print(customers.head())
# df = customers[customers['ContactTitle'].isin(
#     ['Sales Representative', 'Sales Agent', 'Sales Associate', 'Sales Manager', 'Assistant Sales Agent',
#      'Assistant Sales Representative'])]  # Не забываем ~ означает что не соответсвует условиям
# print(df.shape)

# print(products.head())
# df = products[products['UnitPrice'].between(18, 22)]  # Не забываем ~ означает что не соответсвует условиям
# print(df.shape)

print(orders.head())
df = orders[(orders['Freight'] > 500) | (orders['OrderDate'].between('1997-01-01', '1997-12-31'))]
print(df.shape)
