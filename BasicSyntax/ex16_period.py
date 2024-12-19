#
from datetime import datetime, timedelta
import pandas as pd

data_excel_file = r'F:\ArcGIS\Data\Climatatic\最高气温属性表\%d年逐日最高气温.xlsx'
output_file = r'F:\ArcGIS\Data\Climatatic\统计\无霜期.xlsx'

prompt_info1 = r'[%d] 已统计'
prompt_info2 =r'结果已保存至 %s' % output_file

#定义函数，确定指定日期是当年的第几天
def day_of_year(year, month, day):
    my_day = datetime(year, month, day)
    first_day = datetime(year, 1, 1)
    delta = my_day - first_day
    return delta.days

def data_lessthanzero(data, value=0):
    return data.lt(value).astype(int)

def start_end_day(year, data_l):
    First_day = datetime(year, 1, 1)
    June30 = day_of_year(year, 6, 30)
    rows, cols = data_l.shape
    period_df = pd.DataFrame(index=range(rows), columns=['start_date', 'end_date', str(year)])
    for i in range(rows):
        start_day = 0
        end_day = day_of_year(year, 12, 31)
        for j in range(June30+1):
            index = June30 - j
            if data_l.iloc[i,index] == 1:
                start_day = index + 1
                break
        for j in range(end_day - June30 + 1):
            index = June30 + j
            if data_l.iloc[i,index] == 1:
                end_day = index - 1
                break
        period_days = end_day - start_day + 1

        start_date = First_day + timedelta(days=start_day)
        end_date = First_day + timedelta(days=end_day)
        period_df.iloc[i,0] = start_date.date()
        period_df.iloc[i,1] = end_date.date()
        period_df.iloc[i,2] = period_days
    return period_df

def cal_period():
    period_data = pd.DataFrame([])
    for year in range(1981, 2024):
        excel_file = data_excel_file % year
        days = day_of_year(year, 12, 31)
        data = pd.read_excel(excel_file, usecols=range(7, days + 8))
        data_l = data_lessthanzero(data)
        period_df = start_end_day(year, data_l)
        period_data = pd.concat([period_data, period_df[str(year)]], axis=1)
        print(prompt_info1 % year)
    print(period_data)
    period_data.to_excel(output_file, index=True)
    print(prompt_info2)






cal_period()
#print(period_data)