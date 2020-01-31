"""
class TreeNode()

print_tree(root, depth=0)
array_to_bt(arr)
array_to_bt_lc(arr) # arr in LeetCode format

bt_find(root, val):
"""

from typing import List
import collections

class TreeNode():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def print_tree(root, depth=0):
    if root is None:
        return

    print_tree(root.right, depth + 1)
    print("  "*depth + str(root.val))
    print_tree(root.left, depth + 1)

"""
Converts array to binary tree.

If current node has index i, then its children have indices 2n+1 and 2n+2.
It's parent has index (i-1)//2.
Last possible parent has index (n-2)//2, where n = len(arr).

Assumes input array includes all possible None's.

Example use:
    arr = [6, 2,8, 0,4,7,9, None,None,3,5]
    #root, nodes = array_to_bt(arr)
    nodes = array_to_bt(arr)
    root = nodes[0]

    print_tree(root)

    node1 = nodes[arr.index(2)]
    node2 = nodes[arr.index(8)]
    test(root, node1, node2)

"""
def array_to_bt(arr):
    if not arr:
        #return None
        return [None]

    n = len(arr)
    nodes = [None] * n

    for i in range(n):
        if arr[i] is not None:
            nodes[i] = TreeNode(arr[i])
            
    for i in range(n//2):
        if arr[2*i + 1] is not None:
            nodes[i].left = nodes[2*i + 1]

        if arr[2*i + 2] is not None:
            nodes[i].right = nodes[2*i + 2]

    #return nodes[0]
    #return nodes[0], nodes
    return nodes

"""
Converts array in LeetCode format to binary tree.

Example input array:
[5,4,8,11,None,13,4,7,2,None,None,5,1]

What about [None] or [None, ...] ?  Return None.
"""
def array_to_bt_lc(arr): 
    if (not arr) or (arr[0] is None):
        return None

    root = TreeNode(arr[0])

    n = len(arr)
    if n == 1:
        return root

    level = [root]
    index = 1

    while level:
        next_level = []

        for node in level:
            if arr[index] is not None:
                node.left = TreeNode(arr[index])
                next_level.append(node.left)

            index += 1
            if index >= n:
                return root

            if arr[index] is not None:
                node.right = TreeNode(arr[index])
                next_level.append(node.right)

            index += 1
            if index >= n:
                return root
        
        level = next_level

    return root # this point is never reached, I think.

###############################################################################
"""
Returns the first node encountered with given value.
"""
def bt_find(root, val):
    if not root:
        return

    if root.val == val:
        return root
    
    node = bt_find(root.left, val)
    if node:
        return node

    node = bt_find(root.right, val)
    if node:
        return node

###############################################################################

if __name__ == "__main__":
    #arr = [5,4,8,11,None,13,4,7,2,None,None,5,1] # LC format
    #arr = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1] # all nodes at last level shown
    #root = array_to_bt(arr)
    #print_tree(root)

    ### test array_to_bt_lc()
    arr = [5,4,5,4,4,5,3,4,4,None,None,None,4,None,None,4,None,None,4,None,4,4,None,None,4,4]
    #arr = [1]
    #arr = None
    #arr = [None]
    #arr = [0]
    #arr = [1,None,3]
    #arr = [1,2,3]
    root = array_to_bt_lc(arr)
    print_tree(root)
    

    ### test array_to_bt() returning nodes
   
    arr = [3, 5,1, 6,2,0,8, None,None,7,4,None,None]
    nodes = array_to_bt(arr)
    root = nodes[0]
    p = nodes[arr.index(5)]
    q = nodes[arr.index(1)]
    #p = bt_find(root, 5)
    #q = bt_find(root, 1)
    #test(root, p, q)

    #q = bt_find(root, 4)
    q = nodes[arr.index(4)]
    #test(root, p, q)
