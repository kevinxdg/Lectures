# coding=utf-8

import arcpy
import arcpy
import numpy as np
import openpyxl as xl

# 数据准备
data_path = r''
data_files = []
output_file = r''

FVC2000 = arcpy.Raster(r'')
FVC2020 = arcpy.Raster(r'')

FVCrate  = (FVC2020 - FVC2000) / FVC2000
FVCrate.save(output_file)