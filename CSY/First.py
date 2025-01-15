import arcpy
from arcpy.sa import *


#定义判断天数的函数
def days(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if year % 100 == 0:
            if year % 400 == 0:
                return 29
            else:
                return 28
        elif year % 4 ==0:
            return 29
        else:
            return 28


# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

maskfile = r'C:\Users\ccc\Desktop\test\jc.shp'

#剪切
for year in range(1981,2024):
    for month in range(1,13):
        for day in range(1,days(year,month)+1):
            #sname = r'D:\原始数据\逐日平均气温栅格数据\%d-%02d-%02d.tif' % (year, month, day)
            #ras = ExtractByMask(sname, maskfile)
            #savename = r'D:\积温数据范围剪切\E%d-%02d-%02d.tif' % (year, month, day)


            #ras.save(savename)
            #print('当前处理文件:' + savename)




            # 重采样
            filename = r'D:\积温数据范围剪切\E%d-%02d-%02d.tif' % (year, month, day)
            outputname = r'D:\重采样\R%d-%02d-%02d.tif' % (year, month, day)
            arcpy.Resample_management(filename, outputname, "1000 1000", "Nearest")

            #条件函数
            Ras = arcpy.Raster(outputname)
            ras_10 = Ras - 10
            ras_at = Con(outputname,ras_10,0,'value>=10')
            savename10 = r'D:\积温筛选\C%d-%02d-%02d.tif' % (year, month, day)
            ras_at.save(savename10)
            print('当前处理文件：' + savename10)


