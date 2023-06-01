# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:25
Author:   Xienuli
File:     chapter5-5.py
"""
#查看数据类型
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-04.xlsx')
#查看订单编号这一列的数据类型
print(df["订单编号"].dtype)
#查看唯一识别码这一列的数据类型
print(df["唯一识别码"].dtype)
#类型转换
print(df["唯一识别码"].dtype)#查看唯一识别码这一列的数据类型
print(df["唯一识别码"].astype("float64"))#将唯一识别码从int类型转换为float类型