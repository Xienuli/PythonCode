# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:39
Author:   Xienuli
File:     chapter7-5.py
"""
#按照多列数值进行排序
import pandas as pd
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#使用sort_values()方法进行排序（默认为升序）
df.sort_values(by = ["销售ID", "成交时间"],ascending = [True, False],inplace = True)
#输出排序后的数据表
print(df)
