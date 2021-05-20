"""
[medium]
This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""
"""
queue all elements but first, pop all elements back,
queue all elements but second, pop all elements back,
"""

def solution(stack):
    queue = []
    counter = 0
    while len(stack)>counter:
        for _ in range(len(stack)-counter-1):
            queue.append(stack.pop())
        for _ in range(len(queue)):
            stack.append(queue.pop(0))
        counter += 1
    return stack

s1 = [1,2,3,4,5]
s2 = [1,2,3,4]

print(solution(s1))
print(solution(s2))
