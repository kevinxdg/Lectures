#coding=utf-8
import os
import arcpy
import arcpy
import glob

# 环境设置参数
data_dir = 'D:\\Workspace\\Data\\YZProject\\FVC\\FVC_Annual\\'
out_dir = 'D:\\Workspace\\Data\\YZProject\\FVC\\FVC_Level\\'
trans_dir = 'D:\\Workspace\\Data\\YZProject\\FVC\\FVC_Trans\\'
land_dir = 'D:\\Workspace\\Data\\YZProject\\Landuse\\'

os.chdir(data_dir) # 改变当前文件到数据目录

# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖


iyears= [1982,1990,2000,2010,2020]
for i in range(1,5):
    lfile = glob.glob1(land_dir,'*'+ str(iyears[i]) + '*.tif')
    cfile = glob.glob1(trans_dir,'*'+ str(iyears[i]) + '*.tif')
    lLand = arcpy.Raster(land_dir + lfile[0])
    cFVC = arcpy.Raster(trans_dir + cfile[0])
    level_land = lLand * 10000 + cFVC
    level_land.save(trans_dir + 'Land_Trans_' + str(iyears[i]) + '.tif')
    print(iyears[i],'---Done')