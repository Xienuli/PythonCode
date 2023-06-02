# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 22:41
Author:   Xienuli
File:     chapter13-26.py
"""
#绘制树地图
import matplotlib.pyplot as plt
import numpy as np
import squarify

#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
#指定每一块的大小
size = np.array([3.4,0.693,0.585,
                 0.570,0.562,0.531,
                 0.530,0.524,0.501,
                 0.478,0.468,0.436])
#指定每一块的文字标签
xingzuo = np.array(["未知","摩羯座","天秤座",
                    "双鱼座","天蝎座","金牛座",
                    "处女座","双子座","射手座",
                    "狮子座","水瓶座","白羊座"])
#指定每一块的数值标签
rate = np.array(["34%","6.93%","5.85%",
                 "5.70%","5.62","5.31",
                 "5.30%","5.24%","5.01%",
                 "4.78%","4.68%","4.36%"])
#指定每一块的颜色
colors = ['steelblue','#9999ff','red','indianred',
          'green','yellow','orange']
#绘图
plot = squarify.plot(sizes = size,
                     label = xingzuo,
                     color = colors,
                     value = rate,
                     edgecolor = 'white',
                     linewidth = 3)
#设置标题大小
plt.title('菊粉星座分布', fontdict = {'fontsize': 12})
#去除坐标轴
plt.axis('off')
#去除上边框和有边框的刻度
plt.tick_params(top = 'off', right = 'off')
#显示图表
plt.show()
#保存图表到本地
plt.savefig('chart09.svg')