#加和
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

result = r'C:\Users\ccc\Desktop\12.5\zero.tif'
Result = arcpy.Raster(result)



for year in range(2023,2024):
    for month in range(1,13):
        for day in range(1,days(year,month)+1):
            sname = r'D:\积温数据\积温筛选\C%d-%02d-%02d.tif' % (year, month, day)
            Ras = arcpy.Raster(sname)
            Result = Ras + Result


Result.save(r'D:\积温数据\加和\%d.tif' % (year))
    