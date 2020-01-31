"""
687. Longest Univalue Path
Easy

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""

#import sys
#sys.path.insert(1, '../tree/')
from binary_tree import print_tree, array_to_bt, array_to_bt_lc, bt_find

###############################################################################
"""
Easier problem variation: paths don't have to go through root,
but paths CANNOT be V-shaped.

Solution: recursion
"""
def maxlen_unival_path0(root):
    def dfs(node, val=None, count=0, maxlen=0):
        if not node:
            return maxlen

        if node.val == val:
            count += 1
        else:
            count = 1
            val = node.val

        if count > maxlen:
            maxlen = count

        maxlen = dfs(node.left, val, count, maxlen)
        maxlen = dfs(node.right, val, count, maxlen)

        return maxlen

    return dfs(root) - 1 # count edges, not nodes

###############################################################################
"""
Solution: recursion

Paths don't have to go through root.  Paths can be V-shaped.

For each node, look at left "arrow" and right "arrow", where "arrow"
is non-V-shaped *unival* path from that node going down left or right side.
(Node values along arrow are all the same, and same as current node.)

Length of unival path through node is sum of lengths of left and right arrows.

O(n) time
O(n) extra space for recursion stack
"""
def maxlen_unival_path(root):
    def arrow(node, maxlen=0): # DFS; length of arrow
        if not node:
            return 0, maxlen
        
        left_length, maxlen = arrow(node.left, maxlen)
        right_length, maxlen = arrow(node.right, maxlen)

        left_arrow = 0
        right_arrow = 0

        if node.left and node.left.val == node.val:    
            left_arrow = left_length + 1

        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1

        maxlen = max(maxlen, left_arrow + right_arrow)

        return max(left_arrow, right_arrow), maxlen

    _, maxlen = arrow(root)

    return maxlen

"""
Same solution but make maxlen a mutable object in outer function.

"In Python 2 you cannot modify variable references outside of the function. 
In Python 3 there's nonlocal but that does not exist in Python 2. 
Hence this is a common hack where we use an array containing a single value 
and modify that value instead (the reference to the array is preserved)."
"""
def maxlen_unival_path1b(root):
    def arrow(node): # DFS; length of arrow
        if not node:
            return 0
        
        left_length = arrow(node.left)
        right_length = arrow(node.right)

        left_arrow = 0
        right_arrow = 0

        if node.left and node.left.val == node.val:    
            left_arrow = left_length + 1

        if node.right and node.right.val == node.val:
            right_arrow = right_length + 1

        maxlen[0] = max(maxlen[0], left_arrow + right_arrow)

        return max(left_arrow, right_arrow)

    # if used "maxlen" as simple integer, get:
    # UnboundLocalError: local variable 'maxlen' referenced before assignment
    maxlen = [0]

    arrow(root)

    return maxlen[0]

###############################################################################

if __name__ == "__main__":
    def test(root):
        print()
        print("#"*80)
        print_tree(root)

        #maxlen = maxlen_unival_path(root)
        maxlen = maxlen_unival_path1b(root)

        print(f"\nmax length of any unival path = {maxlen}")

    arr = [5, 4,5, 1,1,None,5] # LC ex1; answer = 2
    nodes = array_to_bt(arr)
    root = nodes[0]
    test(root)

    arr = [1, 4,5, 4,4,None,5] # LC ex2; answer = 2
    nodes = array_to_bt(arr)
    root = nodes[0]
    test(root)

    # LC test case; answer = 6
    arr = [5,4,5,4,4,5,3,4,4,None,None,None,4,None,None,4,None,None,4,None,4,4,None,None,4,4]
    root = array_to_bt_lc(arr)
    test(root)
