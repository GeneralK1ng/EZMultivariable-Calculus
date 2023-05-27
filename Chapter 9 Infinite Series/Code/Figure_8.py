import matplotlib.pyplot as plt
import numpy as np

n = 100 # 序列长度
u = (-1) ** np.arange(1, n+1) / np.arange(1, n+1) # 收敛级数
a = 0.5 # 常数
w = a * u # 计算a * u_n

# 计算部分和
sum_u = np.cumsum(u)
sum_w = np.cumsum(w)

# 绘制图形
plt.plot(sum_u, label='u')
plt.plot(sum_w, label='au')
plt.legend()
plt.show()

