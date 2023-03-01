#coding=utf-8
import os
import arcpy
import arcpy
import glob

# 环境设置参数
data_dir = 'D:\\data\\FVC\\FVC_annual\\'
out_dir = 'D:\\data\\FVC\\FVC_Level\\'
os.chdir(data_dir) # 改变当前文件到数据目录

# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

# 读取文件的路径
for iYear in range(1982,2021):
    cfile = glob.glob1(data_dir,'*'+ str(iYear) + '*.tif')
    print(cfile)
    cFVC = arcpy.Raster(data_dir + cfile[0])
    levelFVC = arcpy.sa.Con(cFVC,10,cFVC,'VALUE>=0 AND VALUE<=0.2')
    levelFVC = arcpy.sa.Con(levelFVC,20,levelFVC,'VALUE>0.2 AND VALUE<=0.4')
    levelFVC = arcpy.sa.Con(levelFVC, 30, levelFVC, 'VALUE>0.4 AND VALUE<=0.6')
    levelFVC = arcpy.sa.Con(levelFVC, 40, levelFVC, 'VALUE>0.6 AND VALUE<=0.8')
    levelFVC = arcpy.sa.Con(levelFVC, 50, levelFVC, 'VALUE>0.8 AND VALUE<=1')
    levelFVC.save(out_dir + 'level_' + str(iYear) + '.tif')
    print(iYear, '--Done')





