#coding=utf-8
import arcpy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


G_FVC2003 = arcpy.Raster(r'D:\gisshuju\Changjiang\重叠年份数据03-06年\GIMMS\2003\FVC.A20030.annual.tif')
M_FVC2003 = arcpy.Raster(r'D:\gisshuju\Changjiang\重叠年份数据03-06年\MODIS\2003\FVC.A20030.annual.tif')

sub_FVC = G_FVC2003 - M_FVC2003
arr = arcpy.RasterToNumPyArray(sub_FVC)  # 转为二维矩阵
lst = [i for item in arr for i in item]  # 将二维矩阵 arr 转换成一维向量
vmin = -1
vmax = 1
tmplst = []
for value in lst:
    if(value >= vmin) and (value <= vmax):  # 只保留-1到1之间的数值
        tmplst.append(value)

print(tmplst)

plt.hist(tmplst,bins=100)
plt.show()

