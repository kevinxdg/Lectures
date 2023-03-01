# coding=utf-8
    #以下FVC条件赋值

import arcpy
from arcpy import env
from arcpy.sa import *

env.workspace = "D:/data/HBdata/FVC变化率"
inRaster = Raster("00_20.tif")

if 0.2 >= inRaster >=0:
    print(1)
elif 0.6 >= inRaster >=0.4:
    print(2)
elif 0.8 >= inRaster >=0.6:
    print(3)
elif 1.0 >= inRaster >=0.8:
    print(4)

arcpy.CheckOutExtension("Spatial")

outCon = Con(inRaster)
outCon.save("D:/data/HBdata/FVC条件/FVC1")

