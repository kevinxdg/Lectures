# coding=utf-8
import numpy as np
import pandas as pd
import openpyxl as xl
import os

import plotly.io
import statsmodels.api as sm
import statsmodels.tsa.stattools as stools
import matplotlib.pyplot as plt


# 分辨率参数-dpi，画布大小参数-figsize
plt.figure(dpi=300,figsize=(24,8))
# 改变文字大小参数-fontsize
plt.xticks(fontsize=10)





data_dir = os.getcwd() + '\\Data\\Energy\\'
data_file_e = r'Result_Biomass_2023_02_17_09_55_08.xlsx'
data_path_e = data_dir + data_file_e

# 读取 excel
df = pd.read_excel(data_path_e)
# print(df)

labels = [' ', '1950', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1960', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1970', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1980', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '1990', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2000', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2010', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2020']

Grain = df.iloc[:,1:2]
Rice = df.iloc[:,2:3]
Wheat = df.iloc[:,3:4]
Corn = df.iloc[:,4:5]
Beans = df.iloc[:,5:6]
Tubers = df.iloc[:,6:7]
Cotton = df.iloc[:,7:8]
Oil = df.iloc[:,8:9]
Peanuts = df.iloc[:,9:10]
Rapeseeds = df.iloc[:,10:11]
Sesame = df.iloc[:,11:12]
Fiber = df.iloc[:,12:13]
Jute = df.iloc[:,13:14]
Sugarcane = df.iloc[:,15:16]
Beetroots = df.iloc[:,17:18]
Tobacco = df.iloc[:,18:19]


data = [Grain, Rice, Wheat, Corn, Beans, Tubers, Cotton, Oil, Peanuts, Rapeseeds, Sesame, Fiber, Jute, Sugarcane, Beetroots, Tobacco]
x = range(len(labels))
width = 0.75
bottom_y = [0] * len(labels)
for y in data:
    plt.bar(x, y, width, bottom=bottom_y)
    bottom_y = [a+b for a, b in zip (y, bottom_y)]
plt.xticks(x, labels)
plt.legend(['Grain', 'Rice', 'Wheat', 'Corn', 'Beans', 'Tubers', 'Cotton', 'Oil', 'Peanuts', 'Rapeseeds', 'Sesame', 'Fiber', 'Jute', 'Sugarcane', 'Beetroots', 'Tobacco'], loc='upper left', ncol = 4)
plt.savefig(r'D:\code\CCG\Lectures\CCG\Data\Energy\biomass.png')
plt.show()






























































