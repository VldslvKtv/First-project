import math
from matplotlib import pyplot as plt
from matplotlib import style


def decomposition(m, x):
    t = -1.0
    f = (((t ** (m + 1)) + 1) / (math.pi * m)) * (math.sin(m * x))  # am = 0
    return f


def f(m1, x1):
    res = 0.0
    for i in range(1, m1 + 1):
        res += decomposition(i, x1)
    return res


def value_check(arg):
    if (0 < arg < math.pi) or (2 * math.pi < arg < 3 * math.pi):
        return 1
    else:
        return 0


n = 100
a = 0.5
x0 = (3 * math.pi) / n
x = []
for i in range(2, n):
    x.append(x0 * i)
y = []
m = 10
for j in range(len(x)):
    y.append(a + f(m, x[j]))

max_razn = 0
for k in range(len(x)):
    if abs(value_check(x[k]) - y[k]) > max_razn:
        max_razn = abs(value_check(x[k]) - y[k])

print(f"Максимальная разность между значениями функции и при разложении в ряд Фурье: {max_razn}")

style.use('ggplot')
plt.plot(x, y, 'b', label='line one', linewidth=2)
plt.title('Fourier expansion')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.show()
