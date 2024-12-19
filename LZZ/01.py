
转成表格的代码
import arcpy
import arcpy

from arcpy.sa import *
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True  # 保存时允许覆盖

province_file = r'D:\新建文件夹\FANWEI\YBZP.tif'

for i in range(1, 11):
    filename = r'D:\新建文件夹\12.2\R1981-02-%02d.tif' % i
    outputname = r'D:\新建文件夹\12.2\T1981-02-%02d.dbf' % i
    res = ZonalStatisticsAsTable(province_file, "value", filename, outputname)
    print('当前处理文件: ' + outputname)