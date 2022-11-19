# coding=utf-8

import arcpy
import arcpy
import glob

FVC_path = r'F:\ArcGIS\Data\FVC'               #  已有的分不同土地利用提取的FVC
output_path = r'F:\ArcGIS\Data\FVCMosaic'          #  用于保存合成的FVC地址

files_2000 = glob.glob1(FVC_path,'*2000*.tif')         # 获取数据地址下，名称包含2000、扩展名为.tif的文件
full_files_2000 = [FVC_path + '\\' + f for f in files_2000]   # 组成全路径
# 根据 镶嵌工具的语法（参考工具帮助）
# 第1个参数是要镶嵌的所有数据
# 第2个参数是保存数据的地址
# 第3个参数是保存数据的名称
# 第4个参数表示要镶嵌的波段数
arcpy.MosaicToNewRaster_management(full_files_2000,output_path,'FVC2000.tif',number_of_bands=1)

# 以下请完成，对2020年FVC进行镶嵌

print('Done')








