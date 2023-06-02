# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 16:56
Author:   Xienuli
File:     chapter13-9.py
"""
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])
#在2*1坐标系上的第1个坐标系中绘图
plt.subplot(2,1,1)
plt.plot(x,y)
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
plt.xlabel("月份")
plt.ylabel("注册人数")
#轴刻度线设置程双向且下轴刻度线不显示
plt.tick_params(axis = "both", which = "both", direction = "inout", bottom = "false")

#在2*1坐标系上的第2个坐标系中绘图
plt.subplot(2,1,2)
plt.plot(x,y)
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
plt.xlabel("月份")
plt.ylabel("注册人数")
#轴刻度线设置程双向且下轴刻度线不显示
plt.tick_params(axis = "both", which = "both", direction = "inout", labelbottom = 'false')
#调整两个图的间距
plt.subplots_adjust(hspace=0.5)
#显示图形
plt.show()

