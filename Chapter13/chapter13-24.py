# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 22:29
Author:   Xienuli
File:     chapter13-24.py
"""
#绘制气泡图
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标系
plt.subplot(1,1,1)
#指明x的值
x = np.array([5.5,6.6,8.1,15.8,19.5,22.4,28.3,28.9])
#指明y的值
y = np.array([2.38,3.85,4.41,5.67,5.44,6.03,8.15,6.87])
#绘图
colors = y * 10#根据y值的大小生成不同的颜色
area = y * 100#根据y值的大小生成大小不同的形状
plt.scatter(x,y,c = colors, marker = "o",s = area)
#设置标题
plt.title("1—8月平均气温与啤酒销量关系图",loc = "center")
#添加数据标签
for a,b in zip(x,y):
    plt.text(a, b, b, ha = 'center', va = 'center',fontsize =10, color = "white")
#设置x轴和y轴名称
plt.xlabel('平均气温')
plt.ylabel('啤酒销量')
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart07.svg')