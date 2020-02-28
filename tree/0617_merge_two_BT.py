"""
617. Merge Two Binary Trees
Easy

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  

Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 
Note: The merging process must start from the root nodes of both trees.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

import collections
import copy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###############################################################################
"""
Solution 1: merge BT's using existing tree nodes.  DFS using recursion.
Pre-order traversal.

O(n) time, where n = number of overlapping tree nodes.
This is because any time one node is None, we return the other node.
Example: one tree is skewed to left, and other tree is skewed to right.

Same worst case space complexity due to recursion depth in case both trees
are skewed in the same way.
Avg space complexity is O(log n).

Runtime: 84 ms, faster than 91.37% of Python3 online submissions
Memory Usage: 13.6 MB, less than 82.86% of Python3 online submissions
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def rec(t1, t2):
            if not t1: return t2
            if not t2: return t1

            # Both nodes exist.
            t1.val += t2.val
            t1.left = rec(t1.left, t2.left)
            t1.right = rec(t1.right, t2.right)

            return t1

        return rec(t1, t2)

"""
Solution 1b: iterative version of sol 1, using stack to do DFS.
"""
class Solution1b:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2

        root = t1
        stack = [(t1, t2)]
        
        while stack:
            t1, t2 = stack.pop()

            if not t1 or not t2:
                continue
            
            t1.val += t2.val
            
            if not t1.left:
                t1.left = t2.left
            elif t2.left: # both t1 and t2 have left nodes
                stack.append((t1.left, t2.left))

            if not t1.right:
                t1.right = t2.right
            elif t2.right: # both t1 and t2 have right nodes
                stack.append((t1.right, t2.right))

        return root

###############################################################################
"""
Solution 2: create new tree.  DFS using recursion.
Pre-order traversal.

Runtime: 96 ms, faster than 33.83% of Python3 online submissions
Memory Usage: 14 MB, less than 25.72% of Python3 online submissions
"""
class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def rec(t1, t2):
            if not t1 and not t2:
                return None
            
            if not t1:
                ### or can just deep clone t2
                #t = copy.deepcopy(t2)
                
                t = TreeNode(t2.val)
                t.left = rec(None, t2.left)
                t.right = rec(None, t2.right)

            elif not t2:
                ### or can just deep clone t1
                #t = copy.deepcopy(t1)

                t = TreeNode(t1.val)
                t.left = rec(t1.left, None)
                t.right = rec(t1.right, None)
                
            else:              
                t = TreeNode(t1.val + t2.val)
                t.left = rec(t1.left, t2.left)
                t.right = rec(t1.right, t2.right)
            
            return t
            
        return rec(t1, t2)

"""
Solution 2b: create new tree.  DFS using stack.
Pre-order traversal.

Runtime: 112 ms, faster than 12.24% of Python3 online submissions
Memory Usage: 13.9 MB, less than 51.43% of Python3 online submissions
"""
class Solution2b:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        header = TreeNode(None)
        stack = [(t1, t2, header, True)]

        while stack:
            t1, t2, parent, b_left = stack.pop()

            if not t1 and not t2:
                continue

            if not t1:
                ### or can just deep clone t2
                #t = copy.deepcopy(t2)

                t = TreeNode(t2.val)
                stack.append((None, t2.left, t, True))
                stack.append((None, t2.right, t, False))

            elif not t2:
                ### or can just deep clone t1
                #t = copy.deepcopy(t1)
                
                t = TreeNode(t1.val)
                stack.append((t1.left, None, t, True))
                stack.append((t1.right, None, t, False))
                
            else:              
                t = TreeNode(t1.val + t2.val)
                stack.append((t1.left, t2.left, t, True))
                stack.append((t1.right, t2.right, t, False))

            if b_left:
                parent.left = t
            else:
                parent.right = t

        return header.left

###############################################################################
"""
Solution 3: BFS using deque.
Creates new nodes for tree 1 when needed.

https://leetcode.com/problems/merge-two-binary-trees/discuss/104429/Python-BFS-Solution
"""
class Solution3():
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2:
            return t1 or t2

        q1 = collections.deque( [t1] )
        q2 = collections.deque( [t2] )

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()
            
            if node1 and node2:
                node1.val = node1.val + node2.val

                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)

                q1.append(node1.left)
                q1.append(node1.right)
                
                q2.append(node2.left)
                q2.append(node2.right)
        
        return t1

###############################################################################

if __name__ == "__main__":
    def test(t1, t2, comment=None):
        t1 = array_to_bt_lc(t1)
        t2 = array_to_bt_lc(t2)
        
        root = sol.mergeTrees(t1, t2)

        print("="*80)
        if comment:
            print(comment, "\n")
        
        print_tree(root)
        
    sol = Solution() # merge trees into t1
    sol = Solution1b() # iterative version using stack

    sol = Solution2() # new tree; recursion
    #sol = Solution2b() # new tree; DFS using stack

    #sol = Solution3() # BFS using deque; creates new nodes as needed


    comment = "LC example 1"
    t1 = [1,3,2,5]
    t2 = [2,1,3,None,4,None,7]
    test(t1, t2, comment)

    comment = "LC test case"
    t1 = []
    t2 = [1]
    test(t1, t2, comment)

