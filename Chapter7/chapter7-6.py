# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:39
Author:   Xienuli
File:     chapter7-6.py
"""
#数值排名
import pandas as pd

#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
print(df["销售ID"])
# 对数据表 df 中的 "销售ID" 列进行排名，并使用平均值法计算排名值，返回一个 Series 类型的数据
print(df["销售ID"].rank(method="average"))
# 对数据表 df 中的 "销售ID" 列进行排名，并使用先来先得法计算排名值，返回一个 Series 类型的数据
print(df["销售ID"].rank(method="first"))
# 对数据表 df 中的 "销售ID" 列进行排名，并使用最小值法计算排名值，返回一个 Series 类型的数据
print(df["销售ID"].rank(method="min"))
# 对数据表 df 中的 "销售ID" 列进行排名，并使用最大值法计算排名值，返回一个 Series 类型的数据
print(df["销售ID"].rank(method="max"))