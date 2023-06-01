# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:26
Author:   Xienuli
File:     chapter5-6.py
"""
#索引设置
import pandas as pd
#创建一个字典数据data
data = {'订单编号': ['A1', 'A2', 'A3', 'A4', 'A5'],
        '客户姓名': ['张通', '李谷', '孙凤', '赵恒', '赵恒'],
        '唯一识别码': ['101', '102', '103', '104', '104'],
        '成交时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/11', '2018/8/12']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table5-05.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-05.xlsx')
#为表添加列索引
df.columns = ["订单编号","客户姓名","唯一识别码","成交时间"]
#输出列索引
print(df.columns)
#为表添加行索引
df.index = [1,2,3,4,5]
#输出行索引
print(df.index)
#重新设置索引
df.set_index("订单编号")#在set_index()里指明要用作索引的列的名称
#输出行索引
print(df.index)
#重命名索引
print(df.rename(columns = {"订单编号":"新订单编号","客户姓名":"新客户姓名"}))
#重命名行索引
print(df.rename(index = {1:"一",2:"二",3:"三"}))
#同时重命名行索引和列索引
print(df.rename(columns = {"订单编号":"新订单编号","客户姓名":"新客户姓名"},index = {1:"一",2:"二",3:"三"}))
