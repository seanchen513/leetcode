"""
1008. Construct Binary Search Tree from Preorder Traversal
Medium

Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 

1 <= preorder.length <= 100
The values of preorder are distinct.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree
from typing import List
import bisect

###############################################################################
"""
Solution: preorder recursion on upper bound for subtree.

Left children are bounded by the value of their parents.
Right children share the same bound that their parents have.

O(n) time
O(h) extra space for recursion
O(n) extra space for BST being built
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(bound=float('inf')):
            nonlocal index

            if index == n or preorder[index] > bound:
                return None

            root = TreeNode(preorder[index])

            index += 1

            root.left = build(root.val) 
            root.right = build(bound)

            return root

        n = len(preorder)
        index = 0

        return build()

"""
Solution 1b: same, but pass index as parameter, and return it along with node.
"""
class Solution1b:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(index, bound=float('inf')):
            if index == n or preorder[index] > bound:
                return index, None

            root = TreeNode(preorder[index])

            index += 1

            index, root.left = build(index, root.val) 
            index, root.right = build(index, bound)

            return index, root

        n = len(preorder)

        return build(0)[1]

###############################################################################
"""
Solution 2: preorder recursion on start and end indices of preorder array
for current subtree.

First element of preorder is the root.  Then come the values for the left
subtree, which are all smaller than the root.  Then come the values for the 
right subtree, which are all bigger than the root.

O(n log n) time if use binary search and pass around array indices

O(h) extra space for recursion
O(n) extra space for BST that is built

Binary search
    O(log n) for first search.
    This is done once for every node that is constructed.
    So total time for binary search is at most O(n log n).

If pass around array copies (slicing), and used binary search:
    Copying for left and right halves together is O(n).
    This is done once for every node that is constructed.
    So total time for array copying is at most O(n^2).

Note: can pass around modified "end" index that is 1 more than regular one.
"""
class Solution2:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(start, end):
            if start > end:
                return None
            
            val = preorder[start]
            node = TreeNode(val)

            ### binary search for first element > val within range
            ### specified by indices start+1, end+1 (Python slice convention)
            i = bisect.bisect(preorder, val, start + 1, end + 1)
            
            node.left = build(start + 1, i - 1)
            node.right = build(i, end)
        
            return node
        
        return build(0, len(preorder)-1)

"""
Solution 2b: same, but use linear search instead of binary search.

O(n^2) time if use linear search or pass around array indices, or both.

O(n) time for first search.
This is done once for every node that is constructed.
So total time is at most O(n^2).

O(h) extra space for recursion
O(n) extra space for BST that is built

Note: can pass around modified "end" index that is 1 more than regular one.
"""
class Solution2b:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(start, end):
            if start > end:
                return None
            
            val = preorder[start]
            node = TreeNode(val)
            
            ### linear search for index of first number bigger than val
            i = start + 1
            while i <= end and preorder[i] < val:
                i += 1

            node.left = build(start + 1, i - 1)
            node.right = build(i, end)
        
            return node
        
        return build(0, len(preorder)-1)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\npreorder = {arr}\n")

        res = sol.bstFromPreorder(arr)

        print_tree(res)
        print()


    sol = Solution() # preorder recursion on upper bound for subtree.
    #sol = Solution1b() # same, but pass index as parameter as well

    #sol = Solution2() # preorder recursion on start and end indices; bsearch
    #sol = Solution2b() # same, but use linear search
        
    comment = "Single node tree"
    arr = [1]
    test(arr, comment)

    comment = "LC example; answer = [8,5,10,1,7,null,12]"
    arr = [8,5,1,7,10,12]
    test(arr, comment)

    comment = "LC test case; answer = [4,2]"
    arr = [4,2]
    test(arr, comment)
