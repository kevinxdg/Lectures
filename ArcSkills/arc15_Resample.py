import arcpy
import arcpy
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True        # 保存时允许覆盖


for i in range(1,11):
    filename = r'F:\ArcGIS\Data\Test\YZRTemp\E1981-02-%02d.tif' % i
    outputname = r'F:\ArcGIS\Data\Test\TempReSample\R1981-02-%02d.tif' % i

    print('当前处理文件：' + filename)
    # 重采样的参数：1. 原数据 2. 导出的数据，3. x ,y 尺寸大小 4.采样方法
    arcpy.Resample_management(filename, outputname, "1000 1000", "Nearest")


