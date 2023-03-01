#coding=utf-8
import os
import arcpy
import arcpy
import glob
import numpy as np
import openpyxl as xl

# 环境设置参数
data_dir = 'D:\\data\\FVC\\FVC_annual\\'
out_dir = 'D:\\data\\FVC\\FVC_Level\\'
out_path = 'D:\\data\\FVC\\FVC_change\\'
exl_path = 'D:\\data\\FVC\\testexcel\\'
os.chdir(data_dir) # 改变当前文件到数据目录

# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

# FVC分级后编号
class_id = [10, 20, 30, 40, 50]

wb = xl.Workbook()                  # 新建 excel 文件

#新的转移矩阵（1982-2021年）

for i in range(1983,2021):
    cfile = glob.glob1(out_dir,'*'+ str(i) + '*.tif')
    print(cfile)
    pfile = glob.glob1(out_dir,'*'+ str(i - 1) + '*.tif')
    cFVC = arcpy.Raster(out_dir + cfile[0])
    pFVC = arcpy.Raster(out_dir + pfile[0])
    tFVC = pFVC * 100 + cFVC
    tFVC.save(out_path + '\\' + str(i) + '.tif')  # 保存转移矩阵的土地利用数据
    arr = arcpy.RasterToNumPyArray(tFVC)  # 转为二维矩阵

    lst = [i for item in arr for i in item]    # 将二维矩阵转成一维列表

    vmin =0
    vmax = np.max(class_id) * (100 + 1)    # 确定转移矩阵中编号的最大值范围
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
            mat_luc[j][k] = tmplst.count(class_id[j]*100 + class_id[k])
        row = mat_luc[j].tolist()
        sheet.append(row)

    print(mat_luc)

wb.save(exl_path + '\\FVC.xlsx')   # 保存excel 文件

print('Done')