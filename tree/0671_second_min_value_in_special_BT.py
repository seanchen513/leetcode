"""
LC671. Second Minimum Node In a Binary Tree
Easy

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

from typing import List
import collections

#import sys
#sys.path.insert(1, '../tree/')
from binary_tree import TreeNode, print_tree, array_to_bt #, array_to_bt_lc, bt_find

###############################################################################
"""
Solution #1

O(n) time
O(n) extra space
"""
def second_min_bt(root):
    def second_min(root, min2=float('inf')):
        if root.left: # root.right also evaluates to True
            if min1 < root.left.val:
                min2 = min(min2, root.left.val)
            elif min1 == root.left.val:
                min2 = second_min(root.left, min2)
            
            if min1 < root.right.val:
                min2 = min(min2, root.right.val)
            elif min1 == root.right.val:
                min2 = second_min(root.right, min2)
            
        return min2

    min1 = root.val
    min2 = second_min(root)
    
    if min2 == float('inf'):
        return -1

    return min2

###############################################################################
"""
Solution #2

O(n) time
O(n) extra space
"""
def second_min_bt2(root):
    def second_min(root, min2=float('inf')):
        if root:
            if min1 < root.val < min2:
                min2 = root.val
            elif min1 == root.val:
                min2 = second_min(root.left, min2)
                min2 = second_min(root.right, min2)
        
        return min2

    min1 = root.val
    min2 = second_min(root)
    
    return min2 if min2 < float('inf') else -1

###############################################################################
"""
Brute force...
"""

###############################################################################

if __name__ == "__main__":
    arr = [1,1,2,1,1,2,2]
    nodes = array_to_bt(arr)
    root = nodes[0]
    print_tree(root)

    second_min = second_min_bt(root)
    second_min2 = second_min_bt2(root)

    print(f"\nsecond min (sol #1) = {second_min}")
    print(f"second min (sol #2) = {second_min2}")
