import numpy as np
import matplotlib.pyplot as plt

# 定义二元函数
def func(x, y):
    return x**2 + y**2

# 生成输入值的范围
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 计算函数值
Z = func(X, Y)

# 计算梯度
grad_x, grad_y = np.gradient(Z, x, y)

# 创建等高线图
fig, ax = plt.subplots()
contour = ax.contour(X, Y, Z, levels=20, cmap='viridis')

# 绘制梯度向量
skip = (slice(None, None, 5), slice(None, None, 5))  # 控制梯度箭头的密度
ax.quiver(X[skip], Y[skip], grad_x[skip], grad_y[skip], color='r')

# 添加颜色条
cbar = plt.colorbar(contour)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')

# 显示图形
plt.show()
