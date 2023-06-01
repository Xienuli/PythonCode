# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:42
Author:   Xienuli
File:     chapter7-17.py
"""
#长表转换为宽表
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-04.xlsx')
#melt()方法实现（因为表中数据为宽表，此处进行转化）
df = df.melt(id_vars = ['Company', 'Name'],
        var_name = 'Year',
        value_name = 'Sale')
#输出长表
print(df)
#将长表转化为宽表
df = df.pivot_table(index = ['Company','Name'], columns = 'Year', values = "Sale")
#输出宽表
print(df)
