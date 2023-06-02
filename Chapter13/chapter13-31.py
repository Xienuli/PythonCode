# _*_ coding: utf-8 _*_
"""
Time:     2023/6/3 1:03
Author:   Xienuli
File:     chapter13-31.py
"""
#绘制热力图
import itertools
import matplotlib.pyplot as plt
import numpy as np

#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#解决负号无法正常显示的问题
plt.rcParams["axes.unicode_minus"] = False
#几个相关指标之间的相关性
cm = np.array([[1,0.082,0.031,-0.0086],
              [0.082,1,-0.09,0.062],
              [0.031,-0.09,1,0.026],
              [-0.0086,0.062,0.026,1]])
cmap = plt.cm.cool#设置配色方案
plt.imshow(cm,cmap = cmap)
plt.colorbar()#显示右边的颜色条
#设置x轴和y轴的刻度标签
classes = ["负债率","信贷数量","年龄","家属数量"]
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)

#将数值显示在指定位置
for i,j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
    plt.text(j, i, cm[i,j],horizontalalignment = "center")
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart14.svg')
