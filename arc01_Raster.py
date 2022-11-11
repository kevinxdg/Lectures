# coding=utf-8

import arcpy
import arcpy
import numpy as np

file_path = r'H:\Python\Data\2000年草地FVC.tif'
print(file_path)


ras = arcpy.Raster(file_path)          # 读取栅格图片
arr = arcpy.RasterToNumPyArray(ras)     # 转为二维矩阵

arr = arr.tolist()   # 一维向量

lst = [i for item in arr for i in item]

vmin = -1
vmax = 1
tmplst = []
for value in lst:
    if (value >= vmin) and (value <= vmax):
        tmplst.append(value)


tmplst.sort()
p05 = np.percentile(tmplst, 25)
print(p05)





