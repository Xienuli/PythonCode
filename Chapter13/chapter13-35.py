# _*_ coding: utf-8 _*_
"""
Time:     2023/6/3 1:46
Author:   Xienuli
File:     chapter13-35.py
"""
import matplotlib.pyplot as plt
import numpy as np
#绘制双坐标轴图表
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标轴
plt.subplot(1,1,1)
#指明x和y的值
x = np.array([1,2,3,4,5,6,7,8,9])
y1 = np.array([866,2335,5710,
               6482,6120,1605,
               3813,4428,4631])
y2 = np.array([0.54459448,0.32392354,0.39002751,
               0.41121879,0.32063077,0.33152276,
               0.92226226,0.02950071,0.15716906])
#绘制主坐标轴上的图表
plt.plot(x,y1,color = "k",linestyle = "solid", linewidth = 1,
         marker = "o", markersize = 3, label = "注册人数")
#设置x轴和y轴名称
plt.xlabel('月份')
plt.ylabel('注册量')
#设置主坐标图表的图例
plt.legend(loc = "upper left")
#调用twinx方法
plt.twinx()
#绘制次坐标轴的图表
plt.plot(x,y2,color = "k",linestyle = "dashdot", linewidth = 1,
         marker = "o", markersize = 3, label = "激活率")
#设置次x轴和y轴名称
plt.xlabel('月份')
plt.ylabel('激活率')
#设置主坐标图表的图例
plt.legend()
#设置标题
plt.title("XXX公司1—9月注册量与激活率",loc = "center")
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart17.svg')