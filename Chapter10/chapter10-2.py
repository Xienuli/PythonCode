# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:30
Author:   Xienuli
File:     chapter10-2.py
"""
#数据分组：分组键是Series
#把DataFrame的其中一列取出来就是一个Series
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#输出“客户分类”Series
print(df["客户分类"])
#按照一个Series进行分组
print(df.groupby(df["客户分类"]).count())
#按照多个Series进行分组
print(df.groupby([df["客户分类"],df["区域"]]).sum(numeric_only=True))
#对分组后的某些列进行汇总计算
print(df.groupby(df["客户分类"])["用户ID"].count())

