# coding=utf-8

import arcpy
import arcpy
import numpy as np
import openpyxl as xl
import glob
import pandas as pd

# 数据准备
ras_path = r'D:\data\gisdata\HBlu\HBlureclass'    # land use 数据保存地址
ras_files = glob.glob1(ras_path,'*.tif')  # 获得指定地址下所有扩展名为 .tif 的文件名
ras_paths = [ras_path+'\\'+f for f in ras_files]   # 利用所获得的 tif 文件名组成全路径
print(ras_paths)
exl_path = r'D:\data\HBdata\testexcel'


# 一级土地利用类型编号
class_id = [1, 2, 3, 4, 5, 6]

wb = xl.Workbook()                  # 新建 excel 文件
for f in ras_paths:          # 由循环将所有 tif 文件读入，并进行统计
                             # 参考已经讲过的，统计栅格图像特征的代码
    ras = arcpy.Raster(f)
    arr = arcpy.RasterToNumPyArray(ras)  # 转为二维矩阵

    lst = [i for item in arr for i in item]    # 将二维矩阵转成一维列表

    vmin = 0
    vmax = 7    #根据所需要范围调整
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):      # 只保留 0~7之间的数值，去掉其它异常值
            tmplst.append(value)

# 以下统计转移矩阵

    msize = len(class_id)   # 根据分类标识确定转移矩阵大小

    mat_luc = np.zeros((msize, msize))    # 生成 msize * msize 的0值矩阵

    sheet = wb.create_sheet()
    for j in range(msize):
        for k in range(msize):
            mat_luc[j][k] = tmplst.count(class_id[j])
        row = mat_luc[j].tolist()
        sheet.append(row)

    print(mat_luc)

wb.save(exl_path + '\\lucc.xlsx')   # 保存excel 文件

print('Done')