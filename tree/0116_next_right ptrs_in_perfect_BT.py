"""
116. Populating Next Right Pointers in Each Node
Medium

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:
The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""

#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

###############################################################################
"""
Solution 1: Use BFS.

O(n) time
O(n) extra space for "level" list (due to last level)
"""
class Solution:
    #def connect(self, root: 'Node') -> 'Node':
    def connect(self, root: 'TreeNode') -> 'TreeNode':

        level = [root]
        
        while level:
            next_level = []
            n = len(level)

            for i in range(n):
                node = level[i]
                
                if node:
                    if i < n-1:
                        node.next = level[i+1]
                        
                    next_level.extend([node.left, node.right])
            
            level = next_level

        return root

###############################################################################
"""
Solution 2: Recursion.  Deal with one level of the tree at a time by using 
a depth parameter.  For each fixed depth, store previous node encountered.

O(n log n) time - each recursion is O(n), and we do this O(log n) times
O(1) extra space other than for recursion stack
"""
class Solution2:
    #def connect(self, root: 'Node') -> 'Node':
    def connect(self, root: 'TreeNode') -> 'TreeNode':

        def link(node, max_depth, depth=1, prev=None):
            if not node or depth > max_depth: 
                return prev

            if depth == max_depth:
                if prev: 
                    prev.next = node

                prev = node
                
            prev = link(node.left, max_depth, depth + 1, prev)
            prev = link(node.right, max_depth, depth + 1, prev)
            
            return prev
            
        max_depth = 0 # 1-based (root has depth 1)
        node = root

        while node:
            max_depth += 1
            node = node.left

        for d in range(2, max_depth+1):
            link(root, d)

        return root

###############################################################################
"""
Solution 3: Iterate level by level.  Outer traversal from along left pointers.
Inner traversal along level using "next" pointers to construct "next" pointers
for the following level.

O(n) time
O(1) space

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37472/A-simple-accepted-solution
"""
class Solution3:
    #def connect(self, root: 'Node') -> 'Node':
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        pre = root # first node of each level

        while pre.left: # there is a next level; will make "next" ptrs for it
            # Assume current level already has "next" ptrs constructed
            curr = pre # iterate over current level

            while curr:
                curr.left.next = curr.right # connect siblings

                if curr.next: # connect consecutive cousins
                    curr.right.next = curr.next.left

                curr = curr.next

            pre = pre.left

        return root

###############################################################################
"""

For inorder traversal of perfect tree, consecutive leaves are separated by 
two links.  Unforunately, other nodes are separated by more than two links.

...

"""

"""
        def link_siblings(node):
            if node and node.left:
               node.left.next = node.right

               link_siblings(node.left)
               link_siblings(node.right)
            
        link_siblings(root)

        def link_leaves(node):
            if not node:
                return

            if not node.left and not node.right: # leaf
                if prev_leaf:
                    prev_leaf.next = node
                
                prev_leaf = node

            link_leaves(node.left)
            link_leaves(node.right)
"""

###############################################################################

if __name__ == "__main__":
    import copy

    def print_levels(root):
        node = root
        trav = []

        while node:
            curr = node

            while curr:
                trav += [curr.val]
                curr = curr.next

            trav += ['#']
            node = node.left

        print(trav)

    def test(arr, comment=None):
        root = array_to_bt_lc(arr)
        
        solutions = [Solution(), Solution2(), Solution3()]

        res = [s.connect(copy.deepcopy(root)) for s in solutions]        

        print("="*80)
        if comment:
            print(comment, "\n")
        print(arr, "\n")

        print_tree(root)
        print("\nSolutions:")
        
        for root in res:
            print_levels(root)

    comment = "Tree w/ depth 1"
    arr = [1]
    test(arr, comment)

    comment = "Tree w/ depth 2"
    arr = [1, 2,3]
    test(arr, comment)

    comment = "LC example 1; answer = [1,#,2,3,#,4,5,6,7,#]"
    arr = [1, 2,3, 4,5,6,7]
    test(arr, comment)

    comment = "Tree w/ depth 4"
    arr = [1, 2,3, 4,5,6,7, 8,9,10,11,12,13,14,15]
    test(arr, comment)
