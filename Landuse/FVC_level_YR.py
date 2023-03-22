#coding=utf-8
import os
import arcpy
import arcpy
import glob

# 环境设置参数
data_dir = 'D:\\Workspace\\Data\\YZProject\\FVC\\FVC_Annual\\'
out_dir = 'D:\\Workspace\\Data\\YZProject\\FVC\\FVC_Level\\'
trans_dir = 'D:\\Workspace\\Data\\YZProject\\FVC\\FVC_Trans\\'
land_dir = 'D:\\Workspace\\Data\\YZProject\\landuse\\'
land_trans_dir = 'D:\\Workspace\\Data\\YZProject\\FVC\\land_Trans\\'
os.chdir(data_dir) # 改变当前文件到数据目录

# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

# 读取文件的路径q rhf rhf psu
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


for iYear in range(1983,2021):
    cfile = glob.glob1(out_dir,'*'+ str(iYear) + '*.tif')
    pfile = glob.glob1(out_dir,'*'+ str(iYear - 1) + '*.tif')
    cFVC = arcpy.Raster(out_dir + cfile[0])
    pFVC = arcpy.Raster(out_dir + pfile[0])
    tFVC = pFVC * 100 + cFVC
    #tFVC.save()

iyears= [1982,1990,2000,2010,2020]
for i in range(1, 5):
    cfile = glob.glob1(out_dir,'*'+ str(iyears[i]) + '*.tif')
    pfile = glob.glob1(out_dir, '*' + str(iyears[i-1]) + '*.tif')
    cFVC = arcpy.Raster(out_dir + cfile[0])
    pFVC = arcpy.Raster(out_dir + pfile[0])
    tFVC = pFVC * 100 + cFVC
    tFVC.save(trans_dir + 'FVC_Trans_' + str(iyears[i]) + '.tif')
    print(iyears[i],'--Done')

for i in range(1,5):
    lfile = glob.glob1(land_dir,'*'+ str(iyears[i]) + '*.tif')
    cfile = glob.glob1(out_dir,'*'+ str(iyears[i]) + '*.tif')
    lLand = arcpy.Raster(land_dir + lfile[0])
    cFVC = arcpy.Raster(out_dir + cfile[0])
    level_land = lLand * 10000 + cFVC
    level_land.save(land_trans_dir + 'Land_Trans_' + str(iyears[i]) + '.tif')


# 增加计算1982到2020的转换
cfile = glob.glob1(out_dir,'*1982*.tif')
pfile = glob.glob1(out_dir, '*2020*.tif')
cFVC = arcpy.Raster(out_dir + cfile[0])
pFVC = arcpy.Raster(out_dir + pfile[0])
tFVC = pFVC * 100 + cFVC
tFVC.save(land_trans_dir + 'FVC_Trans_8220.tif')
print('[1982-2020]--Done')

lfile = glob.glob1(land_dir, '*2020*.tif')
lLand = arcpy.Raster(land_dir + lfile[0])
level_land = lLand * 10000 + tFVC
level_land.save(land_trans_dir + 'Land_Trans_8220.tif')