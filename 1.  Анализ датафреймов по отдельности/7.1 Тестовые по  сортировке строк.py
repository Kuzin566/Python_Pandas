import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

# print(products['CategoryName'].sort_values()) # Выведет отсортированную нужную колонку по алфавиту
# print(products.sort_values('CategoryName'))  # Выведен все строки с отсортированным определенным столбцом по филфавиту

# print(products['CategoryName'].sort_values(ascending=False))  # Выведет отсортированную нужную колонку по алфавиту в обратном порядке

# print(products.sort_values(['UnitPrice', 'CategoryName']))  # Сортировка по нескольким столбцам
orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
orders['OrderDate'] = orders['OrderDate'].dt.year
print(orders[orders['OrderDate'] == 1997].sort_values('Freight', ascending=True).sort_values('CustomerID', ascending=True))
