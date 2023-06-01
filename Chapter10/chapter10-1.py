# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:30
Author:   Xienuli
File:     chapter10-1.py
"""
#数据分组：分组键是列名
import pandas as pd
#利用groupby()方法进行数据分组
#创建一个字典数据data
data = {'用户ID':[59224, 55295, 46035, 2459,22179,22557],
        '客户分类':['A类', 'B类', 'A类', 'C类', 'B类', 'A类'],
        '区域':['一线城市', '三线城市', '二线城市', '一线城市', '三线城市', '二线城市'],
        '是否省会':['是', '否', '是', '是', '否', '是'],
        '7月销量':[6, 37, 8, 7, 9, 42],
        '8月销量':[20, 27, 1, 8, 12, 20],
        '9月销量':[0 , 35, 8, 14, 4, 55]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table10-01.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table10-01.xlsx')
#按照 "客户分类" 列进行分组，返回一个 DataFrameGroupBy 对象
print(df.groupby("客户分类"))
#对分组后的数据进行计数操作，返回一个新的 DataFrame 对象
print(df.groupby("客户分类").count())
#对分组后的数据进行求和操作，只对数值列进行计算，返回一个新的 DataFrame 对象
print(df.groupby("客户分类").sum(numeric_only=True))
#按照 "客户分类" 和 "区域" 两列进行分组，返回一个 DataFrameGroupBy 对象
print(df.groupby(["客户分类","区域"]).count())
#对分组后的数据进行计数操作，返回一个新的 DataFrame 对象
print(df.groupby(["客户分类","区域"]).sum(numeric_only=True))
#对 "客户分类" 列进行分组，只对 "用户ID" 列进行计数操作，返回一个新的 Series 对象
print(df.groupby("客户分类")["用户ID"].count())
