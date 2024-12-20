import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 3*x + 2

def df(x):
    return 2*x - 3

def newton_raphson(func, dfunc, x0, tol, max_iter):
    iterations = []
    errors = []
    current_x = x0
    for i in range(max_iter):
        next_x = current_x - func(current_x) / dfunc(current_x)
        absolute_error = abs(next_x - current_x)
        relative_error = absolute_error / abs(next_x) if next_x != 0 else np.inf
        iterations.append((i + 1, current_x, absolute_error, relative_error))
        errors.append(absolute_error)
        if absolute_error < tol:
            break
        current_x = next_x
    return iterations, errors

x0 = 2.5
tol = 1e-6
max_iter = 50

iterations, errors = newton_raphson(f, df, x0, tol, max_iter)

table = [["Iteration", "Current Guess", "Absolute Error", "Relative Error"]]
table += [[i, f"{x:.6f}", f"{abs_err:.6e}", f"{rel_err:.6e}"] for i, x, abs_err, rel_err in iterations]

plt.figure(figsize=(8, 6))
plt.plot(range(1, len(errors) + 1), errors, marker='o', label="Absolute Error")
plt.yscale('log')
plt.title("Convergence of Newton-Raphson Method", fontsize=14)
plt.xlabel("Iteration Number", fontsize=12)
plt.ylabel("Absolute Error (log scale)", fontsize=12)
plt.grid()
plt.legend()
plt.show()

table, len(errors)
