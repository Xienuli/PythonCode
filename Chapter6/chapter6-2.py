# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:28
Author:   Xienuli
File:     chapter6-2.py
"""
#列选择
import pandas as pd
#创建一个字典数据data
data = {'订单编号': ['A1', 'A2', 'A3', 'A4', 'A5'],
        '客户姓名': ['张通', '李谷', '孙凤', '赵恒', '赵恒'],
        '唯一识别码': ['101', '102', '103', '104', '104'],
        '成交时间':['2018/8/8', '2018/8/9', '2018/8/10', '2018/8/11', '2018/8/12']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#为表添加列索引
df.columns = ["订单编号","客户姓名","唯一识别码","成交时间"]
#为表添加行索引
df.index = ["一","二","三","四","五"]
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table6-02.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table6-02.xlsx')
#重命名行索引
df.index = ["一","二","三","四","五"]
#选择一行
print(df.loc["一"])
#选择多行
print(df.loc[["一","二"]])
#通过传入位置来获取数据时需要用到iloc方法
print(df.iloc[0])#获取第1行的数值
print(df.iloc[:,[0,1]])#获取第1行和第2行的数值
print(df.iloc[:,0:3])#获取第1行到第3行的数值

