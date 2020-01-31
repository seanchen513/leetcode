"""
1026. Maximum Difference Between Node and Ancestor
Medium

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)


Example 1:

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7

Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3

Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Note:
The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""

#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

###############################################################################
"""
Solution 1: Recursion.  For each subtree, find the min and max values.  
Calculate and update the global max diff.
"""
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal max_diff

            if not node:
                return float('inf'), -float('inf')
            
            lmin, lmax = dfs(node.left)
            rmin, rmax = dfs(node.right)

            min0 = min(lmin, rmin, node.val)
            max0 = max(lmax, rmax, node.val)

            max_diff = max(max_diff, node.val - min0, max0 - node.val)

            return min0, max0
        
        if not root:
            return 0

        max_diff = -float('inf')
        dfs(root)

        return max_diff

###############################################################################
"""
Solution 2: Recursion.  Top-down.  Every path ends at a leaf->None.
Propagate low and high values found so far along paths until None is reached,
then return high - low.  The max of these are taken as the recursion
goes back up.

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274654/Python-Recursion
"""
class Solution2:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def helper(node, low, high):
            if not node:
                return high - low
            
            high = max(high, node.val)
            low = min(low, node.val)

            l_max_diff = helper(node.left, low, high)
            r_max_diff = helper(node.right, low, high)
            
            return max(l_max_diff, r_max_diff)

            # return max(
            #     helper(node.left, low, high), 
            #     helper(node.right, low, high) )

        if not root:
            return 0

        return helper(root, root.val, root.val)

###############################################################################
"""
Solution 3: Iterative DFS, top-down.

O(n) time
O(h) extra space

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274685/Python-iterative-DFS-top-down
"""
class Solution3:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, root.val, root.val)]
        max_diff = float('-inf')

        while stack:
            node, low, high = stack.pop()

            max_diff = max(max_diff, abs(low - node.val), abs(high - node.val))

            low = min(low, node.val)
            high = max(high, node.val)

            if node.left:
                stack.append((node.left, low, high))
            if node.right:
                stack.append((node.right, low, high))

        return max_diff

###############################################################################

if __name__ == "__main__":
    def test(arr):
        root = array_to_bt_lc(arr)

        solutions = [Solution(), Solution2(), Solution3()]

        max_diff = [s.maxAncestorDiff(root) for s in solutions]

        print("#"*80)
        print_tree(root)

        print(f"\nmax diff (all solutions) = {max_diff}\n")

    arrays = [
        [],
        [1],
        [1,2],
        [2,1],
        [8,3,10,1,6,None,14,None,None,4,7,13], # LC example; answer = 8 - 1 = 7
        [1,None,2,None,0,3], # LC test; answer = 3 - 0 = 3
    ]

    for arr in arrays:
        test(arr)

