"""
35. Lowest Common Ancestor of a Binary Search Tree
Easy

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import print_tree, array_to_bt

###############################################################################
"""
Solution: recursion

Note: LCA is first value found that is in range of given nodes, inclusive

O(n) time - in worst case, visit all nodes in linear tree
O(n) extra space - in worst case, recursion stack for linear tree
"""
def lca_bst(root, node1, node2):
    if not root:
        return None

    val = root.val
    val1 = node1.val
    val2 = node2.val

    if val1 < val and val2 < val: # left side
        return lca_bst(root.left, node1, node2)

    if val1 > val and val2 > val: # right side
        return lca_bst(root.right, node1, node2)

    return root

"""
Solution #1b: same as sol #1, but use inner function and avoid 
recalculating val1 and val2.
"""
def lca_bst1b(root, node1, node2):
    def lca(root):
        val = root.val

        if val1 < val and val2 < val:
            return lca(root.left)

        if val1 > val and val2 > val:
            return lca(root.right)

        return root

    if not root:
        return None

    val1 = node1.val
    val2 = node2.val

    return lca(root)

###############################################################################
"""
Solution #2: iterative

Don't need to use stack or recursion since don't need to backtrace 
to find LCA node.

O(n) time - in worst case, visit all nodes in linear tree
O(1) extra space
"""
def lca_bst2(root, node1, node2):
    if not root:
        return None

    val1 = node1.val
    val2 = node2.val

    node = root
    while node:
        val = node.val

        if val1 < val and val2 < val:
            node = node.left

        elif val1 > val and val2 > val:
            node = node.right

        else:
            return node

###############################################################################

if __name__ == "__main__":
    def test(root, node1, node2):
        lca = lca_bst(root, node1, node2)
        lca1b = lca_bst1b(root, node1, node2)
        lca2 = lca_bst2(root, node1, node2)
        
        print(f"\nlca of {node1.val} and {node2.val} is:")
        print(f"sol #1 : {lca.val}")
        print(f"sol #1b: {lca1b.val}")
        print(f"sol #2 : {lca2.val}")

    ### LC ex1; answer = 6
    arr = [6, 2,8, 0,4,7,9, None,None,3,5]
    nodes = array_to_bt(arr)
    root = nodes[0]
    print_tree(root)

    node1 = nodes[arr.index(2)] # root.left # p = 2
    node2 = nodes[arr.index(8)] # root.right # q = 8
    test(root, node1, node2)
    
    ### LC ex2; answer = 2
    node1 = nodes[arr.index(2)] # root.left # p = 2
    node2 = nodes[arr.index(4)] # root.left.right # q = 4
    test(root, node1, node2)

    ### LC test case
    arr = [2, 1,None]
    nodes = array_to_bt(arr)
    root = nodes[0]
    node1 = nodes[arr.index(2)]
    node2 = nodes[arr.index(1)]
    test(root, node1, node2)
