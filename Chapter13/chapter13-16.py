# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 17:35
Author:   Xienuli
File:     chapter13-16.py
"""
#图表注释
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])

plt.plot(x,y)
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
plt.title(label = "1-9月XXX公司注册用户数")
#设置图表注释
plt.annotate("服务器宕机了",
             xy = (5,1605),
             xytext = (6,1605),
             arrowprops = dict(facecolor = 'black',arrowstyle = '->')#facecolor表示箭的颜色，arrowstyle表示箭的类型。
             )
#显示图形
plt.show()
