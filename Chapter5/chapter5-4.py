# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:25
Author:   Xienuli
File:     chapter5-4.py
"""
#重复值处理
import pandas as pd
#创建一个字典数据data
data = {'订单编号': ['A1', 'A2', 'A3', 'A3', 'A4', 'A5'],
        '客户姓名': ['张通', '李谷', '孙凤', '孙凤', '赵恒', '赵恒'],
        '唯一识别码': ['101', '102', '103', '103', '104', '104'],
        '成交时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/10', '2018/8/11', '2018/8/12']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table5-04.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-04.xlsx')
#删除重复值
print(df.drop_duplicates())
#针对某一列或某几列重复值删除的判断
print(df.drop_duplicates(subset = "唯一识别码"))
#利用多列去重
print(df.drop_duplicates(subset = ["客户姓名","唯一识别码"]))
#自定义删除重复项时保留设置
print(df.drop_duplicates(subset = ["客户姓名","唯一识别码"],keep = "last"))#保留最后一个值
print(df.drop_duplicates(subset = ["客户姓名","唯一识别码"],keep = False))#不保留任何重复值
