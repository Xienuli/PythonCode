# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:38
Author:   Xienuli
File:     chapter7-3.py
"""
#数值排序
import pandas as pd
#创建一个字典数据data
data = {'订单编号': ['A1', 'A2', 'A3', 'A4', 'A5'],
        '客户姓名': ['张通', '李谷', '孙凤', '赵恒', '王娜'],
        '唯一识别码': ['101', '102', '103', '104', '105'],
        '年龄':[31, 45, 23, 36, 21],
        '成交时间':['2018-08-08', '2018-08-09', '2018-08-10', '2018-08-11', '2018-08-11'],
        '销售ID':[1,2,1,2,3]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table7-03.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-03.xlsx')
#使用sort_values()方法进行排序（默认为升序）
df.sort_values(by = ["销售ID"],inplace = True)
#输出排序后的数据表
print(df)
#降序排列
df.sort_values(by = ["销售ID"],ascending = False, inplace = True)
#输出排序后的数据表
print(df)