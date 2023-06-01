# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:42
Author:   Xienuli
File:     chapter7-15.py
"""
#索引重塑
import pandas as pd
#创建一个字典数据data
data = {'C1':[1, 4],
        'C2':[2, 5],
        'C3':[3, 6],}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#重命名行索引
df.index = ["S1","S2"]
#输出原始表
print(df)
#stack()方法将表格型数据转换为树型数据
print(df.stack())
#unstack()方法将树型数据转换为表格型数据
print(df.stack().unstack())