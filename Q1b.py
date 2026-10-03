# ESO208 Computational Methods in Engineering
# Assignment 7
# Question 1(b): Simpson's Rule
# Combination of Simpson's 1/3 and 3/8 rules

# Given data
y = [0, 2, 4, 6, 8, 10, 12, 14]

H = [0, 1, 1.5, 3, 3.5, 3.2, 2, 0]

U = [0, 0.1, 0.12, 0.2, 0.25, 0.3, 0.15, 0]

# Calculate H(y)U(y)
HU = []

for i in range(len(y)):
    HU.append(H[i] * U[i])


# Simpson's 1/3 rule
def simpson_one_third(x, f):
    n = len(x) - 1
    h = x[1] - x[0]

    integral = f[0] + f[n]

    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * f[i]
        else:
            integral += 4 * f[i]

    return (h / 3) * integral


# Simpson's 3/8 rule
def simpson_three_eighth(x, f):
    n = len(x) - 1
    h = x[1] - x[0]

    integral = f[0] + f[n]

    for i in range(1, n):
        if i % 3 == 0:
            integral += 2 * f[i]
        else:
            integral += 3 * f[i]

    return (3 * h / 8) * integral


# There are 7 intervals.
# Use Simpson's 3/8 rule for the first 3 intervals
# and Simpson's 1/3 rule for the remaining 4 intervals.

A_38 = simpson_three_eighth(y[0:4], H[0:4])
A_13 = simpson_one_third(y[3:8], H[3:8])

Q_38 = simpson_three_eighth(y[0:4], HU[0:4])
Q_13 = simpson_one_third(y[3:8], HU[3:8])

# Total area and discharge
A = A_38 + A_13
Q = Q_38 + Q_13

# Average velocity
U_average = Q / A

print("Question 1(b) - Simpson's Rule")
print("--------------------------------")
print(f"Area using Simpson's 3/8 rule = {A_38:.6f} m^2")
print(f"Area using Simpson's 1/3 rule = {A_13:.6f} m^2")
print(f"Total cross-sectional area, A = {A:.6f} m^2")
print()
print(f"Discharge using Simpson's 3/8 rule = {Q_38:.6f} m^3/s")
print(f"Discharge using Simpson's 1/3 rule = {Q_13:.6f} m^3/s")
print(f"Total discharge, Q = {Q:.6f} m^3/s")
print()
print(f"Average velocity, U_bar = {U_average:.6f} m/s")