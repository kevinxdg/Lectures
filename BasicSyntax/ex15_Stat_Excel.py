# 统计极温指标
# 大于35度天数、连续大于35度天数、连续大于35度的最大天数

# pandas 读取 excel

import pandas as pd

output_file = r'F:\ArcGIS\Data\Climatatic\最高气温属性表\%d年逐日最高气温.xlsx' % 1981

# 读取 从 H 到 NH 的数据列
data = pd.read_excel(output_file,usecols="H:NH")

print(data)

print('.........')
#设定比较值
value = 0

# 比较是否大于 value
result = data.lt(value).astype(int)

print(result)