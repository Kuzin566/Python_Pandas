import pandas as pd


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 10)
products = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Products.csv", sep=';')
orders = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Orders.csv", sep=';')
order_details = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Order_details.csv", sep=';')
customers = pd.read_csv("D:\\Stepik\\Python_Pandas\\files\\Customers.csv", sep=';')
employees = pd.read_excel("D:\\Stepik\\Python_Pandas\\files\\Employees.xlsx")

# Series.str.contains(pat, case=True, regex=True, na=None, flags=0)
# pat: строка, регулярное выражение или компилированный шаблон, который нужно найти в строках столбца;
# case: булевый параметр, который указывает, должен ли поиск быть регистрозависимым (по умолчанию True);
# regex: булевый параметр, который указывает, является ли pat регулярным выражением (по умолчанию True);
# na: строка, которая будет использоваться для обработки отсутствующих значений (по умолчанию None);
# flags: дополнительные флаги регулярных выражений, которые нужно использовать при поиске.


# print(customers[customers['ContactTitle'].str.contains(pat='Sales', case=False)])  # Выведел все строки где в ContactTitle' есть значение 'Sales'
# print(customers[customers['ContactTitle'].str.lower().str.startswith('sales')])  #В начале строки
print(customers[customers['ContactTitle'].str.endswith('Manager')])  #В начале строки


