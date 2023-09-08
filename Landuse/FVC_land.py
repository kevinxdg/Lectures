#code=utf-8

# ---------------------------------------
# 统计土地转移过程中FVC变化
# ---------------------------------------

import os
import sys
import arcpy
import arcpy
import glob

# 导入公共包
lib_dir = r'D:\Workspace\PythonLibs\ObjectLib'
sys.path.append(lib_dir)
from dataTools.dataObjects import *
from timeTools.timeObjects import *

# 环境设置参数
#os.chdir(r'D:\Workspace\Data\HBProject\Landuse')

data_dir = r'D:\Workspace\Data\YZProject\Landuse'
fvc_dir = r'D:\Workspace\Data\YZProject\FVC\FVC_Annual'
out_dir = r'D:\Workspace\Data\YZProject\Results\FVCLand'



exl = ExcelHelper()
exl.new_workbook(out_dir + r'\fvc_land.xlsx')

#os.chdir(data_dir) # 改变当前文件到数据目录

# 设定 arcpy 的环境
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖

#
def ras_to_vec(ras,vmax=1, vmin=0, bequal=True):
    arr = arcpy.RasterToNumPyArray(ras)  # 转为二维矩阵
    lst = [i for item in arr for i in item]    # 将二维矩阵转成一维列表
    vmin = 0
    vmax = 70
    tmplst = []
    for value in lst:
        if bequal:
            bcon = (value >= vmin) and (value <= vmax)
        else:
            bcon = (value > vmin) and (value < vmax)
        if bcon:
            tmplst.append(value)
    return tmplst

def stat_landchange_fvc(landtype):
    tags = ['1982', '1990', '2000', '2010', '2020']
    for i in range(4):
        f_tag = tags[i]
        l_tag = tags[i + 1]
        f_land_use = glob.glob1(data_dir, r'*' + f_tag + r'*.tif')
        l_land_use = glob.glob1(data_dir, r'*' + l_tag + r'*.tif')
        f_ras = arcpy.Raster(data_dir + '\\' + f_land_use[0])
        l_ras = arcpy.Raster(data_dir + '\\' + l_land_use[0])
        f_land = arcpy.ia.Con(f_ras,0, 1, r'VALUE = ' + str(landtype))
        l_land  = arcpy.ia.Con(l_ras, 1, 0, r'VALUE = ' + str(landtype))
        m_land = f_land * l_land
        #m_land.save(out_dir + r'\mland' + f_tag + '.tif')
        l_fvc = glob.glob1(fvc_dir, r'*' + l_tag + r'*.tif')
        l_fvc_ras = arcpy.Raster(fvc_dir + '\\' + l_fvc[0])
        l_fvc_result = l_fvc_ras * m_land
        f_fvc = glob.glob1(fvc_dir, r'*' + f_tag + r'*.tif')
        print(r'*' + f_tag + r'*.tif')
        f_fvc_ras = arcpy.Raster(fvc_dir + '\\' + f_fvc[0])
        f_fvc_result = f_fvc_ras * m_land
        f_fvc_result.save(out_dir+ r'\fvcland' + f_tag + '_' + l_tag + '_1.tif')
        l_fvc_result.save(out_dir+ r'\fvcland' + f_tag + '_' + l_tag + '_2.tif')
        f_arr = DataFrameClass(ras_to_vec(f_fvc_result,bequal=False),columns=['FVC'])
        exl.add_sheet(f_tag + '_' + l_tag + '_1')
        exl.copy_DataFrame(f_arr,withtitles=False,withindex=False)
        l_arr = DataFrameClass(ras_to_vec(l_fvc_result,bequal=False),columns=['FVC'])
        exl.add_sheet(f_tag + '_' + l_tag + '_2')
        exl.copy_DataFrame(l_arr,withtitles=False, withindex=False)
        exl.save_workbook()
        print('[' + f_tag + '_' + l_tag +'] Done')


exl.save_workbook()

stat_landchange_fvc(2)





