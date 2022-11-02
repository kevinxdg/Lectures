# coding=utf-8

import arcpy
import numpy as np
file_path = r'H:\Python\Data\2000年草地FVC.tif'

ras = arcpy.Raster(file_path)
arr = arcpy.RasterToNumPyArray(ras).tolist()

lst = [i for item in arr for i in item]

print(lst)


def get_list_by_values(self, value_min, value_max):
    tmp_list = []
    for value in self.to_list:
        if (value >= value_min) and (value <= value_max):
            tmp_list.append(value)
    return tmp_list


#p05 = np.percentile(self.value_list, percent)
