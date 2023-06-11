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
orders['RequiredDate'] = orders['RequiredDate'].astype('datetime64[ns]')

"""Присоедините к датафрейму с сотрудниками df_e датафрейм df_sex.
 Далее в разрезе пола посчитайте количество оформленных заказов. 
 На сколько представители одного пола оформили больше заказов, чем представители другого пола? """
new_df = pd.DataFrame({'TitleOfCourtesy': ['Ms.', 'Dr.', 'Mrs.', 'Mr.'], 'Sex': ['female', 'male', 'female', 'male']})
employees_1 = new_df.merge(employees)
employees_1 = employees_1.merge(orders)
employees_1 = employees_1.groupby('Sex').OrderID.count().reset_index()
print(employees_1)
order_male = employees_1['OrderID'][employees_1.Sex == 'male']
order_female = employees_1['OrderID'][employees_1.Sex == 'female']
order_difference = abs(int(order_male) - int(order_female))
print(order_difference)
