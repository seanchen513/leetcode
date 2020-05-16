"""
1448. Count Good Nodes in Binary Tree
Medium

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4

Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].
"""

from typing import List
import collections

import sys
sys.path.insert(1, '../../leetcode/tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###############################################################################
"""
Solution: DFS. Keep track of current path's max value.

O(n) time
O(height) extra space
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mx=float('-inf')):
            nonlocal count

            if not node:
                return

            if node.val >= mx:
                count += 1

            mx = max(mx, node.val)
            
            dfs(node.left, mx)
            dfs(node.right, mx)

        count = 0

        dfs(root)

        return count

###############################################################################
"""
Solution 2: same, just rewritten.
"""
class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, mx=float('-inf')):
            if not node:
                return 0

            curr = (node.val >= mx)
            mx = max(mx, node.val)
            
            return dfs(node.left, mx) + dfs(node.right, mx) + curr

        return dfs(root)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        root = array_to_bt_lc(arr)

        print(f"\narr = {arr}\n")
        print_tree(root)

        res = sol.goodNodes(root)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution2()

    comment = "LC ex1; answer = 4"
    arr = [3,1,4,3,None,1,5]
    test(arr, comment)

    comment = "LC ex2; answer = 3"
    arr = [3,3,None,4,2]
    test(arr, comment)

    comment = "LC ex3; answer = 1"
    arr = [1]
    test(arr, comment)
