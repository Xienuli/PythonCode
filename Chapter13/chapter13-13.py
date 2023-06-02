# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 17:21
Author:   Xienuli
File:     chapter13-13.py
"""
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
x = np.array([1,2,3,4,5,6,7,8,9])
y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])

plt.plot(x,y,label = "折线图")
plt.bar(x,y,label = "柱形图")
plt.legend()
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
#显示图形
plt.show()


plt.plot(x,y,label = "折线图")
plt.bar(x,y,label = "柱形图")
#将图例设置到左上角
plt.legend(loc = "upper left")
plt.legend(loc = 2)
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
#显示图形
plt.show()

plt.plot(x,y,label = "折线图")
plt.bar(x,y,label = "柱形图")
#设置图例列数，默认为1列，更改为2列
plt.legend(ncol = 2)
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
#显示图形
plt.show()

