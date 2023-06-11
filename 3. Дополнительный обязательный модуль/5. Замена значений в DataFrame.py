import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

# order_details['Discount_fact'] = order_details['UnitPrice'] * order_details['Quantity'] * order_details['Discount']
# order_details['Revenue'] = order_details['UnitPrice'] * order_details['Quantity'] - order_details['Discount_fact']

# orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
# orders['ShippedDate'] = orders['ShippedDate'].astype('datetime64[ns]')
# orders['RequiredDate'] = orders['RequiredDate'].astype('datetime64[ns]')

# print(orders)
"""#Заполнить этим значением пустые поля"""
orders['ShippedDate'] = orders['ShippedDate'].fillna('2022-06-11 00:00:00.000')
# print(orders['ShippedDate'].tail())

"""заменить значение на значение"""
orders['ShippedDate'] = orders['ShippedDate'].replace('2022-06-11 00:00:00.000', '2023-06-11 00:00:00.000')
# print(orders['ShippedDate'].tail())

"""ЗАменить определенное значение используя условия"""
orders['ShippedDate'] = orders['ShippedDate'].replace('2022-06-11 00:00:00.000', '2023-06-11 00:00:00.000')

print(len(customers.iloc[0:-71]))
