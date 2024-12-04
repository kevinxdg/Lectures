import arcpy
from arcpy.sa import *

# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

maskfile = r'C:\Users\ccc\Desktop\test\jc.shp'

for day in range(1,11):
        sname = r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-%02d.tif' % day
        ras = ExtractByMask(sname, maskfile)
        savename = r'C:\Users\ccc\Desktop\逐日平均温度\E1981-02-%02d.tif' % day


        Ras = arcpy.Raster(savename)
        ras_10 = Ras - 10
        ras_at = Con(savename,ras_10,0,'value >= 10')

        savename10 = r'C:\Users\ccc\Desktop\逐日平均温度\A1981-02-%02d.tif' % day






