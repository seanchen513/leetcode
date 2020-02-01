"""
1008. Construct Binary Search Tree from Preorder Traversal
Medium

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc
from typing import List

###############################################################################
"""
Solution: preorder recursion.

First element of preorder is the root.  Then come the values for the left
subtree, which are all smaller than the root.  Then come the values for the 
right subtree, which are all bigger than the root.

O(n log n) time if use binary search and pass around array indices
O(n^2) time if use linear search or pass around array indices, or both.

O(h) extra space for recursion
O(n) extra space for BST that is built

If used linear search instead of binary search:
    O(n) for first search.
    This is done once for every node that is constructed.
    So total time is at most O(n^2).

Binary search
    O(log n) for first search.
    This is done once for every node that is constructed.
    So total time for binary search is at most O(n log n).

If pass around array copies (slicing), and used binary search:
    Copying for left and right halves together is O(n).
    This is done once for every node that is constructed.
    So total time for array copying is at most O(n^2).
"""
import bisect

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(arr, start, end):
            if start > end:
                return None
            
            root_val = arr[start]
            root = TreeNode(root_val)
            
            ### linear search for index of first number bigger than root
            #i = start + 1
            #while (i <= end) and (arr[i] < root_val):
            #    i += 1

            ### binary search for first element > root_val within range
            ### specified by indices start+1, end+1 (Python slice convention)
            i = bisect.bisect(arr, root_val, start + 1, end + 1)
            
            root.left = build(arr, start + 1, i - 1)
            root.right = build(arr, i, end)
        
            return root
        
        return build(preorder, 0, len(preorder)-1)

###############################################################################
"""
Solution 2: preorder recursion using upper bounds.

O(n) time
O(h) extra space for recursion
O(n) extra space for BST being built
"""
class Solution2:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(arr, bound=float('inf')):
            nonlocal index

            if index == n or arr[index] > bound:
                return None

            root = TreeNode(arr[index])

            index += 1

            root.left = build(arr, root.val) 
            root.right = build(arr, bound)

            return root

        n = len(preorder)
        index = 0
        return build(preorder)

###############################################################################

if __name__ == "__main__":
    def test(preorder, comment=None):
        root = array_to_bt_lc(arr)
        
        solutions = [Solution(), Solution2()]

        res = [s.bstFromPreorder(preorder) for s in solutions]

        print("="*80)
        if comment:
            print(comment, "\n")
        print(f"preorder = {preorder}\n")
        
        print(f"\nSolutions:")
        for root in res:
            print_tree(root)
            print()

        
    comment = "Single node tree"
    arr = [1]
    test(arr, comment)

    comment = "LC example; answer = [8,5,10,1,7,null,12]"
    arr = [8,5,1,7,10,12]
    test(arr, comment)

    comment = "LC test case; answer = [4,2]"
    arr = [4,2]
    test(arr, comment)
