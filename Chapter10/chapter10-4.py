# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:31
Author:   Xienuli
File:     chapter10-4.py
"""
#对分组后的结果重置索引
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-02.xlsx')
#roupby("客户分类")表示按照"客户分类"这个列进行分组，sum(numeric_only=True)表示对分组后的每个数值型列进行求和，返回一个Series类型的结果。
print(df.groupby("客户分类").sum(numeric_only=True))
#reset_index()函数将第一行代码中的Series类型结果转化为数据框，使"客户分类"变成一个列名 (原来是行索引)，方便后续处理和输出。
print(df.groupby("客户分类").sum(numeric_only=True).reset_index())