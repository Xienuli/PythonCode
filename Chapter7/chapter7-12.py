# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:41
Author:   Xienuli
File:     chapter7-12.py
"""
#区间切分
import pandas as pd
#创建一个字典数据data
data = {'年龄':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#使用cut()方法对区间进行切分
print(pd.cut(df["年龄"], bins = [0, 3, 6, 10]))#cut()方法有一个参数bins用来指明切分区间
#将数据切分成3份
print(pd.qcut(df["年龄"],3))
