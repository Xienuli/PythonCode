# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:40
Author:   Xienuli
File:     chapter7-10.py
"""
#唯一值获取
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#对表df中的销售ID获取唯一值，先把销售ID取出来，然后利用unique()方法获取唯一值。
print(df["销售ID"].unique())