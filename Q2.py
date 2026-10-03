# ESO208 Computational Methods in Engineering
# Assignment 7
# Question 2(a): Romberg Integration

import math


# Flow rate function
def Q(t):
    return 8 + 5 * math.cos(0.4 * t) ** 2


# Concentration function
def c(t):
    return 5 * math.exp(-0.5 * t) + 3 * math.exp(0.15 * t)


# Integrand: Q(t) * c(t)
def f(t):
    return Q(t) * c(t)


# Romberg integration
def romberg_integration(a, b, tolerance=0.1, max_order=20):

    R = []

    # First trapezoidal approximation
    h = b - a
    R.append([h * (f(a) + f(b)) / 2])

    print("Romberg Integration")
    print("-------------------")
    print(f"R[0,0] = {R[0][0]:.10f}")

    for k in range(1, max_order):

        # Number of subintervals
        n = 2 ** k

        # Step size
        h = (b - a) / n

        # New points introduced at this level
        new_points = 0.0

        for i in range(1, 2 ** (k - 1) + 1):
            x = a + (2 * i - 1) * h
            new_points += f(x)

        # Trapezoidal approximation
        R_k0 = R[k - 1][0] / 2 + h * new_points

        current_row = [R_k0]

        # Richardson extrapolation
        for j in range(1, k + 1):
            value = current_row[j - 1] + (
                current_row[j - 1] - R[k - 1][j - 1]
            ) / (4 ** j - 1)

            current_row.append(value)

        R.append(current_row)

        # Approximate relative error
        approximate_error = abs(
            (current_row[k] - R[k - 1][k - 1])
            / current_row[k]
        ) * 100

        print(f"R[{k},{k}] = {current_row[k]:.10f}"
              f"    Approx. error = {approximate_error:.6f}%")

        # Stop when tolerance is satisfied
        if approximate_error < tolerance:
            break

    return current_row[k], approximate_error, R


# Limits of integration
t1 = 2
t2 = 8

# Required tolerance = 0.1%
tolerance = 0.1

# Perform Romberg integration
mass, error, R = romberg_integration(t1, t2, tolerance)

print()
print("Final Result")
print("------------")
print(f"Mass transported, M = {mass:.10f} mg")
print(f"Approximate relative error = {error:.6f}%")