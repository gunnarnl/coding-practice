"""
[medium]
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# What are some other examples:
# 22226 = bbbbf, bwz, wwf, bwbf, wbz, wbbf
# okay so we can think about this as a lattice
# at the top are the indidual digit
# the next branches are the different cases where exactly two adjacent digits are joined
# then the branch of each of these joins two digits, and so on. So here, at the top would be 2,2,2,2,6; next would be a branch like 22, 2, 2, 2, 6; a branch from this would be 22, 22, 2, 6 and this would have 22, 22, 26 as a single branch. All of these are valid decoded messages.

#First let's write a function that takes lists of numbers (strings) and spits out a list of list of numbers with possible joins:

def joins_one(num):
    return [num[:x]+[num[x]+num[x+1]]+num[x+2:] for x in range(0,len(num)-1) if (len(num[x])==1 and len(num[x+1])==1)]

# what happens when this should apply vacuously?
# [22, 26]
# It returns an empty list! Perfect! This gives us a limiting case.

# Now we want to run this recursively over each of the subbranches
# Let's think about a very simple case (assuming we're dealing with lists of lists):
# [[2, 2, 6]]
# joins_one(l) = [[22,6], [2,26]]
# So we actually want to append these to what came before
# This will mean that there will be a lot of duplicates...
# Maybe a better way to do this would be to first append the first arg to a new list and apply joins_one and append those and so on.
# In certain cases there will be duplicates (it's a lattice), so in the end, we want a set.

def lattice(code):
    new = []
    def join_rec(num):
        if len(num) != 0:
            for l in num:
                new.append(l)
                join_rec(joins_one(l))
    join_rec([list(code)])
    return new

# then we a function to translate a list of numbers to characters. We can do all list at once with nested list comprehensions
def nums_to_codes(nums):
    return ["".join([chr(int(i)+96) for i in l]) for l in nums]

def main(code):
    poss_codes = lattice(code)
    return set(nums_to_codes(poss_codes))

print(main("1111"))
print(main("22226"))
