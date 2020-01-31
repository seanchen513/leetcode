"""
783. Minimum Distance Between BST Nodes
Easy

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Note:

1. The size of the BST will be between 2 and 100.
2. The BST is always valid, each node's value is an integer, and each node's value is different.
"""

#import sys
#sys.path.insert(1, '../tree/')
from binary_tree import print_tree, array_to_bt #, array_to_bt_lc, bt_find

###############################################################################
"""
Solution: iterative in-order traversal of BST using stack.

O(n) time
O(n) extra space for stack
"""
def min_diff_bst(root):
    #if not root:
    #    return None
    
    min_diff = float('inf')
    
    stack = []
    curr = root
    prev_val = None
    
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
            
        curr = stack.pop()

        if prev_val is not None:
            if curr.val - prev_val < min_diff:
                min_diff = curr.val - prev_val
            
        prev_val = curr.val
            
        curr = curr.right
        
    return min_diff

###############################################################################

if __name__ == "__main__":
    arr = [4, 2,6, 1,3,None,None]
    root = array_to_bt(arr)[0]
    print_tree(root)

    min_diff = min_diff_bst(root)

    print(f"\nmin diff = {min_diff}")
