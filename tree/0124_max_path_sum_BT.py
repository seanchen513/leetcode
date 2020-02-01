"""
124. Binary Tree Maximum Path Sum
Hard

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

###############################################################################
"""
Solution: postorder recursion.  Need to track 2 things: max sums of non-V-shaped
paths (call these arrows), and max sums of possibly V-shaped paths.  

Since the latter is global to the recursion, we make it nonlocal (could also 
be a class var; or just include it as another return value).

The former is used to update the latter for each node, and is passed up
to its parent.  Since paths don't need to reach down to the roots,
and in order to maximize sums, we don't let arrows have negative sums
(take an empty arrow with 0 sum instead).

O(n) time
O(h) extra space for recursion
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            left_arrow = dfs(node.left)
            right_arrow = dfs(node.right)

            max_sum = max(max_sum, left_arrow + right_arrow + node.val)

            # Don't let arrows have negative sums.
            return max(0, max(left_arrow, right_arrow) + node.val)

        max_sum = float('-inf') # this is for possibly V-shaped paths
        dfs(root)

        return max_sum

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        root = array_to_bt_lc(arr)
        
        solutions = [Solution()]#, Solution2()]

        res = [s.maxPathSum(root) for s in solutions]

        print("="*80)
        if comment:
            print(comment, "\n")
        print(arr, "\n")

        print_tree(root)
        print(f"\nSolutions: {res}")
        

    comment = "LC example 1; answer = 6"
    arr = [1,2,3]
    test(arr, comment)

    comment = "LC example 2; answer = 42"
    arr =  [-10,9,20,None,None,15,7]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [2,-1]
    test(arr, comment)
    