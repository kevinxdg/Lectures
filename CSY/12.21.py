import arcpy
from arcpy.sa import *
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

#分区统计
province_file = r'C:\Users\ccc\Desktop\test\jcc.tif'
#for i in range(1,11):
#    filename = r'C:\Users\ccc\Desktop\逐日平均温度\R1981-02-%02d.tif' % i
#     ras = ZonalStatistics(province_file, "value", filename, "MEAN")
#     outputname = r'C:\Users\ccc\Desktop\12.2\Z1981-02-%02d.tif' % i
#     ras.save(outputname)
#     print('当前处理文件:' + outputname)#提示处理进度

#
for i in range (1,11):
     filename = r'C:\Users\ccc\Desktop\逐日平均温度\R1981-02-%02d.tif' % i
     outputname = r'C:\Users\ccc\Desktop\逐日平均温度\T1981-02-%02d.dbf' % i
     ras = ZonalStatisticsAsTable(province_file, "value", filename, outputname)

     print('当前处理文件:' + outputname)
