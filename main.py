# coding=utf-8

import arcpy
file_path = r'H:\Python\Projects\Lectures\Data\2000年草地FVC.tif'
ras = arcpy.Raster(file_path)
arr = arcpy.RasterToNumPyArray()




import numpy as np
#p05 = np.percentile(self.value_list, percent)
