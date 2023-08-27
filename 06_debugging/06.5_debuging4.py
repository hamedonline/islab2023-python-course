# debugging example

import math


def find_root(a, b, c):
    """
    return roots of equation ax^2 + bx + c = 0
    :param a: x^2 coefficient
    :param b: x^1 coefficient
    :param c: x^0 coefficient
    :return: available roots
    """

    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        disc = math.sqrt(d)
        root1 = (-b + disc) / (2 * a)
        root2 = (-b - disc) / (2 * a)
        return root1, root2
    else:
        return "This equation has no roots"


# ax^2 + bx + c = 0
a, b, c = 1, 2, -15
result = find_root(a, b, c)  # delta > 0
print(result)

# ax^2 + bx + c = 0
a, b, c = 1, 2, 1
result = find_root(a, b, c)  # delta = 0
print(result)

# ax^2 + bx + c = 0
a, b, c = 2, 1, 1
result = find_root(a, b, c)  # delta < 0
print(result)
