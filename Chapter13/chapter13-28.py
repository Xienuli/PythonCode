# _*_ coding: utf-8 _*_
"""
Time:     2023/6/3 0:17
Author:   Xienuli
File:     chapter13-28.py
"""
#绘制箱型图
import matplotlib.pyplot as plt
import numpy as np

#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标系
plt.subplot(1,1,1)
#指明x值
y1 = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])
y2 = np.array([433,1167,2855,3241,3060,802,1906,2214,2315])
x = [y1,y2]
#绘图
labels = ["注册人数","激活人数"]
plt.boxplot(x,labels = labels,vert = True,widths = [0.2,0.5])
#设置标题
plt.title("XXX公司1—9月注册与激活人数",loc = "center")
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart11.svg')