import matplotlib.pyplot as plt
import numpy as np

def partial_sum(n):
    """
    计算前n项的部分和
    """
    s = 0
    for i in range(1, n+1):
        s += ((-1)**(i+1))/i
    return s


# 计算前200项的部分和
n_vals = range(1, 201)
s_vals = [partial_sum(n) for n in n_vals]

# 绘制部分和和级数的极限
plt.plot(n_vals, s_vals, label='partial sum')
plt.axhline(y=np.log(2), color='r', linestyle='--', label='limit')

plt.title('Illustration of Convergence of a Series')
plt.xlabel('n')
plt.ylabel('sum')
plt.legend()
plt.show()
