# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:34
Author:   Xienuli
File:     chapter11-1.py
"""
#表的横向拼接
#一对一
import pandas as pd
#创建一个字典数据data1
data1 = {'名次':[1, 2, 3, 4],
        '姓名':['小张', '小王', '小李', '小赵'],
        '学号':[100, 101, 102, 103],
        '成绩':[650, 600, 578, 550]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df1
df1 = pd.DataFrame(data1)
#创建一个字典数据data2
data2 = {'学号':[100, 101, 102, 103],
        '班级':['一班', '一班', '二班', '三班']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df2
df2 = pd.DataFrame(data2)
#使用merge()方法对两个表进行拼接
df = pd.merge(df1, df2)
#输出合并表
print(df)