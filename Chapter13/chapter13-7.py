# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 17:02
Author:   Xienuli
File:     chapter13-7.py
"""
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])

plt.plot(x,y)
#设置横坐标标题
plt.xlabel("月份")
#设置纵坐标标题
plt.ylabel("注册人数")
#设置x轴刻度
plt.xticks(np.arange(9),["1月份","2月份","3月份","4月份","5月份","6月份","7月份","8月份","9月份"])
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000人","2000人","3000人","4000人","5000人","6000人"])

#显示图形
plt.show()