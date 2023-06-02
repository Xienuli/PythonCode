# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 23:29
Author:   Xienuli
File:     chapter13-27.py
"""
#绘制雷达图
import matplotlib.pyplot as plt
import numpy as np

#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立坐标系
plt.subplot(111,polar = True)#参数polar等于True表示建立一个极坐标系
dataLenth = 5#把整个圆均分成5份
#np.linespace表示在指定的间隔内返回均匀间隔的数字
angles = np.linspace(0,2 * np.pi,dataLenth,endpoint = False)
labels = ['沟通能力','业务理解能力','逻辑思维能力',
          '快速学习能力','工具使用能力']
data = [2,3.5,4,4.5,5]
data = np.concatenate((data, [data[0]]))#闭合
angles = np.concatenate((angles,[angles[0]]))#闭合
#绘图
plt.polar(angles,data,color = 'r', marker = 'o')
#设置x轴刻度
plt.xticks(angles[:-1],labels)#为了避免xticks()中的刻度数与标签数不一致，此处将设置刻度的函数改为plt.xticks(angles[:-1], labels)。
#设置标题
plt.title(label = "某数据分析师的综合评级")
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart10.svg')
