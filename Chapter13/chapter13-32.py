# _*_ coding: utf-8 _*_
"""
Time:     2023/6/3 1:23
Author:   Xienuli
File:     chapter13-32.py
"""
import matplotlib.pyplot as plt

#绘制水平线和垂直线
#建立坐标系
plt.subplot(1,2,1)
#绘制一条y等于2且起点是0.2，终点是0.6的水平线
plt.axhline(y = 2,xmin = 0.2,xmax = 0.6)
plt.subplot(1,2,2)
#绘制一条x等于2且起点是0.2终点是0.6的垂直线
plt.axvline(x = 2,ymin = 0.2, ymax = 0.6)
#显示图表
plt.show()