import os
import glob


files = os.listdir(r'F:\ArcGIS\Data\Landuse')
print(files)


hdfs = glob.glob1(r'F:\ArcGIS\Data\Landuse', '*.tif')
print(hdfs)

