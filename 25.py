"""
[Hard]
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.
"""

"""
Regexes are just finite state automata, so I think this should precede the same way.

basically for each state, we can choose a way to procede according to the regex.
"""

# def problem(str, exp):
#     def state(str, exp):
#         if len(str)==0 and (len(exp)==0 or :
#             return true
#         if len(str)==0 and exp[0]=
#         if len(exp)>1
#             if exp[1] == '*' and (str[0]==exp[0] or exp[0]=='.'):
#                 return state(str[1:], reg)
#             elseif

#def solution(s, r):


def match(s, r):
    if len(s)==0:
        return False
    else:
        return s[0] == r[0] or (r[0]=='.' and len(s)>0)

def recurse(s, r):
    if r=='':
        return s==''

    if len(r)==1 or r[1] != '*':
        if match(s, r):
            return recurse(s[1:], r[1:])
        else:
            return False

    if r[1]=='*':
        if recurse(s, r[2:]):
            return True
        if match(s, r):
            return recurse(s[1:], r)
        else:
            return False

s1 = "ray"
s2 = "raymond"
r1 = "ra."
s3 = "chat"
s4 = "chats"
r2 = ".*at"

print("String '{}' returns {} for '{}'.".format(s1, str(recurse(s1, r1)), r1))
print("String '{}' returns {} for '{}'.".format(s2, str(recurse(s2, r1)), r1))
print("String '{}' returns {} for '{}'.".format(s3, str(recurse(s3, r2)), r2))
print("String '{}' returns {} for '{}'.".format(s4, str(recurse(s4, r2)), r2))
