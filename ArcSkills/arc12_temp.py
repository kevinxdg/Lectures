import arcpy
import arcpy
import calendar

# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖


def days(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if year % 100 == 0:  #1900
           if year % 400 == 0: # False
               return 29
           else:
               return 28
        elif year % 4 == 0:
            return 29
        else:
            return 28

#print (calendar.monthrange(2023,2)[1])


sum = 0
for year in range(1981,2024):   # 下载的数据年份
    for month in range(1,13):   # 对应月份
        for day in range(1, days(year,month)+1):
            sname = r'F:\ArcGIS\Data\Test\逐日平均温度\%d-%02d-%02d.tif' % (year,month,day)
            print(sname)
            #ras = arcpy.Raster(sname)
            sum = sum + 1
print(sum)


