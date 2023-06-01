# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:38
Author:   Xienuli
File:     chapter7-2.py
"""
#多对一替换
import pandas as pd
#创建一个字典数据data
data = {'订单编号': ['A1', 'A2', 'A3', 'A4', 'A5', 'A6'],
        '客户姓名': ['张通', '李谷', '孙凤', '赵恒', '赵恒', '王丹'],
        '唯一识别码': ['101', '102', '103', '104', '104', '105'],
        '年龄':[31, 45, 23, 240, 260, 280],
        '成交时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/11', '2018/8/12', '2018/8/12']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table7-02.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-02.xlsx')
#多对一替换
df.replace([240,260,280],33,inplace=True)
#输出替换后的数据表
print(df)

#重新从表格中读取数据，赋值给df
df = pd.read_excel(r'table7-02.xlsx')
#多对多替换
df.replace({240:32,260:33,280:34},inplace=True)
#输出替换后的数据表
print(df)
