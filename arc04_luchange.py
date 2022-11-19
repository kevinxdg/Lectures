# coding=utf-8

import arcpy
import arcpy
import numpy as np
import openpyxl as xl


# 数据准备
file_path = r'F:\ArcGIS\Data\LanduseReclass'
out_path = r'F:\ArcGIS\Data\LanduseChange'
exl_path = r'F:\ArcGIS\Data'
all_files = ['湖北1980lucc.tif','湖北1990lucc.tif','湖北1995lucc.tif', \
             '湖北2000lucc.tif','湖北2005lucc.tif','湖北2010lucc.tif', \
             '湖北2015lucc.tif','湖北2020lucc.tif']

first = all_files[:-1]            # 以全列表中的前面7个为每个时期开始
print(first)
last = all_files[1:]              # 以全列表中的后面7个为每个时期结束

# 一级土地利用类型编号
class_id = [1, 2, 3, 4, 5, 6]
# 二级土地利用类型编号
#class_id = [11, 12, 21, 22, 23, 24, 31, 32, 41, 42, 43, 44, 45, 46, 51, 52, 53, 61, 62, 63, 64, 65, 66 ]
mfacotr = 10    # 转移时初期类型编号扩大的倍数

wb = xl.Workbook()                  # 新建 excel 文件

for i in range(len(first)):
    ras1 = arcpy.Raster(file_path + '\\' + first[i])

    ras2 = arcpy.Raster(file_path + '\\' + last[i])
    ras = ras1 * mfacotr + ras2
    #ras.save(out_path + '\\' + str(i) + '.tif')  # 保存转移矩阵的土地利用数据

    arr = arcpy.RasterToNumPyArray(ras)  # 转为二维矩阵

    lst = [i for item in arr for i in item]    # 将二维矩阵转成一维列表

    vmin = 0
    vmax = np.max(class_id) * (mfacotr + 1)    # 确定转移矩阵中编号的最大值范围
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):      # 只保留 最小最大值之间的数值，去掉其它异常值
            tmplst.append(value)

    # 以下统计转移矩阵

    msize = len(class_id)   # 根据分类标识确定转移矩阵大小

    mat_luc = np.zeros((msize, msize))    # 生成 msize * msize 的0值矩阵

    sheet = wb.create_sheet(title=str(i))
    for j in range(msize):
        for k in range(msize):
            mat_luc[j][k] = tmplst.count(class_id[j]*mfacotr + class_id[k])
        row = mat_luc[j].tolist()
        sheet.append(row)

    print(mat_luc)

wb.save(exl_path + '\\lucc.xlsx')   # 保存excel 文件

print('Done')













