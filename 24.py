"""
[Medium]
This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

is_locked, which returns whether the node is locked

lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.

unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.left = None
        self.right = None
        self.data = data
        self.locked = False

    def is_locked(self):
        return self.locked

    #I'm going to assume that a tree can only lock if all of its children are unlocked

    def lock(self):
        if check_locked(self, True):
            return False
        else:
            self.locked = True
            return True

    def unlock(self):
        if check_locked(self, False):
            return False
        else:
            self.locked = False
            return True

def check_locked(node, value):
    if node.locked != value:
        return False

    if node.left != None and check_locked(node.left, value)==False:
        return False

    if node.right != None and check_locked(node.right, value)==False:
        return False

    return True

test = Node("one", right=Node("two"))

print(test.is_locked())
print(test.unlock())
