import numpy as np


def neville(x, y, x_int):
    """
    Interpolates a value using Neville polynomial
    Parameters:
            x: Array containing x values
            y: Array containing y values
        x_int: Value to interpolate
    Returns:
        y_int: Interpolated value
            q: Coefficients matrix
    """

    n = x.size
    q = np.zeros((n, n - 1))
    # Insert 'y' in the first column of the matrix 'q'
    q = np.concatenate((y[:, None], q), axis=1)

    for i in range(1, n):
        for j in range(1, i + 1):
            print(f'q[{i},{j}] = (({x_int}-{x[i-j]})*{q[i, j - 1]} - {(x_int - x[i])} * {q[i - 1, j - 1]}) / {(x[i] - x[i - j])})')
            q[i, j] = ((x_int - x[i - j]) * q[i, j - 1] -
                       (x_int - x[i]) * q[i - 1, j - 1]) / (x[i] - x[i - j])
            

    y_int = q[n - 1, n - 1]
    return [y_int, q]



x = np.array([1.2, 1.3, 1.4, 1.5, 1.6])
y = np.array([3.5095, 3.6984, 3.9043, 4.1293, 4.3756])
x_int = 1.37

print("x", x)
print("y", y)
print("f(x)", x_int)
[y_int, q] = neville(x, y, x_int)

print(q)
print("result:", y_int)
