import arcpy
import arcpy
import numpy

#filename = r'F:\ArcGIS\Data\Test\YZRTemp\E1981-02-01.tif'
#ras = arcpy.Raster(filename)
#aver = arcpy.GetRasterProperties_management(ras,"MAXIMUM")
#print(aver.getOutput(0))


data = []
for i in range(1,11):
    filename = r'F:\ArcGIS\Data\Test\YZRTemp\E1981-02-%02d.tif' % i
    ras = arcpy.Raster(filename)
    aver = arcpy.GetRasterProperties_management(ras,"MINIMUM")
    data.append(float(aver.getOutput(0)))

print(data)
print(numpy.max(data))
