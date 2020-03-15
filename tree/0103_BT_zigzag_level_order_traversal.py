"""
103. Binary Tree Zigzag Level Order Traversal
Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:

Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""

from typing import List
import collections

#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt, array_to_bt_lc

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###############################################################################
"""
Solution: BFS traversal using deque first, then reverse every other sublist
in results list.

O(n) time
O(n) extra space for output
O(n) extra space for "level" list
O(n) extra space for reversing sublists
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        
        while q:
            level = []
            
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
            res.append(level)
         
        for i in range(len(res)):
            if i % 2 == 1:
                res[i] = res[i][::-1]
        
        return res

###############################################################################
"""
Solution 2: BFS using deque.  Traverse BT in zigzag level-order manner.

Note: there are slight variations of this.

O(n) time
O(n) extra space for output 
O(n) extra space for deque
O(n) extra space for "level" list
"""
class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        q = collections.deque([root])
        res = []
        even = 1 # treat as boolean; alternate b/w 0 (False) and 1 (True)
        
        while q:
            level = []
            
            if even:
                for _ in range(len(q)):
                    node = q.popleft()
                    level.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            else:
                for _ in range(len(q)):
                    node = q.pop()
                    level.append(node.val)

                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
        
            even = 1 - even

            res.append(level)

        return res

###############################################################################
"""
Solution 3: DFS using recursion.

O(n) time
O(n) extra space for output
O(h) extra space for recursion call stack, where h is height of tree
"""
class Solution3:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, level):
            if level >= len(res): # add new sublist for new level
                res.append( collections.deque([node.val]) )
            else:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)

            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)

        if not root:
            return []

        res = []

        dfs(root, 0)
        
        return res

###############################################################################
"""
Solution 4: iterative DFS using stack.

O(n) time
O(n) extra space for output
O(h) extra space for stack list
"""
class Solution4:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()

            if level >= len(res): # add new sublist for new level
                res.append( collections.deque([node.val]) )
            else:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)

            # Note: push right before left onto stack, so that left nodes
            # will be processed first.
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))

        return res

###############################################################################

if __name__ == "__main__":
    def test(m, n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        root = array_to_bt_lc(arr)

        print()
        print_tree(root)

        res = sol.zigzagLevelOrder(root)

        print(f"\nres = {res}\n")


    sol = Solution() # level-order traversal, then reverse every other sublist in results list
    sol = Solution2() # traverse BT in zigzag level-order manner
    
    sol = Solution3() # DFS using recursion
    sol = Solution4() # DFS using iteration

    comment = "LC example"
    arr = [3,9,20,None,None,15,7]
    test(arr, comment)
    
    comment = ""
    arr = [1, 2,3, 4,5,6,7, 8,9,10,11,12,13,14,15]
    test(arr, comment)
