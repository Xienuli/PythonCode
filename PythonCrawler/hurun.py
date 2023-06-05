import requests # 发送请求
import pandas as pd # 存入、读取excel数据
from time import sleep # 等待间隔时间，防止反爬
import random # 随机等待
import matplotlib.pyplot as plt # 画图
from wordcloud import WordCloud # 词云图

# 为解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决负号问题
plt.rcParams['axes.unicode_minus'] = False

# 创建空列表，用于存放爬取到的数据
Fullname_Cn_list = []  # 全名_中文
Fullname_En_list = []  # 全名_英文
Age_list = []  # 年龄
BirthPlace_Cn_list = []  # 出生地_中文
BirthPlace_En_list = []  # 出生地_英文
Gender_list = []  # 性别
Photo_list = []  # 照片
ComName_Cn_list = []  # 公司名称_中文
ComName_En_list = []  # 公司名称_英文
ComHeadquarters_Cn_list = []  # 公司总部地_中文
ComHeadquarters_En_list = []  # 公司总部地_英文
Industry_Cn_list = []  # 所在行业_中文
Industry_En_list = []  # 所在行业_英文
Ranking_list = []  # 排名
Ranking_Change_list = []  # 排名变化
Relations_list = []  # 组织结构
Wealth_list = []  # 财富值_人民币_亿
Wealth_Change_list = []  # 财富值变化
Wealth_USD_list = []  # 财富值_美元
Year_list = []  # 年份

# 循环爬取页面数据
for page in range(1, 8):
    sleep_seconds = random.uniform(1, 2)
    print('开始等待{}秒'.format(sleep_seconds))
    sleep(sleep_seconds)
    print('开始爬取第{}页'.format(page))
    offset = (page - 1) * 200
    url = 'https://www.hurun.net/zh-CN/Rank/HsRankDetailsList?num=AA777E5L&search=&offset={}&limit=200'.format(offset)
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'accept-encoding': 'gzip, deflate, br',
        'content-type': 'application/json',
        'referer': 'https://www.hurun.net/zh-CN/Rank/HsRankDetails?pagetype=rich'
    }
    r = requests.get(url, headers = headers)
    json_data = r.json()
    for item in json_data['rows']:
        Fullname_Cn_list.append(item['hs_Character'][0]['hs_Character_Fullname_Cn'])
        Fullname_En_list.append(item['hs_Character'][0]['hs_Character_Fullname_En'])
        Age_list.append(item['hs_Character'][0]['hs_Character_Age'])
        BirthPlace_Cn_list.append(item['hs_Character'][0]['hs_Character_BirthPlace_Cn'])
        BirthPlace_En_list.append(item['hs_Character'][0]['hs_Character_BirthPlace_En'])
        Gender_list.append(item['hs_Character'][0]['hs_Character_Gender_Lang'])
        Photo_list.append(item['hs_Character'][0]['hs_Character_Photo'])
        ComName_Cn_list.append(item['hs_Rank_Rich_ComName_Cn'])
        ComName_En_list.append(item['hs_Rank_Rich_ComName_En'])
        ComHeadquarters_Cn_list.append(item['hs_Rank_Rich_ComHeadquarters_Cn'])
        ComHeadquarters_En_list.append(item['hs_Rank_Rich_ComHeadquarters_En'])
        Industry_Cn_list.append(item['hs_Rank_Rich_Industry_Cn'])
        Industry_En_list.append(item['hs_Rank_Rich_Industry_En'])
        Ranking_list.append(item['hs_Rank_Rich_Ranking'])
        Ranking_Change_list.append(item['hs_Rank_Rich_Ranking_Change'])
        Relations_list.append(item['hs_Rank_Rich_Relations'])
        Wealth_list.append(item['hs_Rank_Rich_Wealth'])
        Wealth_Change_list.append(item['hs_Rank_Rich_Wealth_Change'])
        Wealth_USD_list.append(item['hs_Rank_Rich_Wealth_USD'])
        Year_list.append(item['hs_Rank_Rich_Year'])

# 创建DataFrame，将爬取到的数据存入其中
df = pd.DataFrame({
    '全名（中文）': Fullname_Cn_list,
    '全名（英文）': Fullname_En_list,
    '年龄': Age_list,
    '出生地（中文）': BirthPlace_Cn_list,
    '出生地（英文）': BirthPlace_En_list,
    '性别': Gender_list,
    '照片': Photo_list,
    '公司名称（中文）': ComName_Cn_list,
    '公司名称（英文）': ComName_En_list,
    '公司总部地（中文）': ComHeadquarters_Cn_list,
    '公司总部地（英文）': ComHeadquarters_En_list,
    '所在行业（中文）': Industry_Cn_list,
    '所在行业（英文）': Industry_En_list,
    '排名': Ranking_list,
    '排名变化': Ranking_Change_list,
    '组织结构': Relations_list,
    '财富值（人民币/亿）': Wealth_list,
    '财富值变化': Wealth_Change_list,
    '财富值（美元）': Wealth_USD_list,
    '年份': Year_list
})
# 保存结果数据
with pd.ExcelWriter('2022胡润百富榜.xlsx', engine = 'openpyxl') as writer:
	df.to_excel(writer, index = False, header = True)

# 读取excel
df = pd.read_excel('2022胡润百富榜.xlsx')
# 查看数据形状
print(df.shape)
# 查看前3名富豪
print(df.head(3))
# 查看后3名富豪
print(df.tail(3))
# 统计性描述
print(df.describe())

# 可视化分析
df_Wealth = df['财富值（人民币/亿）']
# 新建画布
plt.figure()
# 绘图
df_Wealth.plot.hist(figsize = (18, 6),grid = True,title = '财富分布-直方图')
# 保存图片
plt.savefig('财富分布-直方图.svg')
# 显示图片
plt.show()

# 剔出年龄未知的富豪
df_Age = df[df.年龄 != '未知']
# 数据切割，8个分段
df_Age_cut = pd.cut(df_Age.年龄.astype(float), bins = [20, 30, 40, 50, 60, 70, 80, 90, 100])
# 新建画布
plt.figure()
# 画柱形图
df_Age_cut.value_counts().plot.bar(figsize = (16, 8),title = '年龄分布-柱形图')
# 保存图片
plt.savefig('年龄分布-柱形图.svg')
# 显示图片
plt.show()

# 公司总部分布
df_ComHeadquarters = df['公司总部地（中文）'].value_counts()
# 新建画布
plt.figure()
# 绘图
df_ComHeadquarters.nlargest(n = 30).plot.bar(
    figsize = (16,10), # 图片大小
    grid = False, # 显示网格
    title = '公司总部分布Top30-柱形图' # 图片标题
)
# 保存图片
plt.savefig('公司总部分布Top30-柱形图.svg')
# 显示图片
plt.show()

# 性别分布
df_Gender = df['性别'].value_counts()
# 新建画布
plt.figure()
# 绘图
df_Gender.plot.pie(
    figsize = (8, 8),  # 图片大小
    legend = True,  # 显示图例
    autopct = '%1.2f%%', # 百分比格式
    title = '性别占比分布-饼图' # 图片标题
)
# 保存图片
plt.savefig('性别占比分布-饼图.svg')
# 显示图片
plt.show()

# 行业分布
df_Industry = df['所在行业（中文）'].value_counts()
# 新建画布
plt.figure()
# 绘图
df_Industry.nlargest(n = 20).plot.bar(
    figsize = (18, 10),# 图片大小
    grid = False,# 显示网格
    title = '行业分布Top20-柱形图'# 图片标题
)
# 保存图片
plt.savefig('行业分布Top20-柱形图.svg')
# 显示图片
plt.show()

# 词云图
ComName_list = df['公司名称（中文）'].values.tolist()
ComName_str = ''.join(ComName_list)
stopwords = [] # 停用词
wc = WordCloud(
    scale = 3, # 清晰度
    background_color = "white", # 背景颜色
    max_words = 1000, # 最大字符数
    width = 800, # 图宽
    height = 500, # 图高
    font_path = 'C:\Windows\Fonts\simhei.ttf', # 字体文件路径，根据实际情况替换
    stopwords = stopwords # 停用词
)
wc.generate_from_text(ComName_str) # 生成词云图
wc.to_file('2022年胡润百富榜_公司名称_词云图.png') # 保存图片
wc.to_image() # 显示图片

