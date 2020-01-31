"""
1123. Lowest Common Ancestor of Deepest Leaves
Medium

Given a rooted binary tree, return the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Explanation: 
The deepest leaves are the nodes with values 2 and 3.
The lowest common ancestor of these leaves is the node with value 1.
The answer returned is a TreeNode object (not an array) with serialization "[1,2,3]".

Example 2:

Input: root = [1,2,3,4]
Output: [4]

Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 
Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt_lc

###############################################################################
"""
Solution 1.

There may be 1, 2, or more deepest leaves.  They all occur at the same level.

Idea: find paths from root to each of the deepest leaves.  The paths will agree
up to their LCA.


"""
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def paths_to_deepest_leaves(node, path=[], max_depth=[0]):
            if not node:
                return

            path = path + [node] # create new object
            depth = len(path)

            if not node.left and not node.right: # leaf
                if depth > max_depth[0]:
                    max_depth[0] = depth
                    self.paths = [path]
                elif depth == max_depth[0]:
                    self.paths.append(path)

            paths_to_deepest_leaves(node.right, path, max_depth)
            paths_to_deepest_leaves(node.left, path, max_depth)

        self.paths = []
        paths_to_deepest_leaves(root)
        
        num_paths = len(self.paths)

        if num_paths == 1:
            return self.paths[0][-1]

        # Now, there are at least 2 deepest leaves, so their paths differ
        # at some point.

        path0 = self.paths[0] # take 1st path as base of comparison

        for level in range(len(path0)): # index along each path; ie, level/depth
            val = path0[level] 
        
            for path_num in range(1, num_paths): # which path
                if self.paths[path_num][level] != val:
                    return path0[level-1]

###############################################################################
"""
Solution 1b: just like sol #1 with small changes:

1. use "nonlocal paths" instead of "self.paths"
2. move max_depth out of paths_to_deepest_leaves()
3. pass "depth" around instead of doing "depth = len(path)"
"""
class Solution1b:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def paths_to_deepest_leaves(node, path=[], depth=0):
            nonlocal paths, max_depth

            if not node:
                return

            path = path + [node] # create new object
            #depth = len(path)

            if not node.left and not node.right: # leaf
                if depth > max_depth:
                    max_depth = depth
                    paths = [path]
                elif depth == max_depth:
                    paths.append(path)

            paths_to_deepest_leaves(node.right, path, depth + 1)
            paths_to_deepest_leaves(node.left, path, depth + 1)

        paths = []
        max_depth = 0
        paths_to_deepest_leaves(root)
        
        num_paths = len(paths)

        if num_paths == 1:
            return paths[0][-1]

        # Now, there are at least 2 deepest leaves, so their paths differ
        # at some point.

        path0 = paths[0] # take 1st path as base of comparison

        for level in range(len(path0)): # index along each path; ie, level/depth
            val = path0[level] 
        
            for path_num in range(1, num_paths): # which path
                if paths[path_num][level] != val:
                    return path0[level-1]

###############################################################################
"""
Solution 2: Postorder recursion with subtree heights and LCA

Base cases:
    node is None: height = 0, LCA is None
    node is leaf: height = 1, LCA is leaf itself (so far)

Induction step:
    case 1 (subtree heights are equal): LCA is node itself (so far)
    case 2 (left subtree deeper): LCA is LCA from left subtree
    case 3 (right subtree deeper): LCA is LCA from right subtree

O(n) time since single pass
O(h) extra space for recursion stack

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution
"""
class Solution2:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(root): # returns (subtree height, LCA)
            if not root:
                return 0, None

            height1, lca1 = helper(root.left)
            height2, lca2 = helper(root.right)

            if height1 > height2:
                return height1 + 1, lca1
            elif height1 < height2:
                return height2 + 1, lca2

            return height1 + 1, root # leaves return (1, themselves)

        return helper(root)[1]

###############################################################################
"""
Solution 3: Postorder recursion using subtree depths.

The LCA node must have deepest leaves in both subtrees.  So the depths of
its two subtrees must be equal, and also equal to the maximum depth in the
entire tree.

This condition might be fulfilled more than once in the process of
recursion, while the max depth is still being updated/calculated.  
(Anytime this happens, that node is the LCA of the deepest nodes
*for that subtree*.)  However, since we are doing *postorder* recursion, 
the actual LCA of deepest nodes for the entire tree will be the last
one found.

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577/JavaC%2B%2BPython-Two-Recursive-Solution
"""
class Solution3:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def helper(node, depth):
            self.deepest = max(self.deepest, depth)

            if not node:
                return depth

            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)

            if left == right == self.deepest:
                self.lca = node
            
            return max(left, right)

        self.deepest = 0
        self.lca = None
        
        helper(root, 0)

        return self.lca

###############################################################################

if __name__ == "__main__":
    def test(arr):
        root = array_to_bt_lc(arr)
        solutions = [Solution(), Solution1b(), Solution2(), Solution3()]

        lcas = [s.lcaDeepestLeaves(root) for s in solutions]
        lca_vals = [lca.val for lca in lcas]

        print("#"*80)
        print(arr)
        print()
        print_tree(root)
        print(f"\nLCA of deepest leaves (all solutions) = {lca_vals}\n")

    arrays = [
        [0],
        [1],
        [1,2],
        [1,2,3], # LC ex1; answr = TreeNode for [1,2,3]
        [1,2,3,4], # LC ex2; answer = TreeNode for [4]
        [1,2,3,4,5], # LC ex3; answer = TreeNode for [2,4,5]
        [1,2,3,None,None,6,7],
        [1,2,3,4,5,6,7],
    ]

    for arr in arrays:
        test(arr)
