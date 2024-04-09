import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from pylab import mpl
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 读取数据
data = pd.read_csv(r"D:\桌面管理\大三下学期\数据可视化\实验4\birthrate.csv", delimiter=',')

# 提取2018年出生率数据列
birthrates_2018 = data.iloc[:, 56].dropna()  # Python中索引是从0开始的，所以第57列对应索引是56

# 绘制直方图和密度图
plt.figure()
plt.hist(birthrates_2018, density=True, bins=np.arange(0, 51, 0.5), alpha=0.5)  # 设置柱宽为0.5
# 拟合正态分布
mu, std = norm.fit(birthrates_2018)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'k', linewidth=2)
plt.xlabel('出生率')
plt.title('2018年出生率直方图和密度图')
plt.legend(['密度图', '直方图'])
plt.grid(True)
plt.show()
