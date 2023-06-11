import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
# print(orders.count())  # Вывести количество строк во всех столбцах
# print(orders['OrderDate'].count())  # Количество строк по определенному столбку
# print(orders['OrderDate'].nunique())  # Количество уникальных строк в столбце
# print(orders['OrderDate'].unique())  # выведет все уникальные строки в столбце
# min() # минимальное значение
# max() # максимальное значение
# mean() # среднее значение
# median() #Медиана
# print(orders['OrderDate'].agg(['min', 'max', 'mean', 'median']))  # Сразу вывести несколько агрегирующих функций
# print(orders.agg({'OrderDate': 'count', 'Freight': 'max'}))  # По нескольким столбцам
# print(orders.agg({'OrderDate': 'count', 'Freight': ['max', 'min', 'mean']})) # у одного столбца сразу несколько аггегируемых функций

# print(products[products['CategoryName'] == 'Beverages'].ProductID.count())
# print(products[products['CategoryName'] == 'Beverages'].UnitPrice.min())

print(orders[orders['OrderDate'].between('1996-01-01', '1996-12-31')].Freight.sum())

