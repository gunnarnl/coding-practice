"""
[easy]
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

"""
move through the length of the string, open brackets add 1 of the type, while closed brackets subtract 1 of the type. End result should be 0 for all
"""

def solution(s):
    pbracket = 0
    cbracket = 0
    sbracket = 0
    for c in s:
        if pbracket<0 or cbracket<0 or sbracket<0:
            return False
        if c=="[":
            sbracket+=1
        elif c=="(":
            pbracket+=1
        elif c=="{":
            cbracket+=1
        elif c=="]":
            sbracket-=1
        elif c==")":
            pbracket-=1
        elif c=="}":
            cbracket-=1
    return sbracket==pbracket==cbracket==0

s1 = "([])[]({})"
s2 = "([])[]{})"
print(solution(s1))
print(solution(s2))
