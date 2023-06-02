# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 15:45
Author:   Xienuli
File:     chapter13-3.py
"""
#用plt.subplot函数建立坐标系
import matplotlib.pyplot as plt
import numpy as np
#表示将图表的整个区域分成2行2列，且在第1个坐标系里面绘图
plt.subplot(2,2,1)
#设置纵坐标刻度
plt.yticks([0.0, 0.25, 0.50, 0.75, 1.00])
#显示图形
plt.show()

#横坐标
x = np.arange(6)
#纵坐标
y = np.arange(6)
#将图标的整个区域分成2行2列，且在第1个坐标系上做折线图
plt.subplot(2,2,1)
#折线图
plt.plot(x,y)
#设置纵坐标刻度
plt.yticks([0, 2, 4])
#将图标的整个区域分成2行2列，且在第4个坐标系上绘图
plt.subplot(2,2,4)
#柱状图
plt.bar(x,y)
#设置纵坐标刻度
plt.yticks([0, 2, 4])
#显示图形
plt.show()


