# _*_ coding: utf-8 _*_
"""
Time:     2023/6/3 0:41
Author:   Xienuli
File:     chapter13-30.py
"""
#绘制圆环图
import matplotlib.pyplot as plt
import numpy as np

#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标系
plt.subplot(1,1,1)
#指明x值
x1 = np.array([8566,5335,7310,6482])
x2 = np.array([4283,2667,3655,3241])
labels = ["东区","北区","南区","西区"]
plt.pie(x1,labels = labels,radius = 1.0,
        wedgeprops = dict(width = 0.3,edgecolor= 'w'))
plt.pie(x2,radius = 0.7,wedgeprops = dict(width = 0.3,edgecolor = 'w'))
#添加注释
plt.annotate('完成量',xy = (0.35,0.35),xytext = (0.7,0.45),
             arrowprops = dict(facecolor = 'black',arrowstyle = '->'))
plt.annotate('完成量',xy = (0.75,0.20),xytext = (1.1,0.2),
             arrowprops = dict(facecolor = 'black',arrowstyle = '->'))
#设置标题
plt.title("全国各区域任务量与完成量占比",loc = "center")
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart13.svg')