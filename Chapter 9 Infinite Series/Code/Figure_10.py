import matplotlib.pyplot as plt

n = 50

u_n = [1/(n**2+1) for n in range(1, n+1)]
sum_u_n = [sum(u_n[:i]) for i in range(1, n+1)]

v_n = [1/(n**2) for n in range(1, n+1)]
sum_v_n = [sum(v_n[:i]) for i in range(1, n+1)]

plt.plot(sum_u_n, label='Original series')
plt.plot(sum_v_n, label='Comparison series')

plt.legend()
plt.title("Partial sums of the series")
plt.xlabel("Number of terms")
plt.ylabel("Partial sum")
plt.show()
