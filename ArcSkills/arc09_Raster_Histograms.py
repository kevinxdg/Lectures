#coding=utf-8

import arcpy
import arcpy
import glob
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#---------------------------------------------------------------

def ras_to_list(inRas, vmin, vmax ):
    arr = arcpy.RasterToNumPyArray(inRas)  # 转为二维矩阵
    arr = arr.tolist()  # 一维向量
    lst = [i for item in arr for i in item]
    tmplst = []
    for value in lst:
        if (value >= vmin) and (value <= vmax):
            tmplst.append(value)
    return tmplst


#---------------------------------------------------------------


#---
m_data_dir = r'D:\Workspace\Data\YZProject\FVC\FVCComp\MODIS'
g_data_dir = r'D:\Workspace\Data\YZProject\FVC\FVCComp\GIMMS'

for iYear in range(2003,2007):
    mRas_file = glob.glob1(m_data_dir,'*' + str(iYear) +'*.tif')
    gRas_file = glob.glob1(g_data_dir,'*' + str(iYear) +'*.tif')
    mRas = arcpy.Raster(m_data_dir + '\\' + mRas_file[0])
    gRas = arcpy.Raster(g_data_dir + '\\' + gRas_file[0])
    dRas = mRas - gRas
    dlist = ras_to_list(dRas,-2, 2)
    bins = np.linspace(-1,1,41)
    s = pd.cut(dlist, bins)
    values = s.value_counts().values
    print(values)
    #plt.hist(dlist,bins)
    stats.probplot(dlist,dist='norm',plot=plt)
    plt.show()
    m = 0.04 #np.mean(dlist)
    #t, p = stats.ttest_1samp(dlist,m)

    mlist = ras_to_list(mRas,-1,1)
    glist = ras_to_list(gRas,-1,1)
    r = stats.ttest_ind(mlist,glist)
    print(r)









