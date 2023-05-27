import numpy as np
import matplotlib.pyplot as plt

def function(a, b, n, x):
    y = 0
    for k in range(n+1):
        y += a**k * np.cos(b**k * np.pi * x)
    return y

# 设置参数值
a = 0.9
b = 2
n = 10

# 设置 x 范围
x = np.linspace(-5, 5, 1000)

# 计算函数值
y = function(a, b, n, x)

# 绘制图像
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y')
plt.grid(True)
plt.show()
