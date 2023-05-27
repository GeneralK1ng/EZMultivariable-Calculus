import matplotlib.pyplot as plt

def partial_sum(n):
    """
    计算前n项的部分和
    """
    s = 0
    for i in range(n+1):
        s += 1/(2**i)
    return s

# 计算前10项的部分和
n_vals = range(11)
s_vals = [partial_sum(n) for n in n_vals]

# 绘制部分和和级数的极限
plt.plot(n_vals, s_vals, label='partial sum')
plt.axhline(y=2, color='r', linestyle='--', label='limit')

plt.title('Illustration of Convergence of a Series')
plt.xlabel('n')
plt.ylabel('sum')
plt.legend()
plt.show()
