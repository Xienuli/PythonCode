# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 22:05
Author:   Xienuli
File:     chapter13-21.py
"""
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标系
plt.subplot(1,1,1)
#指明x的值
x = np.array(["东区","南区","西区","北区"])
#指明y的值
y1 = np.array([8566,6482,5335,7310])
y2 = np.array([4283,3241,2667,3655])
#绘图
plt.bar(x, y1, width = 0.3, label = "任务量")#柱形图的宽度相当于0.3
plt.bar(x, y2, width = 0.3, label = "完成量")#x+0.3相当于把完成量的每个柱子右移0.3
#设置标题
plt.title("全国各分区任务量和完成量",loc = 'center')#标题名及标题的位置
#添加数据标签
for a,b in zip(x,y1):
    plt.text(a, b, b, ha = 'center', va = 'bottom', fontsize = 12)
for a,b in zip(x,y2):
    plt.text(a, b, b, ha = 'center', va = 'top', fontsize = 12)
#设置x轴和y轴的名称
plt.xlabel('区域')
plt.ylabel('任务情况')
#设置x轴的刻度值
plt.xticks(x, ["东区", "南区", "西区", "北区"])
#图例设置
plt.legend(loc = "upper center", ncol = 2)
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart04.svg')