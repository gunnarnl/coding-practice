"""
Given the root to a binary tree, implement serialize(root), which serializes the tree
into a string, and deserialize(s), which de-serializes the string back into the tree.
Example:
>>> serialize, deserialize = coding_problem_03()
>>> s = '3 2 1 None None None 4 5 None None 6 None None'
>>> tree = (3, (2, (1, None, None), None), (4, (5, None, None), (6, None, None)))
>>> isinstance(s, str)
True
>>> deserialized = deserialize(s)
>>> tree == deserialized
True
>>> s == serialize(deserialized)
True
Notes: the implementation below tries to solve the problem as intended.
However, one could instead: serialize, deserialize = lambda tree: repr(tree), lambda s: eval(s)
"""

"""
Here's the version from the email:
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# I guess the way to solve this is using recursion for serialization?
# We want to get to the root nodes and serialize upwards
# Let's start with a function "serialize" that takes binary trees and returns strings
# I'm going to assume values can't be None and values can't contain spaces

def serialize(tree):
    sl = ""
    sr = ""
    if tree.left != None:
        sl = serialize(tree.left)
    else:
        sl = str(tree.left)
    if tree.right != None:
        sr = serialize(tree.right)
    else:
        sr = str(tree.right)
    return str(tree.val)+" "+sl+" "+sr

# This fails because it treats the subsequent list incorrectly as a single constituent.
def deserialize(s):
    #first we need to find terminal nodes
    #I guess I'm going to do this by splitting the string into a list
    s2 = s.split(' ')
    # what we want to do is recursively build our trees up from sequences of 'value None/Node None/Node'
    # Let's write a helper function that takes lists and returns Nodes
    def helper(ls):
        for x, i in enumerate(ls):
            print(ls)
            print(ls[x+2])
            if i != 'None' and is_leaf(ls[x+1]) and is_leaf(ls[x+2]):
                return Node(i, ls[x+1], ls[x+2]) #Actually might matter if these are nodes or not...
            elif i!='None':
                #print(ls[x+1:])
                #print(x)
                helper([ls[x]]+[helper(ls[x+1:])])
    return helper(s2)

def is_leaf(li):
    if li == 'None' or isinstance(li, Node):
        return True
    else:
        return False

#take 2
#I'll come back to this with a fresh mind
def deserialize2(s):
    s2 = s.split(' ')
    # New logic: build it incrementally as it can compose nodes
    def deserialize_helper(ls):
        ix = next((x for x, i in enumerate(ls) if not(is_leaf(i)) and is_leaf(ls[x+1]) and is_leaf(ls[x+2])), None)
        if ix == None:
            return ls
        else:
            return deserialize_helper(ls[:ix]+[Node(ls[ix], ls[ix+1], ls[ix+2])]+ls[ix+3:])
    return deserialize_helper(s2)


node = Node('root', Node('left', Node('left.left')), Node('right'))

print(serialize(node))
assert deserialize2(serialize(node)).left.left.val == 'left.left'

# I don't know how to deserialize the tree in a way that isn't completely stupid
# I guess first thing first would be to find the root nodes, which appear to be necessarily sequences of int None None
