import numpy as np
import matplotlib.pyplot as plt


def partial_sum(n):
    """
    计算前n项的部分和
    """
    s = 0
    for i in range(1, n+1):
        s += 1/(i**2)
    return s


# 计算前1000项的部分和
n_vals = range(1, 1001)
s_vals = [partial_sum(n) for n in n_vals]

# 绘制部分和和级数的极限
plt.plot(n_vals, s_vals, label='partial sum')
plt.axhline(y=(np.pi**2)/6, color='r', linestyle='--', label='limit')

plt.title('Illustration of Convergence of a Series')
plt.xlabel('n')
plt.ylabel('sum')
plt.legend()
plt.show()
