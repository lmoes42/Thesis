# This script takes two integers p and q, and plots a subset of
# the points{(x,y) : y^2 = x^3 + px + q, |x| < 10, |y| < 10}
# on the elliptic curve y^2 = x^3 + px + q

# Get the required libraries
import matplotlib.pyplot as plt
import numpy as np

# Constants for our elliptic curve
p, q, r = 1, 1, 1

# The points we will be computing
y, x = np.ogrid[-5:5:100j, -5:5:100j]

# Find the points satisfying this elliptic curve
plt.contour(
    x.ravel(),
    y.ravel(),
    pow(y, 2) - (pow(x, 3) + p * pow(x, 2) + q * x + r),
    [0]
)
plt.show()
