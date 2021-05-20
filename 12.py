"""
[Hard]

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time."""

"""
Okay let's try it with N = 3 and N = 5 and see if a pattern emerges
N = 3
1, 1, 1
2, 1
1, 2

N = 5
1, 1, 1, 1, 1
2, 1, 1, 1, 1
1, 2,

Okay that's pretty big so let's skip it for a sec and try the integer step case with those integers and N = 4:

1, 1, 1, 1
3, 1
1, 3

It occurs to me that it would be possible to define an N and X s.t. the stairs couldn't be climbed unless 1 is in X. Let's assume that 1 must be in X.

So the strategy is that you choose to advance a number of steps, and then consider the remainder of the steps.

You are standing at the staircase, you entertain all the possibilities in X, then reconsider those possibilities.
"""
def sol():
    m = []
    def func(n, x, prev):
        if n == 0:
             m.append(prev)
        else:
            for i in x:
                if i <= n:
                    func(n-i, x, prev+[i])
    len(func(6, [1,2,3,5], [])) #Oh I read this wrong because Johnny called me in the middle of it, and I need to return the count, not the possibilities themselves. Whatever, trivial to modify this...


sol()
