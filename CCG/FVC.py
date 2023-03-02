#coding=utf-8
import arcpy

G_FVC2000 = arcpy.Raster(r'D:\gisshuju\Changjiang\重叠年份数据03-06年\GIMMS\2003\FVC.A20030.annual.tif')
M_FVC2020 = arcpy.Raster(r'D:\gisshuju\Changjiang\重叠年份数据03-06年\MODIS\2003\FVC.A20030.annual.tif')

sub_FVC = G_FVC2000 - M_FVC2020
