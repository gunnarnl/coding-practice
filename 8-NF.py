"""
[Easy]
This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
 """

 # First thing to notice is that all terminal nodes count as one. So that's the three ones, and the 0. Then the 1 node with 1 daughters is a unival tree.

 # Let's define our trees using the following Node class:

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# From this, it's easy to see when a node is a unival subtree: its left and right daughters must carry the same values all the way down. This means we should be writing a recursive function.

def unival_check(tree):
    if tree == None: #Applies to node with one leaf
        return True
    if tree.left == None and tree.right == None: #Terminal node
        return True
    elif tree.left.val == tree.val and tree.right.val == tree.val:
        return
