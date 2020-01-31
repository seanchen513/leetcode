"""
113. Path Sum II
Medium

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.
"""

from typing import List
import collections

#import sys
#sys.path.insert(1, '../tree/')
from binary_tree import TreeNode, print_tree, array_to_bt #, array_to_bt_lc, bt_find

###############################################################################
"""
Typical solution.
DFS using recursion.
"""
class Solution:
    def path_sum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        def dfs(node, path=[], path_sum=0):
            if not node:
                return
            
            # path.append(node.val) # doesn't work; wrong answers
            # path += [node.val] # doesn't work; wrong answers
            path = path + [node.val] # create new path object

            path_sum += node.val
            
            if not node.left and not node.right and path_sum == target_sum:
                paths.append(path)
            
            dfs(node.left, path, path_sum)
            dfs(node.right, path, path_sum)
        
        paths = []
        dfs(root)

        return paths

###############################################################################
"""
DFS using recursion.
Instead of passing list for path from root for each node, 
path_sum() stores the leaf.  Afterwards, the leaves are processed
to get paths from root to leaves.

SLOW.

O(n) time
O(?) extra space
"""
class Solution1b:
    def path_to_node(self, root, node, path=[]):
        if root is None:
            return None

        if (root == node
            or self.path_to_node(root.left, node, path) 
            or self.path_to_node(root.right, node, path)
        ):
            path.append(root.val)
            # path = path + [root.val] # doesn't work
            return path

        return None

    def path_sum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        def dfs(node, path_sum=0):
            if not node:
                return

            path_sum += node.val
            
            if not node.left and not node.right and path_sum == target_sum:
                leaves.append(node)
            
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)
        
        leaves = []
        dfs(root)
        #print(f"leaves = {[leaf.val for leaf in leaves]}")

        paths = []
        for leaf in leaves:
            paths.append(self.path_to_node(root, leaf, [])[::-1])

        return paths

###############################################################################
"""
Nice solution.
DFS using recursion.
Propagates target sum for subpaths, and returns non-empty subpaths only 
for subpaths that meet target sums.

https://leetcode.com/problems/path-sum-ii/discuss/36802/Short-python-solution
"""
class Solution1c:
    def path_sum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        if not root:
            return []

        if not root.left and not root.right and root.val == target_sum:
            return [[root.val]]
            # if leaf node and root.val != target_sum, will return [] later

        subpaths = self.path_sum(root.left, target_sum - root.val) \
            + self.path_sum(root.right, target_sum - root.val)
        
        # if subpaths is [], then this returns []
        return [[root.val] + subpath for subpath in subpaths]

###############################################################################
"""
DFS preorder using stack.
"""
class Solution2:
    def path_sum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        paths = []

        stack = [(root, [], 0)]

        while stack:
            curr, path, path_sum = stack.pop()

            if curr:
                path = path + [curr.val]

                path_sum += curr.val

                if not curr.left and not curr.right and path_sum == target_sum:
                    paths.append(path)

                stack.extend([(curr.left, path, path_sum), (curr.right, path, path_sum)])

        return paths
        
###############################################################################
"""
BFS using lists.

O(n) time
O(?) extra space
"""
class Solution3:
    def path_sum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        paths = []
        level = [(root, [], 0)] # for bfs
        
        while level:
            next_level = []
            
            for curr, path, path_sum in level:
                if curr:
                    #path.append(curr.val) # doesn't work; wrong answers
                    #path += [curr.val] # doesn't work; wrong answers
                    path = path + [curr.val] # create new path object

                    path_sum += curr.val
                    
                    if not curr.left and not curr.right and path_sum == target_sum:
                        paths.append(path)
            
                    next_level.extend([
                        (curr.left, path, path_sum), 
                        (curr.right, path, path_sum)])
            
            level = next_level
        
        return paths
        
###############################################################################
"""
BFS using queue.

O(n) time
O(?) extra space
"""
class Solution3b:
    def path_sum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        paths = []
        queue = collections.deque([(root, [], 0)]) # for bfs
        
        while queue:
            for _ in range(len(queue)):
                curr, path, path_sum = queue.popleft()

                if curr:
                    #path.append(curr.val) # doesn't work; wrong answers
                    #path += [curr.val] # doesn't work; wrong answers
                    path = path + [curr.val] # create new path object

                    path_sum += curr.val
                    
                    if not curr.left and not curr.right and path_sum == target_sum:
                        paths.append(path)
            
                    queue.extend([
                        (curr.left, path, path_sum), 
                        (curr.right, path, path_sum)])
                   
        return paths
        
###############################################################################
        
if __name__ == "__main__":
    # LC113. example
    arr = [5,4,8,11,None,13,4,7,2,None,None,None,None,5,1] 
    target_sum = 22

    nodes = array_to_bt(arr)
    root = nodes[0]
    print_tree(root)

    s = Solution1c()
    paths = s.path_sum(root, target_sum)

    print(f"\npaths with target sum {target_sum}:\n")
    print(paths)
