# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:35
Author:   Xienuli
File:     chapter11-3.py
"""
#表的横向拼接
#多对多
import pandas as pd
#创建一个字典数据data1
data1 = {'姓名':['小张', '小张', '小王', '小李', '小李'],
        '学号':[100, 100, 101, 102, 102],
        'f_成绩':[650, 610, 600, 578, 542]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df1
df1 = pd.DataFrame(data1)

#创建一个字典数据data2
data2 = {'学号':[100, 100, 101, 102, 102],
        'e_成绩':[650, 610, 600, 578, 542]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df2
df2 = pd.DataFrame(data2)
#使用merge()方法对两个表进行拼接
df = pd.merge(df1, df2)
#输出合并表
print(df)