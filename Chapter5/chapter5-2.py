# _*_ coding: utf-8 _*_
"""
Time:     2023/5/30 16:24
Author:   Xienuli
File:     chapter5-2.py
"""
#缺失值删除
import pandas as pd
#创建一个字典数据data，其中包含编号、年龄、性别和注册时间4个字段
data = {'编号': ['A1', 'A2', '','A4'],
        '年龄': [54, 16, None,41],
        '性别': ['男', '', '','男'],
        '注册时间':['2018/8/8','2018/8/9','','2018/8/11']}
#将字典类型的数据转化为DataFrame数据表，并赋值给df
df = pd.DataFrame(data)
#将数据保存在excel文件中，不包含行索引
df.to_excel(r'table5-02.xlsx', index=False)
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-01.xlsx')
#删除含有NaN值的行
print(df.dropna())
#从表格中读取数据，赋值给df
df = pd.read_excel(r'table5-02.xlsx')
#如果想删除空白行，只要给dropna()方法传入一个参数how = "all"即可，这样就会只删除那些全为空值的行，不全为空值的行就不会被删除。
print(df.dropna(how = "all"))