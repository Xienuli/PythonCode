# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 16:01
Author:   Xienuli
File:     chapter13-4.py
"""
#用plt.subplots函数建立坐标系
import matplotlib.pyplot as plt
import numpy as np
#表示将图表的整个区域分成2行2列，并将4个坐标系全部返回
fig, axes = plt.subplots(2, 2)
#横坐标
x = np.arange(6)
#纵坐标
y = np.arange(6)
#在[0,0]坐标系中绘制折线图
axes[0,0].plot(x,y)
#在[1,1]坐标系中绘制柱状图
axes[1,1].bar(x,y)
#设置纵坐标刻度
axes[0, 0].set_yticks([0, 2, 4])
axes[1, 1].set_yticks([0, 2, 4])
#显示图形
plt.show()
