# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 17:13
Author:   Xienuli
File:     chapter13-11.py
"""
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])

plt.plot(x,y)
#关闭坐标轴显示
plt.axis("off")
#显示图形
plt.show()