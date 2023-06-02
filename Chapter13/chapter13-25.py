# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 22:34
Author:   Xienuli
File:     chapter13-25.py
"""
#绘制面积图
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标系
plt.subplot(1,1,1)
#指明x的值
x = np.array([1,2,3,4,5,6,7,8,9])
#指明y的值
y1 = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])
y2 = np.array([433,1167,2855,3241,3060,802,1906,2214,2315])
#绘图
labels = ["注册人数","激活人数"]#指明系列标签
plt.stackplot(x,y1,y2,labels = labels)
#设置标题
plt.title("XXX公司1—9月注册与激活人数",loc = "center")
#设置x轴和y轴名称
plt.xlabel('月份')
plt.ylabel('注册与激活人数')
#图例设置
plt.legend()
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart08.svg')