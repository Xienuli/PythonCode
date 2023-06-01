# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:41
Author:   Xienuli
File:     chapter7-13.py
"""
#插入新的行或列
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#输出原始表
print(df)
#使用insert()方法，向原始表中插入数据
df.insert(2,"商品类别",["cat01", "cat02", "cat03", "cat04", "cat05"])
#输出插入后的数据表
print(df)