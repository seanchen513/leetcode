"""
543. Diameter of Binary Tree
Easy

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt, array_to_bt_lc

###############################################################################
"""
Solution #1:

O(n) time
O(n) extra space for recursion stack
"""
def diameter_bt(root):
    def diameter(node):
        if not node:
            return 0

        left = diameter(node.left) + 1 if node.left else 0
        right = diameter(node.right) + 1 if node.right else 0

        maxlen[0] = max(maxlen[0], left + right)

        return max(left, right)

    maxlen = [0]
    diameter(root)

    return maxlen[0]

"""
Solution: same as sol #1 but move the "+ 1"
"""
def diameter_bt2(root):
    def diameter(node):
        if not node:
            return 0

        left = diameter(node.left)
        right = diameter(node.right)

        maxlen[0] = max(maxlen[0], left + right)

        return max(left, right) + 1

    maxlen = [0]
    diameter(root)

    return maxlen[0]

###############################################################################

if __name__ == "__main__":
    def test(root):
        print()
        print("#"*80)
        print_tree(root)

        diam = diameter_bt(root)
        diam2 = diameter_bt2(root)

        print(f"\ndiameter of BT (sol #1) = {diam}")
        print(f"diameter of BT (sol #2) = {diam2}")

    root = None
    test(root)
    
    root = TreeNode(1)
    test(root)

    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, )))))
    test(root)

    arr = [5, 4,5, 1,1,None,5] 
    nodes = array_to_bt(arr)
    root = nodes[0]
    test(root)

    arr = [1, 4,5, 4,4,None,5] 
    nodes = array_to_bt(arr)
    root = nodes[0]
    test(root)

    arr = [5,4,5,4,4,5,3,4,4,None,None,None,4,None,None,4,None,None,4,None,4,4,None,None,4,4]
    root = array_to_bt_lc(arr)
    test(root)

    arr = [1, 2,3, 4,5] # LC example; answer = 3
    root = array_to_bt_lc(arr)
    test(root)
    