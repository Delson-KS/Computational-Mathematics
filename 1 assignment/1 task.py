import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

def f(x):
    return x**3 - 2*x**2 - 5

x = np.linspace(1, 4, 500)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x³ - 2x² - 5", color="blue")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.axvline(0, color="black", linestyle="--", linewidth=0.8)
plt.title("Graph of f(x) = x³ - 2x² - 5", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("f(x)", fontsize=12)
plt.grid()
plt.legend()
plt.show()

approx_root = 2.5  # Approximate root around this value from visual inspection

approx_root_value = f(approx_root)

exact_root_result = root_scalar(f, bracket=[1, 4], method="brentq")
exact_root = exact_root_result.root

absolute_error = abs(exact_root - approx_root)

approx_root, approx_root_value, exact_root, absolute_error

