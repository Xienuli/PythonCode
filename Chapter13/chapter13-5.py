# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 16:13
Author:   Xienuli
File:     chapter13-5.py
"""
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])

plt.plot(x,y)
#设置横坐标标题，并设置到x轴的距离为10
plt.xlabel("月份",labelpad = 10)
#设置纵坐标标题，并设置到y轴的距离为10
plt.ylabel("注册人数",labelpad = 10)
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])

#显示图形
plt.show()


