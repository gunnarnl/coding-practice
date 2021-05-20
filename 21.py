"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

"""
We'd probably want to know first of all what the bounds of these intervals really are. That is are the bounds inclusive or exclusive?

Let's assume they're inclusive.

Then it's clear that what we're actually after is the highest number of classes that overlap at once.
"""

def solution(arr):
    #okay so one way to do this would be click "on" (+1) when a class starts and "off" (-1) when it stops, and then record the highest result.
    uarr = list(zip(*arr))
    start = [(t, 1) for t in uarr[0]]
    end = [(t, -1) for t in uarr[1]]
    #then we just iterate through a sorted version of the combined list, adding the second element of the array in each case and recording the high.
    count = 0
    high = 0
    for x in sorted(start+end):
        count += x[1]
        if count > high:
            high = count
    return high

print(solution([(30, 75), (0, 50), (60, 150)]))
