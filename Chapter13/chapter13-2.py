# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 15:33
Author:   Xienuli
File:     chapter13-2.py
"""
#用plt.subplot2grid函数建立坐标系
import matplotlib.pyplot as plt
import numpy as np
#将图表的整个区域分为2行2列，且在（0，0）处绘图
plt.subplot2grid((2,2),(0,0))
#显示图形
plt.show()

#横坐标
x = np.arange(6)
#纵坐标
y = np.arange(6)
#将图表的整个区域分为2行2列，且在（0，0）处绘图
plt.subplot2grid((2,2),(0,0))
#折线图
plt.plot(x,y)
#设置纵坐标刻度
plt.yticks([0, 2, 4])
#将图表的整个区域分为2行2列，且在（0，1）处绘图
plt.subplot2grid((2,2),(0,1))
#柱形图
plt.bar(x,y)
#设置纵坐标刻度
plt.yticks([0, 2, 4])
#显示图形
plt.show()

