import arcpy
import arcpy

ras = arcpy.Raster(r'F:\ArcGIS\Data\Test\长江1980lucc.tif')
ras_int = ras // 10
ras_int.save(r'F:\ArcGIS\Data\Test\长江1980_pyInt.tif') # 保存整除结果：小类合并到大类的结果