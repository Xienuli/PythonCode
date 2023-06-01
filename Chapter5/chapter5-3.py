# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:24
Author:   Xienuli
File:     chapter5-3.py
"""
#缺失值填充
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-02.xlsx')
#对数据表中的所有缺失值进行填充
print(df.fillna(0))
#创建一个字典数据data，其中包含编号、年龄、性别和注册时间4个字段
data = {'编号': ['A1', 'A2', 'A3', 'A4'],
        '年龄': [54, 16, None, 41],
        '性别': ['男', '', '女', '男'],
        '注册时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/11']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table5-03.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-03.xlsx')
#按不同列填充
print(df.fillna({"性别":"男"}))#对性别进行填充
print(df.fillna({"性别":"男","年龄":"30"}))#同时对性别和年龄进行填充