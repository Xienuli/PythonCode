# _*_ coding: utf-8 _*_
"""
Time:     2023/6/2 17:40
Author:   Xienuli
File:     chapter13-17.py
"""
#数据表
import matplotlib.pyplot as plt
import numpy as np

#解决中文乱码问题
plt.rcParams["font.sans-serif"] = 'SimHei'
x = np.array(["东区","南区","西区","北区"])
y1 = np.array([8566,5335,7310,6482])
y2 = np.array([4283,2667,3655,3241])
#绘图
plt.bar(x,y1,width = 0.3, label = "任务量")
plt.bar(x,y2,width = 0.3, label = "完成量")
#设置标题
plt.title("全国各分区任务量和完成量",loc = "center")#标题名及标题位置
cellText = [[8566,5335,7310,6482],[4283,2667,3655,3241]]
#图例设置
plt.legend(loc = "upper center",ncol = 2)
rows = ["任务量","完成量"]
columns = ["东区","南区","西区","北区"]
plt.table(cellText = cellText,
          cellLoc = 'center',
          rowLabels = rows,
          rowColours = ["red","yellow"],
          rowLoc = "center",
          colLabels = columns,
          colColours = ["red","yellow","red","yellow"],
          colLoc = 'left',
          loc = 'bottom'
)
# 隐藏横坐标
plt.xticks([])
plt.show()