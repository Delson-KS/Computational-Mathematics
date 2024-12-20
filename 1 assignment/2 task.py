import numpy as np
from scipy.optimize import root_scalar

def f(x):
    return np.exp(x) - 2 * x - 3

def bisection_method(func, a, b, tol, max_iter):
    iterations = 0
    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            return c, iterations
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return (a + b) / 2, iterations

def secant_method(func, x0, x1, tol, max_iter):
    iterations = 0
    while abs(x1 - x0) > tol and iterations < max_iter:
        f_x0 = func(x0)
        f_x1 = func(x1)
        x_temp = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x_temp
        iterations += 1
    return x1, iterations

a, b = 0, 2
tol = 1e-6
max_iter = 1000

exact_root_result = root_scalar(f, bracket=[a, b], method="brentq")
exact_root = exact_root_result.root

bisection_root, bisection_iterations = bisection_method(f, a, b, tol, max_iter)
bisection_relative_error = abs(bisection_root - exact_root) / abs(exact_root)

secant_root, secant_iterations = secant_method(f, a, b, tol, max_iter)
secant_relative_error = abs(secant_root - exact_root) / abs(exact_root)

print( bisection_iterations, bisection_relative_error, secant_root, secant_iterations, secant_relative_error, exact_root)
