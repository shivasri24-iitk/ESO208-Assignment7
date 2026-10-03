# ESO208 Computational Methods in Engineering
# Assignment 7
# Question 1(a): Trapezoidal Rule

# Given data
y = [0, 2, 4, 6, 8, 10, 12, 14]

H = [0, 1, 1.5, 3, 3.5, 3.2, 2, 0]

U = [0, 0.1, 0.12, 0.2, 0.25, 0.3, 0.15, 0]

# Calculate H(y)U(y)
HU = []

for i in range(len(y)):
    HU.append(H[i] * U[i])

# Trapezoidal rule
def trapezoidal(x, f):
    integral = 0.0

    for i in range(len(x) - 1):
        h = x[i + 1] - x[i]
        integral += h * (f[i] + f[i + 1]) / 2

    return integral


# Cross-sectional area
A = trapezoidal(y, H)

# Discharge
Q = trapezoidal(y, HU)

# Average velocity
U_average = Q / A

print("Question 1(a) - Trapezoidal Rule")
print("---------------------------------")
print(f"Cross-sectional area, A = {A:.6f} m^2")
print(f"Discharge, Q = {Q:.6f} m^3/s")
print(f"Average velocity, U_bar = {U_average:.6f} m/s")