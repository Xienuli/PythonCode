# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:31
Author:   Xienuli
File:     chapter10-3.py
"""
#能一次使用多次汇总方式、针对不同列做不同的汇总运算的aggregate()方法
import pandas as pd
#创建一个字典数据data
data = {'用户ID':[59224, 55295, 46035, 2459,22179, 22557],
        '客户分类':['A类', 'B类', 'A类', 'C类', 'B类', 'A类'],
        '7月销量':[6, 37, 8, 7, 9, 42],
        '8月销量':[20, 27, 1, 8, 12, 20]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table10-02.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-02.xlsx')
#输出原始表
print(df)
#对数据框 df 按照 "客户分类" 列进行分组，并对每一组内的各列应用 "count" 和 "sum" 两种方法进行统计汇总
print(df.groupby("客户分类").aggregate(["count","sum"]))
#对数据框 df 按照 "客户分类" 列进行分组，并对每一组内的 "用户ID" 列使用 "count" 方法，"7月销量"和"8月销量"列使用 "sum" 方法进行统计汇总
print(df.groupby("客户分类").aggregate({"用户ID":"count","7月销量":"sum","8月销量":"sum"}))
