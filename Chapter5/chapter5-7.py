# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:26
Author:   Xienuli
File:     chapter5-7.py
"""
#重置索引
import pandas as pd
#创建一个字典数据data
data = {
    'Z1': ['A', 'A', 'B', 'B'],
    'Z2': ['a', 'b', 'a', 'b'],
    'C1': [1, 3, 5, 7],
    'C2': [2, 4, 6, 8]
}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将 'Z1' 和 'Z2' 列设置为行索引
df.set_index(['Z1','Z2'], inplace=True)
print(df.reset_index())#默认将全部index转化为columns
print(df.reset_index(level=0))#将第0级索引转化为columns
print(df.reset_index(drop = True))#将原索引删除，不加入columns