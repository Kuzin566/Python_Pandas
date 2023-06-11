import pandas as pd

# object - текст или символьный тип данных, также часто называют строкой;
# int64 - целое число;
# float64 - число с плавающей точкой;
# datetime64 - дата и время;
# bool - True False;
# category - текст (ведет себя как число при сортировке). Мы познакомимся с этим типом данных позднее.

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

"""Смена типа данных столбов
можно просто сразу прочитать файл и указать нужные столбцы и как их запарсить 
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';', parse_dates=['OrderDate', 'RequiredDate', 'ShippedDate'])
ИЛИ как ниже"""

print(orders.dtypes)  # вывести тип данных столбцов
print(orders.head())
orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
orders['RequiredDate'] = orders['RequiredDate'].astype('datetime64[ns]')
orders['ShippedDate'] = orders['ShippedDate'].astype('datetime64[ns]')
orders['OrderID'] = orders['OrderID'].astype('object')
orders['Delivery_time'] = orders['ShippedDate'] - orders['OrderDate']
"""В pandas пропуски указаны как NaT для типа данных datetime64 и NaN для прочих типов данных.
Метод .isna() возвращает True при наличие пропуска и False в остальных случаях.
Применим метод .isna() к столбцу df_o['ShippedDate'] и запишем в новый столбец df_o['ShippedDate_flag'].
df_o['ShippedDate_flag']=df_o['ShippedDate'].isna()"""
orders['ShippedDate_flag'] = orders['ShippedDate'].isna()
print(orders.head())


