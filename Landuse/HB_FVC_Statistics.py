#coding=utf-8

import arcpy
import arcpy    # version 2.8
import numpy as np
import pandas as pd
import openpyxl as xl
import os

# 环境设置参数
os.chdir(r'D:\Workspace\Data\HBProject\Workfiles\HBProject.gdb')

arcpy.env.workspace = r'D:\Workspace\Data\HBProject\Workfiles\HBProject.gdb'  # 设置本代码的工作文件
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True
#arcpy.env.extent = "MAXOF"

# 数据准备
posFVCrate_file = 'pos_FVC_Rate'
negFVCrate_file = 'neg_FVC_Rate'

luTrans_file = r'Landuse_trans'   # 土地利用转移数据
excel_file = r'D:\Workspace\Data\HBProject\Statistics\FVC\FVC_trans.xlsx'


# 定义统计图像数据信息的函数
def RasterToList(inRaster, vmin, vmax):     # 定义函数，将图像数据转为一维列表，并筛选值范围
    arr = arcpy.RasterToNumPyArray(inRaster)  # 转为二维矩阵
    lst = [i for item in arr for i in item]    # 将二维矩阵转成一维列表
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):      # 只保留 vmin~vmax之间的数值，去掉其它异常值
            tmplst.append(value)
    return tmplst                               # 返回列表结果

def FVC_stastics(inlist):           # 定义函数统计转移矩阵生成的list中各类fvc像素个数
    fvc_mat = np.zeros((6,6))       # 先生成0值矩阵，后面以转移矩阵形式保存结果s
    for i in range(1,7):            # 按土地利用类型编号1~6循环
        for j in range(1,7):
            id = i * 10 + j         # 土地利用转移的合成编号
            fvc_mat[i-1][j-1] = inlist.count(id)
    return fvc_mat                # 返回矩阵结果

def save_matrix_to_excel(xlbook,sheetname, mat):      # 定义函数，将矩阵mat 存入excel文件xlbook中
    sheet = xlbook.create_sheet(sheetname)
    for row in mat:
        sheet.append(row.tolist())

# 以下调用函数
# 统计正值矩阵
lutrans_ras = arcpy.Raster(luTrans_file)              # 导入土地利用转移数据
posFVC_ras = arcpy.Raster(posFVCrate_file)            # 导入
pos_stat_ras = lutrans_ras * posFVC_ras               # 保留正FVC变化率的土地利用值
posFVC_list = RasterToList(pos_stat_ras, 0, 70)       # 保留的土地利用值矩阵转成列表
posFVC_mat = FVC_stastics(posFVC_list)                # 统计正值矩阵
pos_dataframe = pd.DataFrame(data=posFVC_mat, \
                             columns=['耕地','林地','草地','水域','建设用地','未利用地'],\
                             index=['耕地','林地','草地','水域','建设用地','未利用地'])

print(pos_dataframe)

# 统计负值矩阵
negFVC_ras = arcpy.Raster(negFVCrate_file)
neg_stat_ras = lutrans_ras * negFVC_ras
negFVC_list = RasterToList(neg_stat_ras, 0, 70)
negFVC_mat = FVC_stastics(negFVC_list)
neg_dataframe = pd.DataFrame(data=posFVC_mat, \
                             columns=['耕地','林地','草地','水域','建设用地','未利用地'],\
                             index=['耕地','林地','草地','水域','建设用地','未利用地'])
print(neg_dataframe)

pos_perc = np.divide(posFVC_mat , posFVC_mat.sum())
pos_percent_dataframe = pd.DataFrame(data= pos_perc, \
                                     columns=['耕地', '林地', '草地', '水域', '建设用地', '未利用地'], \
                                     index=['耕地', '林地', '草地', '水域', '建设用地', '未利用地'])

print(pos_percent_dataframe)

neg_perc = np.divide(negFVC_mat , negFVC_mat.sum())
neg_percent_dataframe = pd.DataFrame(data= neg_perc , \
                                     columns=['耕地', '林地', '草地', '水域', '建设用地', '未利用地'], \
                                     index=['耕地', '林地', '草地', '水域', '建设用地', '未利用地'])
print(neg_percent_dataframe)


if not os.path.exists(excel_file):
    wb = xl.Workbook()                  # 新建 excel 文件
    wb.save(excel_file)
writer = pd.ExcelWriter(excel_file)
pos_dataframe.to_excel(writer,sheet_name='正值')
neg_dataframe.to_excel(writer,sheet_name='负值')
pos_percent_dataframe.to_excel(writer, sheet_name='正值百分比')
neg_percent_dataframe.to_excel(writer, sheet_name='负值百分比')

writer.save()

print('Done')






