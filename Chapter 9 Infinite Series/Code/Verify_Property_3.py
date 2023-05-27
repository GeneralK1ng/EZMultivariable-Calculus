import matplotlib.pyplot as plt

# define function to calculate infinite series


def infinite_series(n):
    sum = 0
    for i in range(1, n+1):
        sum += (-1)**(i+1) / i
    return sum


# plot original series
x_values = []
y_values = []

for n in range(1, 100):
    x_values.append(n)
    y_values.append(infinite_series(n))

plt.plot(x_values, y_values)
plt.xlabel('Number of terms')
plt.ylabel('Sum')
plt.title('Convergent infinite series')
plt.show()

# define function to calculate parenthesized series


def parenthesized_series(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 1:
            sum += 1 / (2*i-1)
        else:
            sum -= 1 / (2*i-1)
    return sum


# plot parenthesized series
x_values = []
y_values = []

for n in range(1, 100):
    x_values.append(n)
    y_values.append(parenthesized_series(n))

plt.plot(x_values, y_values)
plt.xlabel('Number of terms')
plt.ylabel('Sum')
plt.title('Parenthesized convergent series')
plt.show()
