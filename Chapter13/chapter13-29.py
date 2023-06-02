# _*_ coding: utf-8 _*_
"""
Time:     2023/6/3 0:26
Author:   Xienuli
File:     chapter13-29.py
"""
#绘制饼图
import matplotlib.pyplot as plt
import numpy as np

#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标系
plt.subplot(1,1,1)
#指明x值
x = np.array([8566,5335,7310,6482])
labels = ["东区","北区","南区","西区"]
explode = [0.05,0,0,0]#让第一块离圆心远一点
labeldistance = 1.1
plt.pie(x,labels = labels,autopct = '%.0f%%', shadow = True,explode = explode,radius = 1.0,labeldistance = labeldistance)
#设置标题
plt.title("全国各区域任务占比",loc = "center")
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart12.svg')