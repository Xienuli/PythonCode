# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:29
Author:   Xienuli
File:     chapter6-4.py
"""
#行列同时选择
import pandas as pd
#从表格table6-02中读取数据，赋值给df
df = pd.read_excel(r'table6-02.xlsx')
#重命名行索引
df.index = ["一","二","三","四","五"]
#获取第一行、第三行和第一列、第三列数据
print(df.loc[["一","三"],["订单编号","唯一识别码"]])#通过普通索引+普通索引选择指定的行和列
print(df.iloc[[0,1],[0,2]])#通过位置索引+位置索引选择指定的行和列

#从表格table6-03中读取数据，赋值给df
df = pd.read_excel(r'table6-03.xlsx')
print(df[df["年龄"] < 200][["订单编号","年龄"]])#通过布尔索引+普通索引选择指定的行和列

#从表格table6-02中读取数据，赋值给df
df = pd.read_excel(r'table6-02.xlsx')
#重命名行索引
df.index = ["一","二","三","四","五"]
print(df.iloc[0:3,1:3])
print(df.loc["一":"三",["客户姓名", "唯一识别码"]])#切片索引+普通索引选择指定的行和列
#print(df.ix[0:3,["客户姓名","唯一识别码"]])
#在 Pandas 1.0.0 版本之后，ix 方法已经被废弃，因此在使用 ix 方法时会出现 'DataFrame' object has no attribute 'ix' 的错误提示。