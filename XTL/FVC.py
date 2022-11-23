————————————————-————  ##########################################################—————————————————————————————
FVC条件赋值为0
1
用CON函数
————————————————————  ##########################################################———————————————————————————
# coding=utf-8
# 以下FVC条件赋值

import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "D:/data/HBdata/FVC变化率"

# Set local variables
inRaster = Raster("00_20.tif")
inTrueRaster = 1
inFalseConstant = 0
whereClause = "VALUE > 0"

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

# Execute Con
outCon = Con(inRaster, inTrueRaster, inFalseConstant, whereClause)

# Execute Con using a map algebra expression instead of a where clause
outCon2 = Con(inRaster > 0, inTrueRaster, inFalseConstant)

# Save the outputs
outCon.save("D:/data/HBdata/FVC条件/FVC1")
outCon2.save("D:/data/HBdata/FVC条件/FVC2")





————————————————-————  ##########################################################—————————————————————————————
统计一级分类的转移矩阵，并保存为指定的
excel文件
————————————————————  ##########################################################——————————————————————————————————

# coding=utf-8

import arcpy
import arcpy
import numpy as np
import openpyxl as xl

# 数据准备
file_path = r'D:\data\HBdata\HBlureclass'
out_path = r'D:\data\HBdata\testchange'
exl_path = r'D:\data\HBdata\testexcel'
all_files = ['湖北省1980lucc.tif', '湖北省1990lucc.tif', '湖北省1995lucc.tif', \
             '湖北省2000lucc.tif', '湖北省2005lucc.tif', '湖北省2010lucc.tif', \
             '湖北省2015lucc.tif', '湖北省2020lucc.tif']

first = all_files[:-1]  # 以全列表中的前面7个为每个时期开始
print(first)
last = all_files[1:]  # 以全列表中的后面7个为每个时期结束

# 一级土地利用类型编号
class_id = [1, 2, 3, 4, 5, 6]
# 二级土地利用类型编号
# class_id = [11, 12, 21, 22, 23, 24, 31, 32, 41, 42, 43, 44, 45, 46, 51, 52, 53, 61, 62, 63, 64, 65, 66 ]
mfacotr = 10  # 转移时初期类型编号扩大的倍数

wb = xl.Workbook()  # 新建 excel 文件

for i in range(len(first)):
    ras1 = arcpy.Raster(file_path + '\\' + first[i])
    ras2 = arcpy.Raster(file_path + '\\' + last[i])
    ras = ras1 * mfacotr + ras2
    # ras.save(out_path + '\\' + str(i) + '.tif')  # 保存转移矩阵的土地利用数据

    arr = arcpy.RasterToNumPyArray(ras)  # 转为二维矩阵

    lst = [i for item in arr for i in item]  # 将二维矩阵转成一维列表

    vmin = 0
    vmax = np.max(class_id) * (mfacotr + 1)  # 确定转移矩阵中编号的最大值范围
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):  # 只保留 最小最大值之间的数值，去掉其它异常值
            tmplst.append(value)

    # 以下统计转移矩阵

    msize = len(class_id)  # 根据分类标识确定转移矩阵大小

    mat_luc = np.zeros((msize, msize))  # 生成 msize * msize 的0值矩阵

    sheet = wb.create_sheet(title=str(i))
    for j in range(msize):
        for k in range(msize):
            mat_luc[j][k] = tmplst.count(class_id[j] * mfacotr + class_id[k])
        row = mat_luc[j].tolist()
        sheet.append(row)

    print(mat_luc)

wb.save(exl_path + '\\lucc.xlsx')  # 保存excel 文件

print('Done')







———————————————————  ########################################——————————————————————----————————————————————————————————————
重分类ge（将二级土地利用重分类为一级）
———————————————————  #########################################——————————————————————————————————————————
# coding=utf-8

import arcpy
import arcpy
import numpy as np
import pandas as pd
import glob

# 数据准备
file_path = r'D:\data\CJdata\landuse'  # 要重分类的数据文件的保存地址
file_output = r'D:\data\CJdata\test'  # 分类完成后数据文件的保存地址

files = glob.glob1(file_path, '*.tif')  # 获取扩展名为 .tif 的数据文件名称

# 根据Arcpy的定义，定义类别转换映射
revalue = arcpy.sa.RemapValue([[11, 1], [12, 1], [21, 2], [22, 2], [23, 2], [24, 2], [31, 3], [32, 3], [33, 3], \
                               [41, 4], [42, 4], [43, 4], [44, 4], [45, 4], [46, 4], \
                               [51, 5], [52, 5], [53, 5], [61, 6], [62, 6], [63, 6], [64, 6], [65, 6], [66, 6],
                               [67, 6]])

for f in files:
    in_file = file_path + '\\' + f  # 组成每一个文件的全路径
    ras = arcpy.sa.Reclassify(in_file, 'Value', revalue)  # 对数据文件进行重分类，重分类定义在空间分析sa模块，参考工具帮助
    # Reclassify (in_raster, reclass_field, remap, {missing_values})
    out_file = file_output + '\\' + f  # 组成输出文件的全路径
    ras.save(out_file)

print('Done')





————————————————————  ###################################————————————————————————————————————
重分类cao（将二级土地利用重分类为一级）
————————————————————  ###################################————————————————————————————————————
# coding=utf-8

# 统计土地利用相关的信息
import sys  # reload()之前必须要引入模块

reload(sys)
sys.setdefaultencoding('utf-8')
# coding=utf-8
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

# coding=utf-8

import arcpy
import arcpy
import numpy as np
import glob

# Name: reclassify_example02.py
# Description: Reclassifies the values in a raster.
# Requirements: Spatial Analyst Extension

# Import system modules
import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "D:\\data\\CJdata\\landuse\\"
output_path = "D:\\data\\CJdata\\test_reclass\\"
rasterlist = arcpy.ListRasters("*", "tif")
for raster in rasterlist:
    inRaster = arcpy.Raster(raster)
    out = output_path + str(raster)
    # Set local variables
    reclassField = "value"
    remap = RemapValue(
        [["11", 1], ["12", 1], ["21", 2], ["22", 2], ["23", 2], ["24", 2], ["31", 3], ["32", 3], ["33", 3],
         ["41", 4], ["42", 4], ["43", 4], ["44", 4], ["45", 4], ["46", 4], ["51", 5], ["52", 5], ["53", 5],
         ["61", 6], ["62", 6], ["63", 6], ["64", 6], ["65", 6], ["66", 6], ["67", 6], ])

    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Execute Reclassify
    outReclassify = Reclassify(inRaster, reclassField, remap, "NODATA")

    # Save the output
    outReclassify.save(out)






————————————————————  ####################################################————————————————————————————————————-————————————————————————————————
批量镶嵌，将几个图层tif格式栅格图像镶嵌成一个
————————————————————  ######################################################——————————————————————————————————————-——————————————————————
# coding=utf-8

import sys, os
import arcpy
from arcpy import *
import glob

# 2. --------------------------------------批量镶嵌--------------------------------------
input_path = r'D:\arcgis\data\2000FVC'
output_path = r'D:\arcgis\data\output'

# 1）创建文件夹
if os.path.exists(output_path) == False:
    os.mkdir(output_path)

# 2）设定工作空间
arcpy.env.workspace = input_path

# 3）得到所有tif格式影像
rasterlist = arcpy.ListRasters("*", "tif")
# rasters = glob.glob(os.path.join(input_path, "*.tif"))
raster_modi = ''
for raster in rasterlist:
    raster_add = raster + ';'
    raster_modi += raster_add
raster_modi = raster_modi.rstrip(';')
raster_result = """ "%s" """ % (raster_modi)
print (raster_result)

# 4）批量镶嵌
# 4.1 定义输出的栅格名字
name_out = "2000年.tif"
# 4.2 定义镶嵌后的投影
Coordinate_System = "PROJCS['WGS_1984_UTM_Zone_50N',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',500000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',117.0],PARAMETER['Scale_Factor',0.9996],PARAMETER['Latitude_Of_Origin',0.0],UNIT['Meter',1.0]]"
# 4.3 定义波段数（这是必须的）
band_num = "1"  # 一般都是1
# 4.4 使用镶嵌工具
arcpy.MosaicToNewRaster_management(raster_result, output_path, name_out, Coordinate_System, number_of_bands=band_num)



————————————————————————————————————————————————————————————————————————————————————————————————————-
镶嵌2
——————————————————————————————————————————————————————————————————————————-

# coding=utf-8
import sys  # reload()之前必须要引入模块

reload(sys)
sys.setdefaultencoding('utf-8')
# coding=utf-8

# coding:utf-8
import arcpy
import shutil, os

# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-

import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "D:\\data\\2020FVC\\"
# 裁剪后文件输出的文件夹
outputpath = "D:\\data\\FVC\\"

# Set local variables
rasters = arcpy.ListRasters("*", "tif")

mosaic_rasters = ""
for raster in rasters:
    mosaic_rasters = mosaic_rasters + raster + ";"
print(mosaic_rasters)

arcpy.CheckOutExtension("Spatial")
arcpy.MosaicToNewRaster_management(mosaic_rasters, outputpath, "2020FVC.tif", "", "32_BIT_FLOAT", "", "1", "", "")

print('finish')









—————————————————————————  ##################################################____________________________________________________________________________________________________________________________________________________________________
绘制箱线图
————————————————————————  ###################################################————————————————————————————————————————————————————————


# coding=utf-8
import arcpy
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

file_path1 = r'D:\arcgis\data\各类FVC\2000年建设用地FVC.tif'
file_path2 = r'D:\arcgis\data\各类FVC\2020年建设用地FVC.tif'

ras1 = arcpy.Raster(file_path1)  # 读取栅格图片
arr1 = arcpy.asterToNumPyArray(ras1)  # 转为二维矩阵
ras2 = arcpy.Raster(file_path2)  # 读取栅格图片
arr2 = arcpy.RasterToNumPyArray(ras2)  # 转为二维矩阵

arr1 = arr1.tolist()  # 一维向量
arr2 = arr2.tolist()  # 一维向量

lst1 = [i for item in arr1 for i in item]
lst2 = [i for item in arr2 for i in item]

vmin = -1
vmax = 1
tmplst1 = []
tmplst2 = []  # tmplst 就是最终用来画图的数据
for value in lst1:
    if (value >= vmin) and (value <= vmax):
        tmplst1.append(value)
for value in lst2:
    if (value >= vmin) and (value <= vmax):
        tmplst2.append(value)

plt.boxplot([tmplst1, tmplst2], patch_artist=True, boxprops={'facecolor': 'k', 'alpha': 0.2})
# patch_artist箱体填充   #boxprops设置箱体属性
plt.xticks([1, 2], [u'2000年', u'2020年'], fontsize=16)  # 设置 x 轴标签及字体
plt.yticks(fontsize=16)  # 设置 y 轴字体大小
plt.ylabel(u"建设用地植被覆盖度", fontsize=20)  # 设置y轴标题
plt.show()





——————————-————————————————  ###########################################_______________________________________________________________________________________________________________________________________________________________
绘制箱线图，并得出分位数（箱线图中文标签可能乱码）
-——————————————————————————  ############################################————————————————————————————————————————————————————
# coding=utf-8
# 统计土地利用相关的信息


import arcpy
import arcpy  # 导入 arcpy 模块用于影像处理
import numpy as np  # 导入 numpy 模块用于后续数据的统计处理
import matplotlib.pyplot as plt  # 导入 matplotlib模块用于绘图

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# file_path = 'W:\\数据\\湖北省植被覆盖度研究\\各类FVC\\'     # 定义数据保存的文件夹地址
file_path = 'H:\\Python\\Data\\'

# 定义所要处理的图像文件
files = ['2000年草地FVC.tif', '2020年草地FVC.tif']  # 草地

# 将所需要的数据从影像文件保存到 data
data = []

for f in files:  # 每次取出 files 列表中的一个元素 （文件名）
    fpath = file_path + f  # 组成带路径的文件名
    ras = arcpy.Raster(fpath)  # 将这个元素对应的影像文件读取到程序变量 ras 中
    arr = arcpy.RasterToNumPyArray(ras)  # 将 ras 变量所表示的影像数据转为二维矩阵
    lst = [i for item in arr for i in item]  # 将二维矩阵 arr 转换成一维向量

    vmin = -1
    vmax = 1
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):
            tmplst.append(value)
    data.append(tmplst)

    # 统计各个图的特征值
    print(f + ':')
    print('最大值 = ', np.max(tmplst))
    print('最小值 = ', np.min(tmplst))
    print('平均值 = ', np.mean(tmplst))
    print('标准差 = ', np.std(tmplst))
    print('变异系数 = ', np.std(tmplst) / np.mean(tmplst))
    print('5% 分位数 = ', np.percentile(tmplst, 5))
    print('25% 分位数 = ', np.percentile(tmplst, 25))
    print('50% 分位数 = ', np.percentile(tmplst, 50))
    print('75% 分位数 = ', np.percentile(tmplst, 75))
    print('95% 分位数 = ', np.percentile(tmplst, 95))
    print('\n')

# 根据 data 所保存的数据进行绘图
plt.boxplot(data, patch_artist=True, boxprops={'facecolor': 'k', 'alpha': 0.2})  # 画分位数的箱线图
plt.xticks([1, 2], ['2000年', '2020年'], fontsize=16)  # 设置 x 轴标签及字体
plt.yticks(fontsize=16)  # 设置 y 轴字体大小
plt.ylabel("草地植被覆盖度", fontsize=20)
plt.show()



——————————————————  ##############################################################————————————————————————————————————————————————————--——————
土地利用转移矩阵（需分类为一级后使用）
——————————————————  ##############################################################————————————————————-——————————————-————————————————


# coding=utf-8

import arcpy
import arcpy
import numpy as np
import glob

file_path = r'D:\Data\长江经济带数据\lucc长江一级分类'

first = ['1980lucc长江.tif', '1990lucc长江.tif', '1995lucc长江.tif', '2000lucc长江.tif', '2005lucc长江.tif', '2010lucc长江.tif',
         '2015lucc长江.tif', '2018lucc长江.tif']
last = ['1990lucc长江.tif', '1995lucc长江.tif', '2000lucc长江.tif', '2005lucc长江.tif', '2010lucc长江.tif', '2015lucc长江.tif',
        '2018lucc长江.tif', '2020lucc长江.tif']
# 表示80-90年土地利用变化，90-95年变化，95-00年变化..........

for i in range(8):
    ras1 = arcpy.Raster(file_path + '\\' + first[i])
    ras2 = arcpy.Raster(file_path + '\\' + last[i])
    ras = ras1 * 10 + ras2
    ras.save('D:\\data\\长江经济带数据\\lucc长江转移矩阵\\a' + str(i) + '.tif')





——————————————  ##################################################################——————————————————————————————————————————
土地利用字符面积统计（统计出土地利用各种类型地的面积）
——————————————  #################################################################——————————————————————————————————————————


# coding=utf-8

# 统计土地利用相关的信息
import sys  # reload()之前必须要引入模块

reload(sys)
sys.setdefaultencoding('utf-8')
# coding=utf-8
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置字体
plt.rcParams["axes.unicode_minus"] = False  # 该语句解决图像中的“-”负号的乱码问题

# coding=utf-8

import arcpy
import arcpy
import numpy as np
import glob
import pandas as pd

ras_path = r'D:\data\test'  # land use 数据保存地址
ras_files = glob.glob1(ras_path, '*.tif')  # 获得指定地址下所有扩展名为 .tif 的文件名
# 不明白的仍然可以自己写
# ras_files = ['landuse2000.tif'] 等，按实际名字列举

ras_paths = [ras_path + '\\' + f for f in ras_files]  # 利用所获得的 tif 文件名组成全路径
print(ras_paths)
for f in ras_paths:  # 由循环将所有 tif 文件读入，并进行统计
    # 参考已经讲过的，统计栅格图像特征的代码
    ras = arcpy.Raster(f)
    arr = arcpy.RasterToNumPyArray(ras)  # 转为二维矩阵

    lst = [i for item in arr for i in item]  # 将二维矩阵转成一维列表

    vmin = 0
    vmax = 70  # 根据所需要范围调整
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):  # 只保留 0~7之间的数值，去掉其它异常值
            tmplst.append(value)

    # 统计在列表中各类值出现的次数 用到了 pandas 程序包
    print(u'土地利用：' + f)
    print(pd.value_counts(tmplst))
