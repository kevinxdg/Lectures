import arcpy
import arcpy
from arcpy.ia import *

#ras1 = arcpy.Raster(r'F:\ArcGIS\Data\Test\逐日平均温度\1981-02-01.tif')
#ras2 = arcpy.Raster(r'F:\ArcGIS\Data\Test\逐日平均温度\1981-02-02.tif')
#ras3 = arcpy.Raster(r'F:\ArcGIS\Data\Test\逐日平均温度\1981-02-03.tif')

result = Con(r'F:\ArcGIS\Data\Test\逐日平均温度\1981-02-10.tif', r'F:\ArcGIS\Data\Test\逐日平均温度\1981-02-10.tif', 0, 'value >= 10')

for i in range(1,10):
    filename = r'F:\ArcGIS\Data\Test\逐日平均温度\1981-02-%02d.tif' % i
    ras= Con(filename, filename, 0, 'value >= 10')
    result = result + ras

result.save(r'F:\ArcGIS\Data\Test\逐日平均温度\sum10.tif')





