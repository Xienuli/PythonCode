# _*_ coding: utf-8 _*_
"""
Time:     2023/6/3 1:43
Author:   Xienuli
File:     chapter13-34.py
"""
import matplotlib.pyplot as plt
import numpy as np

#折线图+柱形图
#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#建立一个坐标轴
plt.subplot(1,1,1)
#指明x和y的值
x = np.array([1,2,3,4,5,6,7,8,9])
y1 = np.array([866,2335,5710,
               6482,6120,1605,
               3813,4428,4631])
y2 = np.array([433,1167,2855,
               3241,3060,802,
               1906,2214,2315])
#直接绘制折线图和柱形图
plt.plot(x,y1,color="k",linestyle ="solid",linewidth = 1,
         marker = "o", markersize = 3,label = "注册人数")
plt.bar(x,y2,color = "k",label = "激活人数")
#设置标题
plt.title("XXX公司1—9月注册与激活人数",loc = "center")
#添加数据标签
for a,b in zip(x,y1):
    plt.text(a,b,b,ha = 'center', va = 'bottom', fontsize = 11)
for a,b in zip(x,y2):
    plt.text(a,b,b,ha = 'center', va = 'bottom', fontsize = 11)
#设置x轴和y轴名称
plt.xlabel('月份')
plt.ylabel('注册量')
#设置x轴和y轴的刻度
plt.xticks(np.arange(1,10,1),["1月份","2月份","3月份",
                               "4月份","5月份","6月份",
                               "7月份","8月份","9月份",])
plt.yticks(np.arange(1000,7000,1000),
           ["1000人","2000人","3000人",
            "4000人","5000人","6000人"])
#设置图例
plt.legend()
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart16.svg')