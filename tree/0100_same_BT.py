"""
100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

###############################################################################
"""
Solution: DFS recursion.

O(n) time
O(h) space, where h is the max of the heights of the two trees.
"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def rec(p, q):
            if not p and not q: # if both are None
                return True
            
            if not p or not q: # if one of them is None
                return False
            
            if p.val != q.val:
                return False
            
            return rec(p.left, q.left) and rec(p.right, q.right)
            
        return rec(p, q)

###############################################################################
"""
Solution: DFS iteration using stack.

O(n) time

O(h) space, where h is max of heights of the two trees.
    O(n) space if both trees are linear with size n.
    O(log n) space if both trees are balanced with same size n.

"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q: # if both are None
                return True
            
            if not p or not q: # if one of them is None
                return False
            
            if p.val != q.val:
                return False
            
            return True

        stack = [(p, q)]

        while stack:
            p, q = stack.pop()

            if not check(p, q):
                return False

            if p:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

        return True

###############################################################################
"""
Solution: BFS iteration using queue.

O(n) time
O(n) space
    O(1) space if both trees are linear (or just one?)
    O(log n) space if both trees are balanced with same size n.

"""
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q: # if both are None
                return True
            
            if not p or not q: # if one of them is None
                return False
            
            if p.val != q.val:
                return False
            
            return True

        queue = collections.deque([(p, q)])

        while queue:
            p, q = queue.popleft()

            if not check(p, q):
                return False

            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

        return True
