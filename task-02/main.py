import numpy as np
import random
from scipy.optimize import minimize_scalar
from scipy.integrate import quad


# Function to integrate
def f(x):
    return x**2

# Integration limits
a, b = 1, 2

# Define function max value on interval [a, b] 
res = minimize_scalar(lambda x: -f(x), bounds=(a, b), method='bounded')
f_max = f(res.x)

# Nr of random points
N = 500000

def is_inside(x, y):
    """Check if point (x, y) is inside a shape."""
    return y <= f(x)

# Generate random points
points = [(random.uniform(a, b), random.uniform(0, f_max)) for _ in range(N)]

# Count points under the curve
inside_points = [point for point in points if is_inside(point[0], point[1])]

# Monte Carlo method
monte_carlo_integral = (b - a) * f_max * (len(inside_points) / len(points))

# calculate the integral use 'quad' method
analytical_integral, _ = quad(f, a, b)

print("Значення інтеграла методом Монте-Карло:", monte_carlo_integral)
print("Значення інтеграла методом quad:", analytical_integral)
print("Похибка оцінки:", abs(monte_carlo_integral - analytical_integral))
