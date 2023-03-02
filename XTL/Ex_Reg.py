# coding=utf-8
import numpy as np
import pandas as pd
import openpyxl as xl
import os
import statsmodels.api as sm
import statsmodels.tsa.stattools as stools



#data_file_e = r'D:\code\Projects\Test\Lectures\XTL\Energy.xlsx'
data_path_e = os.getcwd() + '\\..\\Data\\Energy.xlsx'

#data_path_e =data_file_e
# 直接保存 dataframe

# 读取 excel
df = pd.read_excel(data_path_e)
print(df)
x = df.iloc[:,2:3]
y = df.iloc[:,1:2]

print(x)
print(y)
X = sm.add_constant(x)
model = sm.OLS(y,X)
result_ols = model.fit()
print(result_ols.summary())
#print(df.iloc[:,3:5])   # 取其中指定列
#print(df.loc[:,'陕西'])




