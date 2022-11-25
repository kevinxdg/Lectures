#coding=utf-8

import arcpy
import arcpy    # version 2.8
import numpy as np
import openpyxl as xl

# 环境设置参数
arcpy.env.workspace = r'H:\Python\Projects\Lectures\Landuse'  # 设置本代码的工作文件
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True
#arcpy.env.extent = "MAXOF"

# 数据准备
posFVCrate_file = 'H:\\Data\\GIS\\Hubei\\FVC\\TM\\FVCRate\\posFVCRate.tif'
negFVCrate_file = 'H:\\Data\\GIS\\Hubei\\FVC\\TM\\FVCRate\\negFVCrate.tif'

luTrans_file = r'H:\Data\GIS\Hubei\Landuse\TM\Transition\trans.tif'   # 土地利用转移数据
excel_file = r'H:\Python\Projects\Lectures\Landuse\Results\FVC_trans.xlsx'


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
print(posFVC_mat)


negFVC_ras = arcpy.Raster(negFVCrate_file)

neg_stat_ras = lutrans_ras * negFVC_ras
negFVC_list = RasterToList(neg_stat_ras, 0, 70)
negFVC_mat = FVC_stastics(negFVC_list)                 # 统计负值矩阵
print(negFVC_mat)


wb = xl.Workbook()                  # 新建 excel 文件
save_matrix_to_excel(wb,'正值',posFVC_mat)

pos_mat = np.divide(posFVC_mat , posFVC_mat.sum())
save_matrix_to_excel(wb,'正值百分比', pos_mat)

save_matrix_to_excel(wb,'负值', negFVC_mat)

neg_mat = np.divide(negFVC_mat , negFVC_mat.sum())
save_matrix_to_excel(wb,'负值百分比', neg_mat)

wb.save(excel_file)


print('Done')






