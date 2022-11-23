# coding=utf-8

import arcpy
import arcpy

# 环境设置参数
arcpy.env.workspace = r'F:\ArcGIS\Data\FVCMosaic'   # 设置本代码的工作文件
arcpy.env.overwriteOutput = True

# 数据文件准备
data_path = r'F:\ArcGIS\Data\FVCMosaic'          # 数据文件夹地址
data_file = r'FVCrate.tif'                       # 已有的FVC变化率文件
positive_file = r'FVCpositive.tif'               # 要保存的正变化率文件
negative_file = r'FVCnegative.tif'               # 要保存的负变化率文件
#landuse_file = r'F:\ArcGIS\Data\Landuse\luc.tif'   # 湖北省土地利用转移数据文件


# 数据处理
fvc_ras = arcpy.Raster(data_path + '\\' + data_file)       # 读入fvc数据
# 以下进行条件选择，参考 Con函数帮助
# 第1项参数为输入分析的数据
# 第2项参数为条件成立时设定的栅格数据值
# 第3项参数为条件不成立时设定的栅格数据值
# 第4项参数为条件
#

 #This

fvc_int = arcpy.sa.Int(fvc_ras * 1000)


#pos_ras = arcpy.sa.Con(fvc_ras, 1, 0, 'Value > 0' )    # 事实上这个函数运行发现有点问题




# 以下对这个函数的Bug进行改造
p1_ras = arcpy.sa.Con(fvc_int, "0", "1", "value>0")
p2_ras = arcpy.sa.Con(fvc_int, "0", "1", "value<0")

#pos_ras = p1_ras + p2_ras
p1_ras.save(data_path + '\\p1.tif')
p2_ras.save(data_path + '\\p2.tif')
#pos_ras.save(data_path + '\\' + positive_file)

print('Done')