# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one at i.
# Solve it without using division and in O(n).
#
# Example:
#
#     >>> coding_problem_02([1, 2, 3, 4, 5])
#     [120, 60, 40, 30, 24]

import numpy as np

def fun(ls):
    ln = len(ls)
    rn = [ls[:i]+ls[i+1:] for i in range(0, ln)]
    new = []
    # for i in rn:
    #     new.append(np.prod(i))
    # return new
    #Nope, faster:
    return list(map(lambda x: np.prod(x), rn))

print(fun([1, 2, 3, 4, 5]))
print(fun([1, 3, 6]))
