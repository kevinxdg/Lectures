#coding=utf-8

import arcpy
import arcpy    # version 2.8
import os

# 环境设置参数
os.chdir(r'D:\Workspace\Data\HBProject\Landuse')

arcpy.env.workspace = r'D:\Workspace\Data\HBProject\Workfiles\HBProject.gdb'  # 设置本代码的工作文件
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True
#arcpy.env.extent = "MAXOF"

# 数据准备
lu2000_file = r'HBLanduse2000.tif'
lu2020_file = r'HBLanduse2020.tif'
luTrans_file = r'Landuse_trans'

lu2000 = arcpy.Raster(lu2000_file)
lu2020 = arcpy.Raster(lu2020_file)

luTransition = lu2000 * 10 + lu2020
luTransition.save(luTrans_file)

print('Done')