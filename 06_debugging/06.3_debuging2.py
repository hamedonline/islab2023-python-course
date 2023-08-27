# debugging example
import math


def power_2_func(x):
    return math.pow(x, 2)


a = []
b = []

for i in range(0, 5):
    a.append(i ** 2)
    b.append(int(power_2_func(i)))

print(a)
print(b)
