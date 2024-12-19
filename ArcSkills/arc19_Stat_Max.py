# 统计极温指标
# 大于35度天数、连续大于35度天数、连续大于35度的最大天数

# 使用函数 arcpy.TableToExcel_conversion

import arcpy
import arcpy
from arcpy.sa import *

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

for year in range(1981,2024):
    shp_file = r'F:\ArcGIS\Data\Climatatic\逐日最高气温\【立方数据学社】%d年逐日最高气温.shp' % year
    output_file = r'F:\ArcGIS\Data\Climatatic\最高气温属性表\%d年逐日最高气温.xlsx' % year
    arcpy.TableToExcel_conversion(shp_file, output_file)
    print(r'[%d]-完成导出' % year)
