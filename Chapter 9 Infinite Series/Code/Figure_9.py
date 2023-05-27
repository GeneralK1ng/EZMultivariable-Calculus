import matplotlib.pyplot as plt

n = 50
p_values = [0.1, 0.5, 1, 1.5, 2, 3]
for p in p_values:
    u_n = [1/(i**p) for i in range(1, n+1)]
    sum_u_n = [sum(u_n[:i]) for i in range(1, n+1)]
    plt.plot(sum_u_n, label=f'p={p}')

plt.legend()
plt.title("Partial sums of the p-series")
plt.xlabel("Number of terms")
plt.ylabel("Partial sum")
plt.show()
