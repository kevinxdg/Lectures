# coding=utf-8

import arcpy
import arcpy
import numpy as np
import glob

file_path = r'F:\ArcGIS\Data\Landuse'

first = ['湖北1980lucc.tif','湖北1990lucc.tif','湖北1995lucc.tif']
last = ['湖北1990lucc.tif','湖北1995lucc.tif','湖北2000lucc.tif']

for i in range(3):
    ras1 = arcpy.Raster(file_path + '\\' + first[i])
    ras2 = arcpy.Raster(file_path + '\\' + last[i])
    ras = ras1 * 100 + ras2
    ras.save('F:\\ArcGIS\\Data\\a' + str(i) + '.tif' )




#arcpy.Mosaic_management()