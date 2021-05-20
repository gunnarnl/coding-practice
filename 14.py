"""
[Medium]
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""

# Okay the idea here is that we are trying to estimate pi by seeing if a pair of x, y coordinates fall within a simple circle with radius 1.
#
# First, some math: assume r = 1, then the set of points within the circle are all those such that x^2 + y^2 <= 1
#
# Since pi is effectively the area of the circle in a 2x2 grid, if we generate a number of points in such a grid, we can estimate pi by taking the number of points that are in the circle over the number of points within the the entire square, this would mirror the ratio of circle area to square area. We then multiply by 4 to get Our Pi.

# The more samples we use, the more accurate our estimation of pi

from random import random
from random import seed

#seed(12)

samples = 10000
grange = lambda x: -1 + (x * 2) #to ensure the random number is between -1 and 1
points = [(grange(random()), grange(random())) for _ in range(samples)]

in_circ = len(list(filter((lambda x: x[0]**2+x[1]**2 <= 1), points)))
our_pi = 4 * (in_circ / len(points))

print(our_pi)
