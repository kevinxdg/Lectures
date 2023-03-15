#coding =utf-8

from Libs.cmodel import *
data_file = r'Energy.xlsx'
data_path = data_dir + '\\' + data_file
data = pd.read_excel(data_path)
excel_tool.load_workbook(data_path)
data = excel_tool.cell_DataFrame().astype('float')

c = data.corr()
print(data)
print(data.corr())
print(type(c))