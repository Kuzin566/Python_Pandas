import pandas as pd

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

# print(orders['Freight'].reset_index())  #Вывод столбца
# print(orders.Freight) #Вывод столбца
# print(orders.Freight.reset_index)  # Вывести date frame
# print(orders.Freight.to_frame())  # Вывести date frame
# print(orders.head())  #выведет верхушку таблицы, по умолчанию 5
# print(orders.tail())  #выведет последние 5 строк, по умолчанию 5
# print(orders[["OrderID", "CustomerID"]])  # Вывести несколько столбцов
# print(orders.columns)  # Вывести колонки
print(orders.drop(columns=['ShippedDate', 'Freight']))  # Вывести все столбцы за исключением указаных


order_details['Discount_fact'] = order_details['UnitPrice'] * order_details['Quantity'] * order_details['Discount']
order_details['Revenue'] = order_details['UnitPrice'] * order_details['Quantity'] - order_details['Discount_fact']
print(order_details) # Добавить новый столбец в таблицу используя выражение от других столбцов