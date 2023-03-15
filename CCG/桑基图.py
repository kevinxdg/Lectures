from pyecharts import options as opts
from pyecharts.charts import Sankey
import pandas as pd
import os

data_file_e = r'D:\\Python\\Data\\FVC\\1982,2020FVCzhuanyi\\1982-2020.xlsx'
name = data_file_e
df=pd.read_excel(name)
nodes=[]
for i in range(2):
    values=df.iloc[:,i].unique()
    for value in values:
        dic={}
        dic['name']=value
        nodes.append(dic)
print(nodes)

f1=df.groupby(['name1','name2'])['Count'].sum().reset_index()
print(f1)

f1.columns=['source','target','value']
result=pd.concat([f1])

linkes=[]
for i in result.values:
    dic={}
    dic['source']=i[0]
    dic['target']=i[1]
    dic['value']=i[2]
    linkes.append(dic)
print(linkes)

from pyecharts.charts import Sankey
from pyecharts import options as opts

pic = (
    Sankey()
        .add('',
             nodes,
             linkes,
             linestyle_opt=opts.LineStyleOpts(opacity=0.3, curve=0.5, color='source'),
             label_opts=opts.LabelOpts(position='top'),
             node_gap=30,
             )
        .set_global_opts(title_opts=opts.TitleOpts(title=''))
)

pic.render('1982-2020FVC转移桑基图.html')

