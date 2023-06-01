# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:22
Author:   Xienuli
File:     chapter5-1.py
"""
#缺失值查看
import pandas as pd
#创建一个字典数据data，其中包含编号、年龄、性别和注册时间4个字段
data = {'编号': ['A1', 'A2', 'A3', 'A4'],
        '年龄': [54, 16, 47, 41],
        '性别': ['男', '', '女', '男'],
        '注册时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/11']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table5-01.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-01.xlsx')
#使用info()方法查看数据的基本信息
df.info()
#使用isnull()方法来判断哪些值是缺失值，如果是缺失值则返回True，如果不是缺失值则返回False。
print(df.isnull())

