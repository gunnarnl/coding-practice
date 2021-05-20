"""
[Medium]
This problem was asked by Facebook.

A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

"""
Example:

N = 3, K = 3;

4, 2, 1
3, 6, 3
2, 3, 2

Minimum: 6

To solve this, we want to build rows incrementally, adding houses only when they don't match the color of the previous house. We can generate all possible rows and return the row with the minimum cost.
"""

def solution(arr):
    n = len(arr)
    k = len(arr[0])
    rows = [[]]
    def add_houses(rows, count=0):
        if count == n:
            #print("Final: "+str(rows))
            values = map(lambda x: sum(x[1]), map(lambda x: list(zip(*x)), rows))
            mini = min(list(values))
            return mini
        else:
            newrows = []
            for l in rows:
                for i,k in enumerate(arr[count]):
                    if len(l)==0:
                        newrows += [l+[(i,k)]]
                    elif i != l[count-1][0]:
                        newrows += [l+[(i,k)]]
            #print(newrows)
            return add_houses(newrows, count+1)
    print(add_houses(rows))

arr = [[4, 2, 1],[3, 6, 3],[2, 3, 2]]

solution(arr)
