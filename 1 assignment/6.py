import math
def g(x):
    return (6 * x - 5) / x

true_root = 1

x0 = 0.5

iterations = 10

x_values = [x0]
errors = []

for i in range(iterations):
    x_next = g(x_values[-1])
    x_values.append(x_next)
    error = abs(x_next - true_root)
    errors.append(error)

for i in range(iterations):
    print(f"Iteration {i + 1}: x = {x_values[i + 1]:.6f}, Absolute Error = {errors[i]:.6f}")

if abs(g(1) - 1) < 1:
    print("\nThe iteration method converges to the root.")
else:
    print("\nThe iteration method does not converge to the root.")
