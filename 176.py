"""
[easy]
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

#So I'm determining if there's a function from characters to characters?

def solution(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        pairs = set(zip(s1, s2))
        dom, codom = zip(*pairs)
        if len(dom) == len(set(dom)):
            return True
        else:
            return False

s1 = "foo"
s2 = "bar"
s3 = "abc"
s4 = "bcd"

print(solution(s1, s2))
print(solution(s3, s4))
