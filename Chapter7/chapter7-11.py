# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:40
Author:   Xienuli
File:     chapter7-11.py
"""
#数值查找
import  pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#isin()方法：查看数据表中是否包含某个值
print(df["年龄"].isin([31,21]))
#在全表查找是否包含某个值
print(df.isin(["A2",31]))