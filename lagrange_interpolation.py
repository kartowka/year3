import numpy as np


def lagrange(x, y, x_int):
    """
    Interpolates a value using Lagrange polynomial
    Parameters:
            x: Array containing x values
            y: Array containing y values
        x_int: Value to interpolate
    Returns:
        y_int: Interpolated value
    """

    n = x.size
    y_int = 0
    num_of_iteration = 0
    for i in range(0, n):
        p = y[i]
        for j in range(0, n):
            if i != j:
                print(f'p = {p}*{(x_int - x[j])}/{(x[i] - x[j])}')
                p = p * (x_int - x[j]) / (x[i] - x[j])
            num_of_iteration+=1
        print(f'f`(x) = {y_int}+{p}, iteration No.: {num_of_iteration}')        
        y_int = y_int + p
        num_of_iteration+=1
    return [y_int]

x = np.array([1.2, 1.3, 1.4, 1.5, 1.6])
y = np.array([3.5095, 3.6984, 3.9043, 4.1293, 4.3756])
x_int = 1.37
print("x", x)
print("y", y)
print("f(x)", x_int)
[y_int] = lagrange(x, y, x_int)
print(f"the interpolated value at {x_int} is: {y_int}")