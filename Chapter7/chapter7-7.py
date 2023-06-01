# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:39
Author:   Xienuli
File:     chapter7-7.py
"""
#删除列
import pandas as pd

#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#输出原始表
print(df)
#删除列的方法一
df.drop(["销售ID","成交时间"],axis = 1,inplace = True)
#输出删除后的数据表
print(df)
#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#删除列的方法二
df.drop(df.columns[[4,5]],axis = 1,inplace = True)
#输出删除后的数据表
print(df)
#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#删除列的方法三
df.drop(columns = ["销售ID","成交时间"],inplace = True)
#输出删除后的数据表
print(df)
