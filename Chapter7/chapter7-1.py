# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:37
Author:   Xienuli
File:     chapter7-1.py
"""
#数值替换
import numpy as np
import pandas as pd
#创建一个字典数据data
data = {'订单编号': ['A1', 'A2', 'A3', 'A4', 'A5'],
        '客户姓名': ['张通', '李谷', '孙凤', '赵恒', '赵恒'],
        '唯一识别码': ['101', '102', '103', '104', '104'],
        '年龄':[31,45,23,240,240],
        '成交时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/11', '2018/8/12']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table7-01.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-01.xlsx')
#使用repalce()方法对某个值进行替换
df["年龄"].replace(240,33,inplace=True)
#输出替换后的数据表
print(df)

#创建一个字典数据data，其中包含编号、年龄、性别和注册时间4个字段
data = {'编号': ['A1', 'A2', np.NAN,'A4'],
        '年龄': [54, 16, np.NAN,41],
        '性别': ['男', np.NAN, np.NAN,'男'],
        '注册时间':['2018/8/8','2018/8/9',np.NAN,'2018/8/11']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#使用repalce()方法对NAN值进行替换相当于使用fillna()方法
df.replace(np.NAN,0,inplace=True)
#输出替换后的数据表
print(df)