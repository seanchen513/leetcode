"""
1382. Balance a Binary Search Tree
Medium

Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""

from typing import List

import sys
sys.path.insert(1, '../../leetcode/tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###############################################################################
"""
Solution: use inorder traversal to build sorted array of tree nodes from
BST.  Then use recursion to build balanced BST from sorted array.

O(n) time
O(n) extra space: for sorted array
"""
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(root): # build sorted array
            if not root:
                return
            
            inorder(root.left)
            arr.append(root)
            inorder(root.right)
                        
        def build(start, end):  # build balanced BST using sorted array
            if start > end:
                return
            
            mid = start + (end - start) // 2
            node = arr[mid]
            
            node.left = build(start, mid-1)
            node.right = build(mid+1, end)
            
            return node
            
        arr = []
        inorder(root) # build sorted array
        
        return build(0, len(arr)-1) # build balanced BST using sorted array
             
###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        root = array_to_bt_lc(arr)
        
        print()
        print_tree(root)

        root = sol.balanceBST(root)

        print()
        print_tree(root)


    sol = Solution()

    comment = "LC example"
    arr = [1,None,2,None,3,None,4,None,None]
    test(arr, comment)
    