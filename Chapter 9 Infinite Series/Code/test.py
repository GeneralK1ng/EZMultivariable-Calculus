import numpy as np
import matplotlib.pyplot as plt

def limit_function(x):
    numerator = x * np.sin(x) * np.cos(x) - x**2
    denominator = np.exp(x) * np.log(1 + x) + np.log(1 - x)
    return numerator / denominator

x = np.linspace(-1, 1, 1000)
y = limit_function(x)

plt.plot(x, y)
plt.axvline(x=0, color='red', linestyle='--')  # 在x=0处绘制红色虚线
plt.xlabel('x')
plt.ylabel('L')
plt.title(r'Graph of $L=\lim_{x\to 0}\frac{x\sin(x)\cos(x)-x^2}{e^x\ln(1+x)+\ln(1-x)}$')
plt.grid(True)
plt.show()
