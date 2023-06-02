# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 22:13
Author:   Xienuli
File:     chapter13-22.py
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
y = np.array([8566,6482,5335,7310])
#绘图
#width指明条形图的宽度，align指明条形图的位置，还可以选edge，默认是center
plt.barh(x, height = 0.5,width = y,align = "center")
#设置标题
plt.title("全国各分区任务量",loc = "center")
#添加数据标签
for a,b in zip(x,y):
    plt.text(b,a,b,ha = 'center', va = 'center',fontsize = 12)
#设置x轴和y轴的名称
plt.ylabel('区域')
plt.xlabel('任务量')
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart05.svg')


