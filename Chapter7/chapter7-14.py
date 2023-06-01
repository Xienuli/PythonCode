# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:41
Author:   Xienuli
File:     chapter7-14.py
"""
#行列互换
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#输出原始表
print(df)
#对表进行转置，然后输出转置表
print(df.T)
#对转置表进行转置，然后输出表
print(df.T.T)
