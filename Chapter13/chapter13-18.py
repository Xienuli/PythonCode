# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 21:19
Author:   Xienuli
File:     chapter13-18.py
"""
#图表注释
import matplotlib.pyplot as plt
import numpy as np
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标系
plt.subplot(1,1,1)
#指明x的值
x = np.array([1,2,3,4,5,6,7,8,9])
#指明y的值
y = np.array([866,2335,5710,6482,6120,1605,3813,4428,4631])
#绘图
plt.plot(x,y,color = 'k', linestyle = 'dashdot', linewidth = 1, marker = 'o',markersize = 5,label = "注册用户数")
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000","2000","3000","4000","5000","6000"])
#设置标题
plt.title(label = "XXX公司1-9月注册用户数",loc = "center")
#设置x轴和y轴的名称
plt.xlabel('月份')
plt.ylabel('注册量')
#设置x轴刻度
plt.xticks(np.arange(9) + 1,["1月份","2月份","3月份","4月份","5月份","6月份","7月份","8月份","9月份"])
#设置y轴刻度
plt.yticks(np.arange(1000,7000,1000),["1000人","2000人","3000人","4000人","5000人","6000人"])
#添加数据标签
for a,b in zip(x,y):
    plt.text(a,b,b,ha = 'center', va = 'bottom', fontsize = 10)
#设置网格线
plt.grid()
#图例设置
plt.legend()
#显示图形
plt.show()
#保存图表到本地
plt.savefig('chart01.svg')