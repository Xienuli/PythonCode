# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:42
Author:   Xienuli
File:     chapter7-18.py
"""
#apply()与applymap()函数
import pandas as pd
#创建一个字典数据data
data = {'C1':[1, 4, 7],
        'C2':[2, 5, 8],
        'C3':[3, 6, 9],}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#对C1列中的每个元素加1
first_df = df['C1'].apply(lambda x : x + 1)
#输出新的数据表
print(first_df)
#对表中的每个元素加1
second_df = df.applymap(lambda x : x + 1)
#输出新的数据表
print(second_df)
