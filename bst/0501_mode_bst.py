"""
LC501. Find Mode in Binary Search Tree
Easy

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""

from typing import List

import sys
sys.path.insert(1, '../tree/')
from binary_tree import TreeNode, print_tree #, array_to_bt, array_to_bt_lc, bt_find

###############################################################################
"""
Solution #1: Use iterative inorder traversal.

O(n) time
O(1) space as long as not O(n) values are same

LeetCode Jan 24, 2020
Runtime: 56 ms, faster than 64.38% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
"""
def find_mode(root) -> List:
    if not root:
        return []

    max_count = 0
    modes = []

    # inorder

    stack = []
    curr = root
    prev_val = None
    count = 1
    max_count = 1

    while curr or stack:
        if curr:
            while curr:
                stack.append(curr)
                curr = curr.left

        curr = stack.pop()
        
        if prev_val is None:
            prev_val = curr.val
        elif curr.val == prev_val:
            count += 1
        else:
            if count > max_count:
                modes = [prev_val]
                max_count = count
            elif count == max_count:
                modes.append(prev_val)

            count = 1
            prev_val = curr.val

        curr = curr.right

    if count > max_count:
        modes = [prev_val]
        #max_count = count
    elif count == max_count:
        modes.append(prev_val)

    return modes

###############################################################################
"""
Solution #2: use dict to keep count

O(n) time
O() extra space

LeetCode Jan 24, 2020
Runtime: 56 ms, faster than 64.38% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
"""
import collections

def find_mode2(root) -> List:
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        counts[node.val] += 1
        inorder(node.right)
    
    if not root:
        return []

    counts = collections.defaultdict(int)
    inorder(root)

    # find all keys with max value in the dict counts
    max_val = max(counts.values())
    
    return [k for k, v in counts.items() if v == max_val]   

###############################################################################

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    print_tree(root)

    modes = find_mode(root)
    modes2 = find_mode2(root)

    print(f"\nmodes (sol #1) = {modes}")
    print(f"modes (sol #2) = {modes2}")
