"""
101. Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 
Note:
Bonus points if you could solve it both recursively and iteratively.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###############################################################################
"""
Solution: recursion, compare the two sides.

O(n) time: since every node is visited at most once (except the root).
O(n) extra space: for recursion in case of skewed tree.

"""
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def compare_sides(root, root2):
            if not root:
                return not root2

            if not root2:
                return not root

            ### Alternative checks
            # if not root and not root2:
            #     return True
            # if not root or not root2:
            #     return False

            return (root.val == root2.val and 
                compare_sides(root.left, root2.right) and 
                compare_sides(root.right, root2.left))

        return compare_sides(root, root)


###############################################################################
"""
Solution 2: create 2nd tree that flips left and right links.
Then compare two trees.

Building the 2nd tree is not necessary, but solution is for learning purposes.
"""
class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        def build_mirror(root):
            if not root:
                return None

            t = TreeNode(root.val)
            t.left = build_mirror(root.right)
            t.right = build_mirror(root.left)
            
            return t

        def compare_trees(root, root2):
            if not root:
                return not root2

            if not root2:
                return not root

            return (root.val == root2.val and 
                compare_trees(root.left, root2.left) and 
                compare_trees(root.right, root2.right))

        root2 = build_mirror(root)
        # print("\n\n")
        # print_tree(root2)
 
        return compare_trees(root, root2)

###############################################################################
"""
Solution 3: Use BFS using deque.  Deque holds tuples of nodes that represent
mirror traversals of tree.  If tree is symmetric, each tuple should contain
nodes that have equal values.

O(n) time
O(n) extra space
"""
class Solution3:
    def isSymmetric(self, root: TreeNode) -> bool:
        q = collections.deque( [(root, root)] )

        while q:
            node1, node2 = q.popleft()

            if not node1 and not node2:
                continue
            
            if not node1 or not node2: # exactly one is None
                return False

            if node1.val != node2.val:
                return False

            q.append( (node1.left, node2.right) )
            q.append( (node1.right, node2.left) )

        return True

###############################################################################

if __name__ == "__main__":
    def test(arr, comment):
        root = array_to_bt_lc(arr)

        print("="*80)
        if comment:
            print(comment)

        print()    
        print(arr)
        print()
        print_tree(root)

        res = sol.isSymmetric(root)

        print(f"\nres = {res}\n")

    
    sol = Solution() # recursion to compare tree w/ its mirror self
    #sol = Solution2() # build mirror tree, then recursion to compare
    sol = Solution3() # use BFS with deque holding tuples of mirror nodes

    comment = "trivial case; answer = True"
    arr = [1]
    test(arr, comment)

    comment = "LC ex1; answer = True"
    arr = [1,2,2,3,4,4,3]
    test(arr, comment)

    comment = "LC ex2; answer = False"
    arr = [1,2,2,None,3,None,3]
    test(arr, comment)

    comment = "LC test case; invalidates doing simple inorder; answer = False"
    arr = [1,2,2,2,None,2]
    test(arr, comment)

    comment = "LC test case; answer = False"
    arr = [5,4,1,None,1,None,4,2,None,2,None]
    test(arr, comment)

    comment = "LC test case; answer = False"
    arr = [2,3,3,4,5,None,4]
    test(arr, comment)
