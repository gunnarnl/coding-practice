"""
[Medium]
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time

def scheduler(f, n):
    m = n / 1000
    time.sleep(m)
    return f()

def test():
    return print("Hello!")

scheduler(test, 50)

#Am I missing something?
