# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:40
Author:   Xienuli
File:     chapter7-9.py
"""
#数值计数
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#查看不同值出现的绝对次数
print(df["销售ID"].value_counts())
#查看不同值出现的占比
print(df["销售ID"].value_counts(normalize = True))
#通过设置sort = False可以实现不按计数值降序排列
print(df["销售ID"].value_counts(normalize = True, sort = False))
