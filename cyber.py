import matplotlib.pyplot as plt
import mplcyberpunk
import numpy as np
from matplotlib import cm
import matplotlib.font_manager as fm
from ridge_map import RidgeMap

plt.style.use("cyberpunk")

plt.plot([1, 3, 9, 5, 2, 1, 1], marker='o')
plt.plot([4, 5, 5, 7, 9, 8, 6], marker='o')

mplcyberpunk.add_glow_effects()

plt.show()

plt.style.use("cyberpunk")

# 数据
x = np.arange(-7, 7, 0.1)
y1 = np.sin(x)
y2 = np.sin(x) + x
y3 = np.sin(x) * x
y4 = np.sin(x) / x
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)

# 线条发光
mplcyberpunk.make_lines_glow()
# 面积图
mplcyberpunk.add_underglow()

plt.show()

# time
t = np.arange(0, 6.4, 0.1)
# frequency
f = 1
amplitudes = np.arange(-10, 11, 1)
# amplitude
A = [x * np.cos(f*t) for x in amplitudes]

# 设置颜色样式，cool、spring、winter、tab20、coolwarm
colormap_sect = np.linspace(0, 1, len(amplitudes))
colors = [cm.cool(x) for x in colormap_sect]

plt.rcParams['figure.figsize'] = [6, 4]
plt.style.use("cyberpunk")
plt.xlim(right=6.3)

for i in range(21):
    plt.plot(t, A[i], color=colors[i])
mplcyberpunk.make_lines_glow()

# 标题名，cool、spring、winter、tab20、coolwarm
plt.title("Colormap: 'coolwarm'")

plt.show()

# 中文显示
plt.rcParams['font.sans-serif'] = ['SimHei'] # Windows
plt.rcParams['font.sans-serif'] = ['Hiragino Sans GB'] # Mac
plt.rcParams['axes.unicode_minus'] = False

# 字体
font_prop = fm.FontProperties(fname="方正兰亭刊黑.ttf")

# 获取数据，此处需特殊技巧才能成功
rm = RidgeMap(bbox=(122.014, 25.344, 120.036, 21.902), font=font_prop)

# 设置线条数，朝向，以及其他属性
values = rm.get_elevation_data(num_lines=200, viewpoint='north')
values = rm.preprocess(values=values,
                       water_ntile=10,
                       vertical_ratio=240)

# 设置标题，线条颜色，背景颜色等
rm.plot_map(values, label="Taiwan", kind='gradient', line_color=plt.get_cmap('spring'), background_color='#212946')
plt.show()

