import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

order_details['Discount_fact'] = order_details['UnitPrice'] * order_details['Quantity'] * order_details['Discount']
order_details['Revenue'] = order_details['UnitPrice'] * order_details['Quantity'] - order_details['Discount_fact']

orders['OrderDate'] = orders['OrderDate'].astype('datetime64[ns]')
orders['ShippedDate'] = orders['ShippedDate'].astype('datetime64[ns]')
orders['RequiredDate'] = orders['RequiredDate'].astype('datetime64[ns]')
orders['year'] = orders['OrderDate'].dt.year
orders['month'] = orders['OrderDate'].dt.month
orders['week'] = orders['OrderDate'].dt.isocalendar().week

db_od_final = order_details.groupby('OrderID').Revenue.sum().reset_index()
db_o = orders.merge(db_od_final)
# # db_o = db_o.groupby('year').Revenue.sum().plot()
# db_o_1 = db_o.groupby('year').Revenue.sum().plot(kind='bar')
# plt.show()
# db_o_2 = db_o.groupby(['year', 'month']).Revenue.sum().plot(kind='bar')
# plt.show()
# db_o_1997 = db_o[db_o['year'] == 1997].groupby('month').Revenue.sum().reset_index()
# db_o_1997 = db_o_1997.rename(columns={'Revenue': 'rev_1997'})
#
# db_o_1998 = db_o[db_o['year'] == 1998].groupby('month').Revenue.sum().reset_index()
# db_o_1998 = db_o_1998.rename(columns={'Revenue': 'rev_1998'})
#
# db_o_final = db_o_1997.merge(db_o_1998, how='left')
# db_o_final.plot(kind='bar')
# plt.show()

"""df_o = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Orders.csv', sep = ';')
df_od = pd.read_csv('C:/Users/User/Desktop/Данные для pandas/Order_details.csv', sep = ';')
Посчитайте отдельно по 1997 и по 1998 году чистую выручку в разрезе недель. 
Запишите результаты в новые датафреймы. Далее объедините их в общий датафрейм, в котором будет 3 столбца: номер недели, 
чистая выручка 1997 год, чистая выручка 1998 год. 
Постройте столбчатую диаграмму и выберите номера недель, на которых выручка в 1997 году была выше чем в 1998.
Примечание: Объедините датафреймы с помощью типа соединения inner, чтобы в итоговый датафрейм попали только недели, 
по которым есть заказы и в 1997 и в 1998 году."""
db_o_1997 = db_o[db_o['year'] == 1997].groupby('week').Revenue.sum().reset_index()
db_o_1997 = db_o_1997.rename(columns={'Revenue': 'rev_1997'})

db_o_1998 = db_o[db_o['year'] == 1998].groupby('week').Revenue.sum().reset_index()
db_o_1998 = db_o_1998.rename(columns={'Revenue': 'rev_1998'})

db_o_final = db_o_1997.merge(db_o_1998, how='inner')
db_o_final.plot(kind='bar', x='week')
plt.show()

