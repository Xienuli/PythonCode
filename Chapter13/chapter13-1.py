# _*_ coding: utf-8 _*_
"""
Time:     2023/6/1 9:44
Author:   Xienuli
File:     chapter13-1.py
"""
#教材是使用的是IPython，PyCharm的默认解释器是Python，此章节代码均用Python解释器进行编译
import matplotlib.pyplot as plt

#用add_subplot函数建立坐标系
fig = plt.figure()
#给坐标系赋值
ax1 = fig.add_subplot(1,1,1)
#显示图形
plt.show()

#给fig重新赋值
fig = plt.figure()
#给第一个坐标系赋值
ax1 = fig.add_subplot(2,2,1)
#给第二个坐标系赋值
ax2 = fig.add_subplot(2,2,2)
#给第三个坐标系赋值
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
#显示图形
plt.show()


