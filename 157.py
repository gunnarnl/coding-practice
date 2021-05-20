"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

"""
Solution: A palindrome may only have one character without a pair, the center character. Any string that has more than one character with an odd number of instances is unable to be a palindrome. The solution, then, is just to get the counts of each character in the string and check if more than one count is odd.
"""
from collections import Counter

def solution(l):
    counts = Counter(l) #returns dictionary of counts of each item in l
    odds = [counts[k] for k in counts if not is_even(counts[k])]
    if len(odds) > 2:
        return False
    else:
        return True

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

s1 = "carrace"
s2 = "daily"

print(solution(s1))
print(solution(s2))
