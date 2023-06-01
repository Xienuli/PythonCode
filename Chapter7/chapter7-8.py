# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:39
Author:   Xienuli
File:     chapter7-8.py
"""
#删除行
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#重命名行索引
df.index = ["0a","1b","2c","3d","4e"]
#输出原始表
print(df)
#删除行的方法一
df.drop(["0a","1b"],axis = 0,inplace = True)
print(df)
#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#重命名行索引
df.index = ["0a","1b","2c","3d","4e"]
#删除行的方法二
df.drop(df.index[[0,1]],axis = 0,inplace = True)
#输出删除后的数据表
print(df)
#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#重命名行索引
df.index = ["0a","1b","2c","3d","4e"]
#删除行的方法三
df.drop(index = ["0a","1b"],inplace = True)
#输出删除后的数据表
print(df)

#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#重命名行索引
df.index = ["0a","1b","2c","3d","4e"]
#实现删除特定行的原理：不直接删除满足条件的行，而是把不满足条件的值筛选出来作为新的数据源
print(df[df["年龄"] < 40])



