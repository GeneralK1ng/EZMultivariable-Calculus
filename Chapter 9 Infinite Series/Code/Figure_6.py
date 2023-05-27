import numpy as np
import matplotlib.pyplot as plt

# 绘制阶梯状图形
def plot_staircase(n):
    fig, ax = plt.subplots()
    x = np.arange(1, n+1)
    y = np.cumsum(1/x)
    ax.step(x, y, where='post', label='Staircase')
    
    # 绘制对数曲线
    x_log = np.linspace(1, n, 1000)
    y_log = np.log(x_log) + 1
    ax.plot(x_log, y_log, color='r', linestyle='--', label='Logarithmic Curve')
    
    # 设置图像参数
    ax.set_xlabel('n')
    ax.set_ylabel('Partial Sum')
    ax.set_title('Staircase Plot of Harmonic Series')
    ax.legend()
    
    # 显示图像
    plt.show()

# 测试
plot_staircase(1000000)
