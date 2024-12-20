import numpy as np


def f(x):
    return x ** 3 + x ** 2 + x + 1


def mullers_method(func, x0, x1, x2, tol=1e-6, max_iter=100):
    print("Starting Muller's Method:")
    for iteration in range(max_iter):
        h1, h2 = x1 - x0, x2 - x1
        delta1 = (func(x1) - func(x0)) / h1
        delta2 = (func(x2) - func(x1)) / h2

        a = (delta2 - delta1) / (h2 + h1)
        b = a * h2 + delta2
        c = func(x2)

        discriminant = b ** 2 - 4 * a * c
        root_part = np.sqrt(discriminant) if discriminant >= 0 else np.sqrt(complex(discriminant))

        denominator = b + root_part if abs(b + root_part) > abs(b - root_part) else b - root_part
        if abs(denominator) < 1e-12:  # Handle potential division by zero
            raise ValueError(f"Unstable denominator encountered at iteration {iteration + 1}.")

        dx = -2 * c / denominator
        x3 = x2 + dx

        # Print debug information
        print(f"Iteration {iteration + 1}: x3 = {x3}, f(x3) = {func(x3)}, dx = {dx}")

        # Check for convergence
        if abs(dx) < tol:
            print(f"Converged to root {x3} after {iteration + 1} iterations.")
            return x3, func(x3)

        # Update points for next iteration
        x0, x1, x2 = x1, x2, x3

    raise ValueError("Muller's method did not converge within the maximum number of iterations.")


x0, x1, x2 = -1, 0, 1

tol = 1e-6
max_iter = 100

try:
    root, f_at_root = mullers_method(f, x0, x1, x2, tol, max_iter)
    absolute_error = abs(f_at_root)

    print("\nResults:")
    print(f"Root: {root}")
    print(f"f(root): {f_at_root}")
    print(f"Absolute Error: {absolute_error}")
except ValueError as e:
    print(f"Error: {e}")
