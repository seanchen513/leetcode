"""
98. Validate Binary Search Tree
Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt

###############################################################################
"""
NOT a solution!

It's not enough to recursively compare each node with its children.

Example:
[10, 5,15, None,None,6,20]

    10
   / \
  5   15
     / \
    6   20

is NOT a BST since 10 has 6 as a right descendant.
"""
class NotSolution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if root.left and root.left.val >= root.val:
            return False
        
        if root.right and root.right.val <= root.val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    
###############################################################################
"""
Solution #1: DFS recursion, passing along bounds for what range the
node's value can be.

O(n) time
O(n) extra space for skewed tree
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(root, min, max):
            if not root:
                return True
            
            val = root.val
            if val <= min or val >= max:
                return False
            
            return valid(root.left, min, val) and valid(root.right, val, max)
    
        return valid(root, -float('inf'), float('inf'))

"""
Solution #1b: iterative version
"""
class Solution1b:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, -float('inf'), float('inf'))]

        while stack:
            node, min, max = stack.pop()
            if node:
                val = node.val

                if val <= min or val >= max:
                    return False

                stack.extend([(node.left, min, val), (node.right, val, max)])
            
        return True

###############################################################################
"""
Solution #2: validate using inorder traversal; recursion.

This doesn't check the definition of a BST directly, but checks that the
inorder traversal of a BST should yield the values of the nodes in order.

O(n) time
O(n) extra space
"""
class Solution2:
    prev = -float('inf')

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        if not self.isValidBST(root.left):
            return False

        if root.val <= self.prev:
            return False

        self.prev = root.val

        if not self.isValidBST(root.right):
            return False

        return True

"""
Solution #2b: iterative version
"""
class Solution2b:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = -float('inf')
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if node.val <= prev:
                return False

            prev = node.val
            node = node.right

        return True

###############################################################################

if __name__ == "__main__":
    def test(arr):
        solutions = [
            NotSolution(),
            Solution(),
            Solution1b(),
            Solution2(),
            Solution2b(),
        ]

        root = array_to_bt(arr)[0]
        is_bst = [s.isValidBST(root) for s in solutions]

        print("#"*80)
        print(arr)
        print()
        print_tree(root)
        print(f"\nis BST? {is_bst}\n")

    arrays = [
        [],
        [0],
        [1],
        [2,1,3], # LC ex1; True
        [5,1,4,None,None,3,6], # LC ex2; False
        [10, 5,15, None,None,6,20] # LC test; False
    ]

    for arr in arrays:
        test(arr)
