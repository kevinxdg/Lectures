#import arcpy
#ras = arcpy.Raster(r'C:\Users\ccc\Desktop\test\长江1980lucc.tif')
#ras_int = ras // 10
#ras_int.save(r'C:\Users\ccc\Desktop\test\长江1980lucc_pyint.tif')
#import arcpy
#ras1 = arcpy.Raster(r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-01.tif')
#ras2 = arcpy.Raster(r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-02.tif')
#ras3 = arcpy.Raster(r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-03.tif')
import arcpy
from arcpy import env
from arcpy.ia import *#调用
ras1 = Con(r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-01.tif',r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-01.tif',0,'value>=10')
ras1.save(r'C:\Users\ccc\Desktop\逐日平均温度\t01.tif')#处理一个

result = ras = Con(r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-10.tif',r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-10.tif',0,'value>=10')
for i in range(1,10)#循环
    filename = r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-%0d.tif' %i
    ras = Con(filename, filename, 0,'value>=10')
    result = result + ras
    savename = r'C:\Users\ccc\Desktop\逐日平均温度\1981-02-0%d.tif' %i
result.save(r'C:\Users\ccc\Desktop\逐日平均温度\sum10.tif')

