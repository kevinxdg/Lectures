def cr(head, feet):
    for c in range(head+1):
        print()
        r = head - c
        if c * 2 + r * 4 == feet:
            return c
    return "无解"
solve = cr(40,100)
print(solve)

import arcpy
import arcpy
ras = arcpy.Raster(r'C:\Users\ccc\Desktop\test\长江1980lucc.tif')
ras_10 = ras * 10
ras_10.save(r'C:\Users\ccc\Desktop\test\长江1980lucc_10_python.tif')

import arcpy


