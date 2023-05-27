import matplotlib.pyplot as plt
import numpy as np

n = 100 # 序列长度
u = (-1) ** np.arange(1, n+1) / np.arange(1, n+1) # 收敛级数
v = 1/np.arange(1, n+1)**2 # 幂级数
w1 = u + v # 计算u_n + v_n
w2 = u - v # 计算u_n - v_n

# 计算部分和
sum_u = np.cumsum(u)
sum_v = np.cumsum(v)
sum_w1 = np.cumsum(w1)
sum_w2 = np.cumsum(w2)

# 绘制图形
plt.plot(sum_u, label='u')
plt.plot(sum_v, label='v')
plt.plot(sum_w1, label='u+v')
plt.plot(sum_w2, label='u-v')
plt.legend()
plt.show()



