# coding=utf-8

import arcpy
import arcpy
import glob

# 环境设置参数
arcpy.env.workspace = 'H:\\Data\\GIS\\Hubei\\FVC\\TM\\FVCRate\\'  # 设置本代码的工作文件
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True
#arcpy.env.extent = "MAXOF"


# 数据准备
FVC2000 = arcpy.Raster('H:\\Data\\GIS\\Hubei\\FVC\\TM\\2000FVC\\2000FVC.tif')
FVC2020 = arcpy.Raster('H:\\Data\\GIS\\Hubei\\FVC\\TM\\2020FVC\\2020FVC.tif')
FVCrate_file = 'FVCrate.tif'

#print(arcpy.GetRasterProperties_management(FVC2000,'TOP'))
#print(arcpy.GetRasterProperties_management(FVC2000,'LEFT'))
#print(arcpy.GetRasterProperties_management(FVC2000,'RIGHT'))
#print(arcpy.GetRasterProperties_management(FVC2000,'BOTTOM'))

#print(arcpy.GetRasterProperties_management(FVC2020,'TOP'))
#print(arcpy.GetRasterProperties_management(FVC2020,'LEFT'))
#print(arcpy.GetRasterProperties_management(FVC2020,'RIGHT'))
#print(arcpy.GetRasterProperties_management(FVC2020,'BOTTOM'))


FVCRate = (FVC2020 - FVC2000) / FVC2000
print(FVCrate_file)
FVCRate.save(FVCrate_file)

print('Done')
