# coding=utf-8

import arcpy
import arcpy
import numpy as np
import pandas as pd

# 数据准备
file_path = r'F:\ArcGIS\Data\Landuse'
first = ['湖北1980lucc.tif']
last = ['湖北1990lucc.tif']

for i in range(len(first)):
    ras1 = arcpy.Raster(file_path + '\\' + first[i])
    ras2 = arcpy.Raster(file_path + '\\' + last[i])
    ras = ras1 * 100 + ras2
    ras.save('F:\\ArcGIS\\Data\\a' + str(i) + '.tif' )  # 保存转移矩阵的土地利用数据

    arr = arcpy.RasterToNumPyArray(ras)  # 转为二维矩阵

    lst = [i for item in arr for i in item]    # 将二维矩阵转成一维列表

    vmin = 0
    vmax = 70
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):      # 只保留 0~70之间的数值，去掉其它异常值
            tmplst.append(value)

    # 以下统计转移矩阵
    mat_luc = np.zeros((6,6))
    print(mat_luc)

    for i in range(6):
        for j in range(6):
            mat_luc[i][j] = tmplst.count((i+1)*10+j+1)

    print(mat_luc)











