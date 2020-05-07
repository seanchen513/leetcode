"""
993. Cousins in Binary Tree
Easy

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Example 1:

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""

#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

###############################################################################
"""
Solution: BFS with "level" and "next_level" dicts that map each node to its
parent. Check if the given nodes are found at the same level, 
and check if they have the same parent.

O(n) time
O(n) extra space for "level" list
O(n) extra space for storing parents (due to last level)
"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = {root: None} # dict of node -> parent

        while level:
            next_level = {}
            x_node = y_node = None

            for node in level:
                if node.val == x:
                    x_node = node
                elif node.val == y:
                    y_node = node

                if x_node and y_node:
                    return True if level[x_node] != level[y_node] else False
                
                if node.left:
                    next_level[node.left] = node
                if node.right:
                    next_level[node.right] = node

            level = next_level

        # Not both nodes were found, or both are at different levels.
        return False

###############################################################################
"""
Solution 1b: same, but use "level" and "next_level" lists that store tuples
(node, parent). Use "found" dict that maps given nodes (if found) to their parents.
"""
class Solution1b:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [(root, None)]
        
        while level:
            next_level = []
            found = {}
            
            for node, parent in level:
                if node.val == x:
                    found[x] = parent
                elif node.val == y:
                    found[y] = parent
                    
                if node.left:
                    next_level.append((node.left, node))
                if node.right:
                    next_level.append((node.right, node))
                    
            if len(found) == 2:
                return found[x] != found[y]
            elif len(found) == 1:
                return False
                    
            level = next_level
            
        return False

###############################################################################
"""
Solution 1c: same, but use "level" and "next_level" lists. 
Use fact that cousins cannot be adjacent while looping through each level.
One way to do this is to use a loop counter, and store the 
counter as flags for the found nodes.  

Be careful to increment the counter for positions where a node is not present.

Does NOT suffice to check that the two positions are different by 1 (plus/minus).

Use "found" to store positions of found nodes in order they are encountered.
Siblings will have found[1] - found[0] == 1 and each position with a particular
parity depending on the parity of the start position.

O(n) time
O(n) extra space for "level" list (due to last level)
O(1) other extra space
"""
class Solution1c:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        level = [root]

        while level:
            next_level = []
            found = [] # store positions of x or y in order as they are found
            pos = 1 # start with odd position
            # siblings with have positions (odd, even), where even - odd = 1

            for node in level:
                if node:
                    if node.val in (x, y):
                        found += [pos]

                    if len(found) == 2:
                        if found[1] - found[0] == 1 and found[1] % 2 == 0:
                            return False # siblings
                        else:
                            return True
                    
                    next_level.extend([node.left, node.right])

                pos += 1 # do this whether node is None or not

            level = next_level

        # Not both nodes were found, or both are at different levels.
        return False

###############################################################################
"""
Solution 2: Recursion to find the two given nodes.  When each is found, 
store its parent and depth.  After recursion, check.

O(n) time
O(h) extra space for recursion
"""
class Solution2:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, depth=0, parent=None):
            if not node or len(found) == 2:
                return 

            if node.val in (x, y):
                found[node.val] = (parent, depth)

            dfs(node.left, depth + 1, node)
            dfs(node.right, depth + 1, node)

        found = {}
        dfs(root)

        if len(found) == 2:
            if found[x][0] != found[y][0] and found[x][1] == found[y][1]:
                return True

        return False

###############################################################################

if __name__ == "__main__":
    def test(arr, x, y, comment=None):
        root = array_to_bt_lc(arr)
        
        solutions = [Solution(), Solution1b(), Solution1c(), Solution2()]

        res = [s.isCousins(root, x, y) for s in solutions]        

        print("="*80)
        if comment:
            print(comment, "\n")
        print(arr, "\n")

        print_tree(root)

        print(f"\nnodes: {x}, {y}\n")
        print(f"Are cousins (all solutions)? {res}\n")

    comment = "LC example 1; answer = False"
    arr = [1, 2,3, 4]
    x, y = 4, 3
    test(arr, x, y, comment)

    comment = "LC example 2; answer = True"
    arr = [1, 2,3, None,4,None,5]
    x, y = 5, 4
    test(arr, x, y, comment)

    comment = "LC example 3; answer = False"
    arr = [1, 2,3, None,4]
    x, y = 2, 3
    test(arr, x, y, comment)

    comment = "Cousins with adjacent positions"
    arr = [1, 2,3, None,4,5,None]
    x, y = 5, 4
    test(arr, x, y, comment)

    comment = "LC test case; answer = True"
    arr = [1,2,10,3,4,None,20,6,7,5,None,54,25,65,11,38,8,61,16,55,None,34,95,None,None,13,14,None,None,22,9,71,None,47,31,None,98,50,None,None,None,None,29,21,15,32,None,12,19,76,None,62,52,37,49,None,None,83,None,None,None,23,None,27,44,36,42,17,26,39,68,None,None,70,None,None,56,None,46,53,66,None,None,75,24,59,48,None,None,89,84,None,80,18,28,33,None,40,None,None,97,None,90,None,None,None,73,69,None,None,78,None,None,77,35,None,None,None,79,None,None,None,None,None,85,None,30,60,None,None,45,41,64,None,None,None,None,None,None,None,88,82,None,99,None,None,None,None,86,91,None,93,63,81,74,57,None,43,51,96,None,None,None,None,None,None,None,None,None,None,None,None,None,100,67,None,None,None,None,None,None,None,72,None,58,None,None,None,None,None,None,None,None,None,87,92,94]
    x, y = 18, 80
    #test(arr, x, y, comment)
