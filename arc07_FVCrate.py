# coding=utf-8

import arcpy
import arcpy


# 环境设置参数
arcpy.env.workspace = r'H:\ArcGIS\Data\FVC'  # 设置本代码的工作文件
arcpy.env.overwriteOutput = True                                         # 设置输出文件存在时，是否覆盖

# 数据准备
data_path = r'H:\ArcGIS\Data\FVC'          # 数据文件夹地址
data_files = ['FVC2000.tif','FVC2020.tif']         # 两年的数据文件名称
output_file = r'FVCrate.tif'       # 输出的数据文件名称

FVC2000 = arcpy.Raster(data_path + '\\' + data_files[0])
FVC2020 = arcpy.Raster(data_path + '\\' + data_files[1])


FVCrate  = (FVC2020 - FVC2000) / FVC2000
FVCrate.save(data_path + '\\' + output_file)

print('Done')


