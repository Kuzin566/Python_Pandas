import pandas as pd


df_p = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
df_o = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
df_od = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
df_c = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
df_e = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx", sheet_name='Лист3')
print(df_p)
