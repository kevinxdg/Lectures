import arcpy
from arcpy.sa import *
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖
#重采样

#for i in range(1,11):
 #    filename = r'C:\Users\ccc\Desktop\逐日平均温度\E1981-02-%02d.tif' % i
  #   outputname = r'C:\Users\ccc\Desktop\逐日平均温度\R1981-02-%02d.tif' % i
     #参数解释1.元数据2.导出数据3.xy尺寸大小4.采样方法
   #  arcpy.Resample_management(filename, outputname, "1000 1000", "Nearest")
    # print('当前处理文件' + filename)#提示处理进度

#分区统计
province_file = r'C:\Users\ccc\Desktop\test\jcc.tif'
for i in range(1,11):
     filename = r'C:\Users\ccc\Desktop\逐日平均温度\R1981-02-%02d.tif' % i
     ras = ZonalStatistics(province_file, "value", filename, "MEAN")
     outputname = r'C:\Users\ccc\Desktop\test\ZZ1981-02-%02d.tif' % i
     ras.save(outputname)
     print('当前处理文件:' + outputname)#提示处理进度