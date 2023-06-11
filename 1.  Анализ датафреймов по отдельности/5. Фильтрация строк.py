import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

print(orders.head())
print(orders.dtypes)
orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
# print(products[products.CategoryName == 'Condiments'])  # Вывести только те строки, где CategoryName == 'Condiments']
# print(orders[orders.ShippedDate.isnull()])  # вывести все строки где в вуказанном столбце Nan(Пустота)
"""что бы отобразить те строки где не подходит нужно нам условие, можно использовать два варианта
использовать ~
print(products[~(products.CategoryName == 'Condiments')]), что как по мне пред ебучий
Либо просто !=
print(products[(products.CategoryName != 'Condiments'])
"""
# print(orders[orders.ShippedDate.isnull()])  # вывести все строки где в вуказанном столбце Nan(Пустота) если хоти где не Null, то используем notnull()

# df = orders[orders['Freight'].between(10, 20)]  # чтобы не включать 10 и 20 то делаем between(10,20, inclusive='neither')
"""inclusive = 'both' - захватывает обе границы диапазона. По умолчанию параметр не указывается .between(10,20);
inclusive = 'neither' - не захватывает границы диапазона;
inclusive = 'left' - захватывает левую границу диапазона;
inclusive = 'right' - захватывает правую границу диапазона."""
# #.between() - это метод для фильтрации по диапазону, а .isin() - метод для фильтрации по нескольким рандомным значениям, например: 3, 10, 89
# print(df)
# df = orders[~(orders['EmployeeID'].isin([2, 4, 6]))]  #Не забываем ~ означает что не соответсвует условиям
# print(df)

"""Фильтрация по нескольким строкам"""
print(products[(products['CategoryName'] == 'Beverages') & (products['UnitPrice'] > 20)])  # And = &, OR= |
