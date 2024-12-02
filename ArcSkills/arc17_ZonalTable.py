import arcpy
import arcpy
from arcpy.sa import *

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

province_file = r'F:\ArcGIS\Data\Test\长江经济带\YBZP.tif'

for i in range(1,11):
    filename = r'F:\ArcGIS\Data\Test\TempReSample\R1981-02-%02d.tif' % i
    outputname = r'F:\ArcGIS\Data\Test\Zonal\T1981-02-%02d.dbf' % i
    ras = ZonalStatisticsAsTable(province_file, "value", filename, outputname)
    print('当前处理文件：' + outputname)