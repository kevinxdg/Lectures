#
from datetime import datetime
import pandas as pd

#定义函数，确定指定日期是当年的第几天
def day_of_year(year, month, day):
    my_day = datetime(year, month, day)
    first_day = datetime(year, 1, 1)
    delta = my_day - first_day
    return delta.days

def data_lessthanzero(data):
    return data.lt(0).astype(int)



def period(year,data_l):
    June30_index = day_of_year(year, 6, 30)
    city_count = 372
    for i in range(city_count):
        days = June30_index + 1
        total_days = day_of_year(year,12,31)
        last_days = total_days -June30_index
        start = 0
        end_date = total_days
        for j in range(days):
            value = data_l.iloc[i,June30_index - j]
            if value == 1:
                start = June30_index - j + 1
                break

        for j in range(last_days):
            value = data_l.iloc[i,June30_index + j]
            if value == 1:
                end_date = June30_index + j - 1
                break
        period_days = end_date - start + 1
        print(period_days)




excel_file = r'F:\ArcGIS\Data\Climatatic\最高气温属性表\%d年逐日最高气温.xlsx' % 1981
data = pd.read_excel(excel_file, usecols="H:NH")
data_l = data_lessthanzero(data)
print(period(1981,data_l))