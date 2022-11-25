# coding=utf-8

import arcpy
import arcpy    # version 2.8
import os


# 环境设置参数
os.chdir(r'D:\Workspace\Data\HBProject\FVC')

arcpy.env.workspace = r'D:\Workspace\Data\HBProject\Workfiles\HBProject.gdb'  # 设置本代码的工作文件
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True
#arcpy.env.extent = "MAXOF"


# 数据准备
FVC2000 = arcpy.Raster('FVC2000.tif')
FVC2020 = arcpy.Raster('FVC2020.tif')
FVCrate_file = 'FVC_Rate'
posFVCrate_file = r'pos_FVC_Rate'
negFVCrate_file = r'neg_FVC_Rate'

# 计算 FVC 变化率
FVCRate = (FVC2020 - FVC2000) / FVC2000
FVCRate.save(FVCrate_file)
print(FVCrate_file + ' saved.')

# 提取 FVC 变化率正值像素
posFVCRate = arcpy.ia.Con(FVCRate,1,0,"VALUE > 0")
posFVCRate.save(posFVCrate_file)
print(posFVCrate_file + ' saved.')

# 提取 FVC 变化率负值像素
negFVCRate = arcpy.ia.Con(FVCRate,1,0, "VALUE <= 0")
negFVCRate.save(negFVCrate_file)
print(negFVCrate_file + ' saved.')


print('Done')
