# coding=utf-8
import numpy as np
import pandas as pd
import openpyxl as xl
import os
data_dir = os.getcwd() + '\\..\\Data\\'
data_file_a = r'a.xlsx'
data_file_b = r'b.xlsx'
data_file_e = r'example.xlsx'
data_path_a = data_dir + data_file_a
data_path_b = data_dir + data_file_b
data_path_e = data_dir + data_file_e
# 直接保存 dataframe
data = pd.DataFrame(data=[[1,2,3],[4,5,6]])
data.to_excel(data_path_a)


# 读取 excel
df = pd.read_excel(data_path_e)
print(df)
print(df.iloc[:,3:5])   # 取其中指定列
print(df.loc[:,'陕西'])


# 操作 Excel
# 新建 workbook
book_b = xl.Workbook()
book_b.create_sheet('Lecture')
book_b.save(data_path_b)
book_b.close()

# 读取 excel表格

book_e = xl.load_workbook(data_path_e)
sheet = book_e.worksheets[0]
values = sheet['A1':'C28']
df = pd.DataFrame(values)
#print(df)

book_e.close()











