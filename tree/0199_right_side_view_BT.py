"""
199. Binary Tree Right Side View
Medium

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc
from typing import List

###############################################################################
"""
Solution 1: BFS and take last element of each level.

O(n) time
O(n) extra space (due to last level)
O(h) space for output
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        view = []
        level = [root]
        
        while level:
            view += [level[-1].val]
            
            next_level = []
            
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            level = next_level
            
        return view
                    
###############################################################################
"""
Solution 2: modified postorder traversal (LRP, left-right-parent).
For each level, the rightmost element is visited first.

O(n) time
O(h) space for recursion stack
O(h) space for dict and output
"""
class Solution2:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(node, depth=0):
            if not node:
                return

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

            if depth not in view:
                view[depth] = node.val

        view = {}
        dfs(root)

        return [view[d] for d in range(len(view))]

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        root = array_to_bt_lc(arr)
        
        solutions = [Solution(), Solution2()]

        res = [s.rightSideView(root) for s in solutions]        

        print("="*80)
        if comment:
            print(comment, "\n")
        print(arr, "\n")

        print_tree(root)
        print(f"\nSolutions: {res}")
        
    comment = "Tree w/ depth 1"
    arr = [1]
    test(arr, comment)

    comment = "Tree w/ depth 2"
    arr = [1, 2,3]
    test(arr, comment)

    comment = "Tree w/ depth 3"
    arr = [1, 2,3, 4,5,6,7]
    test(arr, comment)

    comment = ""
    arr = [1,None,3,None,7]
    test(arr, comment)

    comment = ""
    arr = [1,2,None,4]
    test(arr, comment)

    comment = ""
    arr = [1, 2,3, 4,None,None,7, 8,None,None,15]
    test(arr, comment)

    comment = "LC example 1; answer = [1, 3, 4]"
    arr = [1, 2,3, None,5,None,4]
    test(arr, comment)
