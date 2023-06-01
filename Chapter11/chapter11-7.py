# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:36
Author:   Xienuli
File:     chapter11-7.py
"""
#重叠数据合并
import pandas as pd
#创建一个字典数据data1
data1 = {'编号':[1,2,3,4,5],
         '姓名':['许丹', '李旭文', '程成', '赵涛', '葛颜'],
         '班级':['一班', '一班', '一班', '一班', '二班']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df1
df1 = pd.DataFrame(data1)
#为df1设置行索引
df1 = df1.set_index("编号")
#创建一个字典数据data2
data2 = {'编号':[1,2,3,4],
         '姓名':['赵义', '李鹏', '卫来', '葛颜'],
         '班级':['二班', '二班', '二班', '二班']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df2
df2= pd.DataFrame(data2)
#为df2设置行索引
df2 = df2.set_index("编号")
#不保留原表索引输出合并表
print(pd.concat([df1,df2],ignore_index = True))
#使用drop_duplicates()方法删除重复值
print(pd.concat([df1,df2],ignore_index = True).drop_duplicates())
