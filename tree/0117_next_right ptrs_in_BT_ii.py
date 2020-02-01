"""
117. Populating Next Right Pointers in Each Node II
Medium

Given a binary tree

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

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]

Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Constraints:

The number of nodes in the given tree is less than 6000.
-100 <= node.val <= 100
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
    #def connect(self, root: 'Node') -> 'Node': # for LC
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
                    
                    if node.left:    
                        next_level.append(node.left)
                    if node.right:    
                        next_level.append(node.right)
                    
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
    #def connect(self, root: 'Node') -> 'Node': # for LC
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        def max_depth(node, depth=0):
            if not node:
                return depth

            return max(max_depth(node.left, depth + 1), 
                max_depth(node.right, depth + 1) )

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
            
        max_d = max_depth(root) # 1-based; root has depth 1

        for d in range(2, max_d+1):
            link(root, d)

        return root
###############################################################################
"""
Solution 3: BFS using current level's next pointers to build the next level's
next pointers.  Use var "curr" to keep track of last node encountered on next 
level.  It's advanced each time the next node on the next level is found and
"curr.next" is assigned.

Initialize "curr" to a dummy node.  Dummy node ends up pointing to first node 
of each level, which can be used to advance the iteration to the next level.

O(n) time
O(1) extra space

https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37811/Simple-solution-using-constant-space
"""
class Solution3:
    #def connect(self, root: 'Node') -> 'Node': # for LC
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        pre = root

        while pre: # first node of current level
            # Dummy node that will point to first node of next level.
            # This will be side effect of first assignment of "curr.next" below.
            temp = TreeNode(0) 

            curr = temp # traverses the next level, following new "next" ptrs

            while pre: # traverse current level
                if pre.left:
                    curr.next = pre.left
                    curr = curr.next # traverse next level

                if pre.right:
                    curr.next = pre.right
                    curr = curr.next

                pre = pre.next

            pre = temp.next # set to first node of next level

        return root

###############################################################################
"""
Solution 3b: same as sol #3, but instead of using dummy "temp" var to point
to first node of next level, find the first node of next level explicitly
within the same inner loop.  Since "curr" starts out as "first", be careful 
we don't make it point back to itself.
"""
class Solution3b:
    #def connect(self, root: 'Node') -> 'Node': # for LC
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        pre = root

        while pre: # first node of current level
            first = None # will point to first node of next level
            curr = None # traverses the next level, following new "next" ptrs

            while pre: # traverse current level
                if not first:
                    curr = first = pre.left or pre.right
                
                if curr:
                    if pre.left and curr != pre.left:
                        curr.next = pre.left
                        curr = curr.next # traverse next level

                    if pre.right and curr != pre.right:
                        curr.next = pre.right
                        curr = curr.next

                pre = pre.next

            pre = first # set to first node of next level

        return root

###############################################################################
"""
Solution 3c: same as sol #3, but instead of using dummy "temp" var to point
to first node of next level, find the first node of next level explicitly
within its own loop.  Since "curr" starts out as "first", be careful 
we don't make it point back to itself.
"""
class Solution3c:
    #def connect(self, root: 'Node') -> 'Node': # for LC
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        pre = root

        while pre: # first node of current level
            # find the first node of next level
            first = None
            pre2 = pre
            while pre2 and not first:
                first = pre2.left or pre2.right
                pre2 = pre2.next

            # 
            curr = first # traverses the next level, following new "next" ptrs

            while pre: # traverse current level
                if pre.left and curr != pre.left:
                    curr.next = pre.left
                    curr = curr.next # traverse next level

                if pre.right and curr != pre.right:
                    curr.next = pre.right
                    curr = curr.next

                pre = pre.next

            pre = first # set to first node of next level

        return root

###############################################################################

if __name__ == "__main__":
    import copy

    def print_levels(root):
        pre = root
        trav = []

        while pre:
            node = pre
            pre = None

            while node:
                trav += [node.val]

                if not pre: # set to first node of next level
                    pre = node.left or node.right

                node = node.next

            trav += ['#']

        print(trav)

    def test(arr, comment=None):
        root = array_to_bt_lc(arr)
        
        solutions = [Solution(), Solution2(), Solution3(), Solution3b(), Solution3c()]

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

    comment = "Tree w/ depth 3; answer = [1,#,2,3,#,4,5,6,7,#]"
    arr = [1, 2,3, 4,5,6,7]
    test(arr, comment)

    comment = "Tree w/ depth 4"
    arr = [1, 2,3, 4,5,6,7, 8,9,10,11,12,13,14,15]
    test(arr, comment)

    comment = ""
    arr = [1,None,3,None,7]
    test(arr, comment)

    comment = ""
    arr = [1, 2,3, 4,None,None,7, 8,None,None,15]
    test(arr, comment)

    comment = "LC example; answer = [1,#,2,3,#,4,5,7,#]"
    arr = [1,2,3,4,5,None,7]
    test(arr, comment)
