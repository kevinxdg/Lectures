# coding=utf-8

import arcpy
import arcpy
import numpy as np
import glob
import pandas as pd

ras_path = r'H:\ArcGIS\Data\HBLanduse'    # land use 数据保存地址
ras_files = glob.glob1(ras_path,'*.tif')  # 获得指定地址下所有扩展名为 .tif 的文件名
# 不明白的仍然可以自己写
# ras_files = ['landuse2000.tif'] 等，按实际名字列举

ras_paths = [ras_path+'\\'+f for f in ras_files]   # 利用所获得的 tif 文件名组成全路径
print(ras_paths)
for f in ras_paths:          # 由循环将所有 tif 文件读入，并进行统计
                             # 参考已经讲过的，统计栅格图像特征的代码
    ras = arcpy.Raster(f)
    arr = arcpy.RasterToNumPyArray(ras)  # 转为二维矩阵

    lst = [i for item in arr for i in item]    # 将二维矩阵转成一维列表

    vmin = 0
    vmax = 7
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):      # 只保留 0~7之间的数值，去掉其它异常值
            tmplst.append(value)

    #统计在列表中各类值出现的次数 用到了 pandas 程序包
    print('土地利用：' + f)
    linfo = pd.value_counts(tmplst)
    print(linfo)












