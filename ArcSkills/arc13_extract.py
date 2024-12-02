import arcpy
import arcpy
from arcpy.sa import *  # 从 Spatial Analysis Tools 工具箱导入
from arcpy.ia import *


# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

maskfile = r'F:\ArcGIS\Data\Test\长江经济带\YZRange.shp'

for day in range(1,11):
    sname = r'F:\ArcGIS\Data\Test\逐日平均温度\1981-02-%02d.tif' % day
    ras = ExtractByMask(sname, maskfile)
    savename = r'F:\ArcGIS\Data\Test\YZRTemp\E1981-02-%02d.tif' % day
    ras.save(savename)
    ras_10 = ras - 10
    ras_at = Con(savename,ras_10,0,'value >= 10')
    savename10 = r'F:\ArcGIS\Data\Test\YZRTemp\A1981-02-%02d.tif' % day
    ras_at.save(savename10)
