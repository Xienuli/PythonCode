# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:35
Author:   Xienuli
File:     chapter11-4.py
"""
#连接键的类型
#默认以公共列作为连接键
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
print(pd.merge(df1, df2))
#用on来指定连接键
print(pd.merge(df1, df2,on = "学号"))

#重新为data2赋值
data2 = {'学号':[100, 101, 102, 103],
         '姓名':['小张', '小王', '小李', '小赵'],
         '班级':['一班', '一班', '二班', '三班']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df2
df2 = pd.DataFrame(data2)
#多个连接键
print(pd.merge(df1, df2,on = ["学号", "姓名"]))

#重新为data1赋值
data1 = {'名次':[1, 2, 3, 4],
        '姓名':['小张', '小王', '小李', '小赵'],
        '编号':[100, 101, 102, 103],
        '成绩':[650, 600, 578, 550]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df2
df1 = pd.DataFrame(data1)
#重新为data2赋值
data2 = {'学号':[100, 101, 102, 103],
         '班级':['一班', '一班', '二班', '三班']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df2
df2 = pd.DataFrame(data2)
#分别指定左右连接键
print(pd.merge(df1, df2,left_on = "编号", right_on= "学号"))

#把索引列当作连接键
#左表右表均为索引
print(pd.merge(df1.set_index("编号"), df2.set_index("学号"), left_index = True, right_index = True))
#索引列和普通列混用
print(pd.merge(df1.set_index("编号"), df2, left_index = True, right_on = "学号"))