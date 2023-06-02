# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 17:30
Author:   Xienuli
File:     chapter13-15.py
"""
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
#设置数据标签
plt.text(5,1605,1605)
#显示图形
plt.show()

#plt.text函数是只是针对坐标轴中的具体某一点的（x，y）显示数值str，要想对整个图标显示数据标签，需要用for循环进行遍历
#在（x，y）处显示y值
plt.plot(x,y)
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
plt.title(label = "1-9月XXX公司注册用户数")
for a,b in zip(x,y):
    plt.text(a,b,b,ha = "center", va = "bottom", fontsize = 11)
#显示图形
plt.show()

