"""
108. Convert Sorted Array to Binary Search Tree
Easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 """

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree #, array_to_bt

###############################################################################
"""
Solution #1: recursion

Depth of recursion tree is log n.  First set of slicing is O(n),
second set is 2*O(n/2) = O(n), third is 4*O(n/4) = O(n), etc. 
So total time due to slicing is O(n log n).  This dominates the
cost of creating the TreeNode's.

O(n log n) time due to copying arrays.
O(n) extra space for the tree that is built and returned.
O(n) extra space for the recursion stack due to array copies.
    - space per recursion level: n/2 + n/4 + n/8 + ... = n 
"""
def build_bst(arr):
    if not arr:
        return None

    mid = len(arr) // 2 # tree is left-biased
    #mid = (len(arr) - 1) // 2 # tree is right-biased

    root = TreeNode(arr[mid])
    root.left = build_bst(arr[:mid])
    root.right = build_bst(arr[mid+1:])

    return root

###############################################################################
"""
Solution #2: same as sol #1 but pass array indices instead of copying.

O(n) time since n TreeNode's are created.
O(n) extra space for the tree that is built is returned.
O(log n) extra space for the recursion stack.
    - the tree is height-balanced, so no worst case skewed tree in general.
"""
def build_bst2(arr):
    def build(low, high):
        if low > high:
            return None

        mid = (low + high) // 2 # tree is right-biased
        #mid = (low + high + 1) // 2 # tree is left-biased

        root = TreeNode(arr[mid])
        root.left = build(low, mid-1)
        root.right = build(mid+1, high)

        return root

    return build(0, len(arr)-1)

###############################################################################

if __name__ == "__main__":
    arr = [-10,-3,0,5,9]
    #arr = []
    #arr = [5]
    arr = [1,2,3,4,5,6,7,8,9]
    root = build_bst(arr)
    print(arr)
    print_tree(root)
