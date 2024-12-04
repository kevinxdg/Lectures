import arcpy
import arcpy
ras = arcpy.Raster(r'C:\Users\ccc\Desktop\test\长江1980lucc.tif')
ras_10 = ras * 10
ras_10.save(r'C:\Users\ccc\Desktop\test\长江1980lucc_10_python.tif')

import arcpy
