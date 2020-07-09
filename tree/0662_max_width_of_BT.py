"""
662. Maximum Width of Binary Tree
Medium

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).

Note: Answer will in the range of 32-bit signed integer.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

###############################################################################
"""
Solution: BFS. Label each node with an index. For each level of BFS, calculate
the width of the level as the difference between the min and max indices of
nodes at that level.

Indices for tree nodes:
1
2,3
4,5, 6,7

l = 2x 
r = 2x + 1

Alternative:
0
1,2
3,4, 5,6

l = 2x + 1
r = 2x + 2

O(n) time
O(n) extra space: for lists

"""
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:        
        level = [(root, 1)]
        max_width = 0
        inf = float('inf')

        while level:
            next_level = []
            min_index = inf
            max_index = -inf

            for node, index in level:
                min_index = min(min_index, index)
                max_index = max(max_index, index)

                if node.left:
                    next_level.append((node.left, 2*index))
                    
                if node.right:
                    next_level.append((node.right, 2*index + 1))

            level = next_level
            max_width = max(max_width, max_index - min_index)

        # Add 1 here to avoid repeatedly adding 1 in the max_width
        # calculation within the loop.
        return max_width + 1

###############################################################################
"""
Solution 2: DFS with dict that maps depth/level to min index at that depth/level.

O(n) time
O(n) extra space: for dict
"""
class Solution2:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node, depth, index):
            nonlocal max_width

            if depth not in d: # first node encountered at this depth
                d[depth] = index

            max_width = max(max_width, index - d[depth])

            if node.left:
                dfs(node.left, depth + 1, 2*index)

            if node.right:
                dfs(node.right, depth + 1, 2*index + 1)

        d = {}
        max_width = 0

        dfs(root, 0, 1)

        # Add 1 here to avoid repeatedly adding 1 in the max_width
        # calculation within dfs().
        return max_width + 1
