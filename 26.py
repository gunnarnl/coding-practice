"""
[medium]
This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def solution(head, k):
    phead, pk = head, head
    for _ in range(k):
        phead = phead.next
    prev = None
    while phead:
        prev = pk
        pk = pk.next
        phead = phead.next
    prev.next = pk.next
