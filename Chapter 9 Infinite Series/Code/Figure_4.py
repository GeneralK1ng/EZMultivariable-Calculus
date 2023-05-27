import matplotlib.pyplot as plt

# 绘制大正方形
fig, ax = plt.subplots()
square = plt.Rectangle((0,0), 1, 1, fill=False)
ax.add_patch(square)

# 绘制小正方形
x = 0
y = 1
for i in range(8):
    size = 1 / 2**(i+1)
    x += size
    square = plt.Rectangle((x, y), -size, -1, fill=False)
    ax.add_patch(square)

# 设置图例和标题
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_aspect('equal')
ax.set_title(r'$\sum_{n=1}^{\infty} \frac{1}{2^n} = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$')

plt.show()
