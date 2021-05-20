"""
[easy]
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""
import random

def rand7():
    return random.randint(1,7)

def rand5():
    return getint5(rand7())

def getint5(int):
    if int > 5:
        print("Uh oh: "+str(int))
        return getint5(rand7())
    else:
        return int

print(rand5())
