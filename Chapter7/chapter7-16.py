# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:42
Author:   Xienuli
File:     chapter7-16.py
"""
#宽表转换为长表
import pandas as pd
# 创建一个字典数据 data
data = {'Company':["Apple", "Google", "Facebook"],
        'Name':["苹果", "谷歌", "脸书"],
        'Sale2013':[5000, 3500, 2300],
        'Sale2014':[5050, 3800, 2900],
        'Sale2015':[5050, 3800, 2900],
        'Sale2016':[5050, 3800, 2900]}
#将字典类型的数据转化为 DataFrame 数据表，并赋值给 df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table7-04.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-04.xlsx')
#将 "Company" 和 "Name" 列作为索引
df = df.set_index(['Company', 'Name'])
print(df)
#将宽表转换为长表
df= df.stack()
#输出转换后的长表
print(df)
#进行索引重置
df = df.reset_index()
#索引重置后输出
print(df)

