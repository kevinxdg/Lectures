# coding=utf-8

import arcpy
import arcpy
import numpy as np
import pandas as pd
import glob

# 数据准备
file_path = r'F:\ArcGIS\Data\Landuse'                     # 要重分类的数据文件的保存地址
file_output = r'F:\ArcGIS\Data\LanduseReclass'    # 分类完成后数据文件的保存地址

files = glob.glob1(file_path, '*.tif')                    # 获取扩展名为 .tif 的数据文件名称

# 根据Arcpy的定义，定义类别转换映射
revalue = arcpy.sa.RemapValue([[11,1],[12,1],[21,2],[22,2],[23,2],[24,2],[31,3],[32,3], [33,3],\
                               [41,4], [42,4], [43,4], [44, 4], [45, 4], [46, 4],\
                               [51, 5],[52,5], [53,5],[61,6], [62,6], [63, 6], [64, 6], [65, 6], [66,6]])

for f in files:
    in_file = file_path + '\\' + f                          # 组成每一个文件的全路径
    ras = arcpy.sa.Reclassify(in_file, 'Value', revalue)    # 对数据文件进行重分类，重分类定义在空间分析sa模块，参考工具帮助
                                                            # Reclassify (in_raster, reclass_field, remap, {missing_values})
    out_file = file_output + '\\' + f                       # 组成输出文件的全路径
    ras.save(out_file)

print('Done')
