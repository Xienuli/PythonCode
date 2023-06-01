# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:38
Author:   Xienuli
File:     chapter7-4.py
"""
#按照有缺失值的列进行排序
import numpy as np
import pandas as pd
#对data进行重新赋值
data = {'订单编号': ['A1', 'A2', 'A3', 'A4', 'A5'],
        '客户姓名': ['张通', '李谷', '孙凤', '赵恒', '王娜'],
        '唯一识别码': ['101', '102', '103', '104', '105'],
        '年龄':[31, 45, 23, 36, 21],
        '成交时间':['2018-08-08', '2018-08-09', '2018-08-10', '2018-08-11', '2018-08-11'],
        '销售ID':[1,2,np.NAN,2,3]}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#通过设置na_position参数对缺失值的显示位置进行设置，默认为last
df.sort_values(by = ["销售ID"],na_position = "first", inplace = True)
#输出排序后的数据表
print(df)