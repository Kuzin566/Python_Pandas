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

e = pd.DataFrame({'Title': employees['Title']})      # Образно явно указываем как будет называться столбец у выбранного столбца
c = pd.DataFrame({'Title': customers['ContactTitle']})
print(pd.concat([e, c]))
# print(employees['Title'].to_frame())

# print(customers['ContactTitle'].reset_index())
