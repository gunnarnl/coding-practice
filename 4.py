"""
[Hard]
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def solution(ls):
    # All we care about is the positive integers in the array.
    nat = sorted(set(filter(lambda x: x>0, ls)))
    # then we get the length of the array and walk through it, checking if the integer is in the positive integers of the input, starting from the lowest positive integer. If not, return that number. To handle the limiting case (integers in the array are continuous and the lowest integer not in the array is +1 the highest integer), we also check for an integer 1 greater than the length of the list.
    return next((i for i in range(1,len(nat)+2) if i not in nat))

print(solution([3, 4, -1, 1]))
print(solution([1, 2, 0]))
