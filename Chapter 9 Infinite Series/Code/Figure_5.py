import numpy as np
import matplotlib.pyplot as plt

# 计算前n个和
def partial_sum(n):
    return np.cumsum(1/np.arange(1, n+1))

# 设置绘图参数
fig, ax = plt.subplots()
ax.plot(partial_sum(100), label='Partial Sum')
ax.hlines(1, 0, 100, color='r', linestyle='--', label='Actual Sum')
ax.legend()

# 显示图形
plt.show()
