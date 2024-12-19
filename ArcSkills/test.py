import arcpy
result = pandas.DataFrame([])

for year in range(1981, 2024):
    data = pd.read_excel(r'F:\ArcGIS\Data\Climatatic\最高气温属性表\%d年逐日最高气温.xlsx' % year ,usecols=range(7,7+365))
    new_data = data.lt(0).astype(int)
    sumdata = new_data.sum(axis=1)
    result = pd.concat([result, sumdata], axis=1)

print(result)

result.to_excel(r'F:\ArcGIS\Data\Climatatic\统计\test.xlsx', index=True)