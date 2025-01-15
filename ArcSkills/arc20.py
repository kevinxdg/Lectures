import arcpy
import arcpy
import calendar
from arcpy.sa import *

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")

filename = r'D:\Downloads\Baiduyun\Pre\pre_%d%02d%02d.tif'
new_filename = r'D:\Downloads\Baiduyun\Proj\pre_%d%02d%02d.tif'

for year in range(1981,2023):
    for month in range(1,13):
        days = calendar.monthrange(year,month)[1]
        for day in range(1, days + 1):
            arcpy.management.ProjectRaster(in_raster=filename %(year, month,day), out_raster= new_filename % (year, month, day), out_coor_system=arcpy.env.outputCoordinateSystem, cell_size = "1000 1000",  resampling_type="NEAREST")


