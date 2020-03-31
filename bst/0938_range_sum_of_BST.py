"""
938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
 
Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

###############################################################################
"""
Solution: recursive

O(n) time
O(h) extra space
"""
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            return root.val + self.rangeSumBST(root.left, L, R) + self.rangeSumBST(root.right, L, R)

"""
Solution: another way to write it using a helper fn.

"""
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(root):
            if not root:
                return 0
            
            if root.val < L:
                return dfs(root.right)
            if root.val > R:
                return dfs(root.left)
            
            return root.val + dfs(root.left) + dfs(root.right)

        return dfs(root)

"""
Solution: another way to write it, using a helper function, and a 
variable to hold the sum rather than using a return value.
"""
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(root):
            nonlocal s

            if not root:
                return
            
            if root.val < L:
                dfs(root.right)
            elif root.val > R:
                dfs(root.left)
            else:
                s += root.val
                dfs(root.left)
                dfs(root.right)

        s = 0 # sum
        dfs(root)

        return s

"""
Solution: iterative DFS using stack (preorder)

O(n) time
O(h) extra space
"""
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack = [root]
        s = 0

        while stack:
            node = stack.pop()

            if node:
                if node.val < L:
                    stack.append(node.right)
                elif node.val > R:
                    stack.append(node.left)
                else:
                    s += node.val
                    stack.extend([node.left, node.right])

        return s
