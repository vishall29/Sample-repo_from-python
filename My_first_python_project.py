import pandas as pd
import xlrd
import xlrd.sheet
df=pd.read_excel(r'C:\Users\visha\Downloads\Sample - Superstore.xls')
print(df.head())
df['Price'] = df['Sales'] / df['Quantity']
print(df.head())