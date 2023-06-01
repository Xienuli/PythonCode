# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:29
Author:   Xienuli
File:     chapter6-3.py
"""
#选择满足条件的行
import pandas as pd
#创建一个字典数据data
data = {'订单编号': ['A1', 'A2', 'A3', 'A4', 'A5'],
        '客户姓名': ['张通', '李谷', '孙凤', '赵恒', '赵恒'],
        '唯一识别码': ['101', '102', '103', '104', '104'],
        '年龄':[31,45,23,240,240],
        '成交时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/11', '2018/8/12']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table6-03.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table6-03.xlsx')
#选择年龄小于200的数据
print(df[df["年龄"] < 200])
#选择年龄小于200且唯一识别码小于102的数据
print(df[(df["年龄"] < 200) & (df["唯一识别码"] < 102)])