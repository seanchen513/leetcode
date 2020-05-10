"""
1339. Maximum Product of Splitted Binary Tree
Medium

Given a binary tree root. Split the binary tree into two subtrees by removing 1 edge such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:

Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation:  Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025

Example 4:

Input: root = [1,1]
Output: 1

Constraints:

Each tree has at most 50000 nodes and at least 2 nodes.
Each node's value is between [1, 10000].
"""

import sys
sys.path.insert(1, '../../leetcode/tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

###############################################################################
"""
Solution: DFS recursion.

O(n) time
O(h) extra space, where h = height of tree
"""
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def sum_tree(node):
            if not node:
                return 0
            
            return sum_tree(node.left) + sum_tree(node.right) + node.val       
        
        def dfs(node):
            nonlocal max_product
            
            if not node:
                return 0
            
            subtree_sum = dfs(node.left) + dfs(node.right) + node.val
            other_sum = total_sum - subtree_sum
            
            max_product = max(max_product, subtree_sum * other_sum)
            
            return subtree_sum
            
        total_sum = sum_tree(root)
        max_product = float('-inf')
        
        dfs(root)
        
        return max_product % (10**9 + 7)
        
###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        root = array_to_bt_lc(arr)

        print(f"\narr = {arr}\n")
        print_tree(root)

        res = sol.maxProduct(root)

        print(f"\nres = {res}\n")


    sol = Solution() # 

    comment = "LC ex1; answer = 90"
    arr = [1,None,2,3,4,None,None,5,6]
    test(arr, comment)

    comment = "LC ex2; answer = 1025"
    arr = [2,3,9,10,7,8,6,5,4,11,1]
    test(arr, comment)

    comment = "LC ex3; answer = 1"
    arr = [1,1]
    test(arr, comment)
