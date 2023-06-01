# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:33
Author:   Xienuli
File:     chapter10-5.py
"""
#数据透视表
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#客户分类作为index，区域作为columns，用户ID作为values，对values执行count运算
df = pd.pivot_table(df,values = "用户ID", columns = "区域", index = "客户分类", aggfunc = "count")
#输出数据表
print(df)

#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#Python数据透视表中的默认合计列默认是关闭的，修改其值为True可以让其显示出来
df = pd.pivot_table(df,values = "用户ID", columns = "区域", index = "客户分类", aggfunc = "count",margins = True)
#输出数据表
print(df)

#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#合计列默认名称为All，可以通过设置参数margins_name的值进行修改
df = pd.pivot_table(df,values = "用户ID", columns = "区域", index = "客户分类", aggfunc = "count",margins = True, margins_name = "总计")
#输出数据表
print(df)

#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#NaN表示缺失值，可以通过设置参数fill_value的值对缺失值进行填充
df = pd.pivot_table(df,values = "用户ID", columns = "区域", index = "客户分类", aggfunc = "count",margins = True, fill_value = 0)
#输出数据表
print(df)

#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#aggfunc用来表示计算类型，当只传入一种类型时，表示对所有的值字段都进行同样的计算；如果需要对不同值进行不同的计算类型，则需要传入一个字典，其中键为列名，值为计算方式
df = pd.pivot_table(df,values = ["用户ID", "7月销量"], columns = "区域", index = "客户分类", aggfunc = {"用户ID":"count","7月销量":"sum" })
#输出数据表
print(df)

#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#重置索引
df = pd.pivot_table(df,values = "用户ID", columns = "区域", index = "客户分类", aggfunc = "count").reset_index()
#输出数据表
print(df)