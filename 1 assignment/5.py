import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2 - 2 * x


def false_position(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")

    errors = []
    iterations = []
    for i in range(max_iter):
        c = b - (func(b) * (b - a)) / (func(b) - func(a))
        absolute_error = abs(func(c))
        relative_error = abs((b - a) / c) if c != 0 else np.inf

        # Store errors and iterations
        errors.append(absolute_error)
        iterations.append((i + 1, c, absolute_error, relative_error))

        # Check for convergence
        if absolute_error < tol:
            return c, func(c), iterations, errors

        # Update the interval
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

    raise ValueError("False Position Method did not converge within the maximum number of iterations.")



a, b = 0, 3
tol = 1e-6
max_iter = 100

try:
    root, f_at_root, iteration_data, errors = false_position(f, a, b, tol, max_iter)
    print("\nIteration Table:")
    print(f"{'Iteration':<10}{'Root Approx.':<15}{'Abs. Error':<15}{'Rel. Error':<15}")
    for iter_num, approx_root, abs_err, rel_err in iteration_data:
        print(f"{iter_num:<10}{approx_root:<15.6f}{abs_err:<15.6e}{rel_err:<15.6e}")

    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(errors) + 1), errors, marker='o', label="Absolute Error")
    plt.yscale('log')
    plt.title("Convergence of False Position Method", fontsize=14)
    plt.xlabel("Iteration Number", fontsize=12)
    plt.ylabel("Absolute Error (log scale)", fontsize=12)
    plt.grid()
    plt.legend()
    plt.show()

    print("\nFinal Results:")
    print(f"Root: {root}")
    print(f"f(root): {f_at_root}")
    print(f"Absolute Error: {errors[-1]}")

except ValueError as e:
    print(f"Error: {e}")
