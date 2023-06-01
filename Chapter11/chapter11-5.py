# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:36
Author:   Xienuli
File:     chapter11-5.py
"""
#连接方式
#内连接
import pandas as pd
#创建一个字典数据data1
data1 = {'名次':[1, 2, 3, 4],
        '姓名':['小张', '小王', '小李', '小赵'],
        '学号':[100, 101, 102, 103],
        '成绩':[650, 600, 578, 550]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df1
df1 = pd.DataFrame(data1)
#创建一个字典数据data2
data2 = {'姓名':['小张', '小王', '小李', '小钱'],
        '学号':[100, 101, 102, 104],
        '班级':['一班', '一班', '二班', '三班']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df2
df2= pd.DataFrame(data2)
#内连接
print(pd.merge(df1, df2, on = "学号", how = "inner"))
#左连接
print(pd.merge(df1, df2, on = "学号", how = "left"))
#右连接
print(pd.merge(df1, df2, on = "学号", how = "right"))
#外连接
print(pd.merge(df1, df2, on = "学号", how = "outer"))
#重复列名处理
print(pd.merge(df1, df2, on = "学号", how = "inner",suffixes = ["_L", "_R"]))