"""
270. Closest Binary Search Tree Value
Easy

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


###############################################################################
"""
Solution: binary search on tree.

Possible to check target == root.val and return early.

O(h) time, which is O(n) worst case when tree is linear
O(1) extra space
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        min_diff = float('inf')
        val = None

        while root:
            if abs(target - root.val) < min_diff:
                min_diff = abs(target - root.val)
                val = root.val

            if target < root.val:
                root = root.left
            else:
                root = root.right

        return val

"""
Solution: more concise version
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        val = root.val

        while root:
            val = min(val, root.val, lambda x: abs(target - x))
            root = root.left if target < root.val else root.right

        return val

###############################################################################
"""
Solution: iterative inorder using stack. Return early if we find a node with
value >= target.

This works well when k << n.

O(k) time ~ O(n)
O(1) extra space
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        prev = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if target <= root.val:
                return min(prev, root.val, key=lambda x: abs(target -x))
            
            prev = root.val
            root = root.right

        return prev

"""
Solution: same, but don't use min() with lambda.
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        prev = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if target <= root.val:
                if root.val - target < target - prev:
                    return root.val
                else:
                    return prev
            
            prev = root.val
            root = root.right

        return prev

"""
Solution: same, but use recursion (messy).

Inorder traversal using recursion. Return early if we find a node with
value >= target.

This works well when k << n.
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(root):
            nonlocal val, prev
        
            if (val != None) or not root:
                return

            inorder(root.left)
            if val != None:
                return

            if root.val >= target:
                if root.val - target < target - prev:
                    val = root.val
                else:
                    val = prev
                return
                    
            prev = root.val
            inorder(root.right)
        
        val = None
        prev = float('-inf')
        
        inorder(root)

        return val if val != None else prev

###############################################################################
"""
Solution: recursion to traverse tree and check each node. Use nonlocal vars
min_diff and val (for tree value giving min diff).

O(n) time
O(1) extra space
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs(root):
            nonlocal min_diff, val
        
            if not root:
                return

            diff = abs(root.val - target)
            if diff < min_diff:
                min_diff = diff
                val = root.val

            dfs(root.left)
            dfs(root.right)
        
        min_diff = float('inf')
        val = None
        
        dfs(root)

        return val

"""
Solution: same but use list to hold min_diff and val, and have recursive
function accept list as parameter.
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs(root, res):
            if not root:
                return

            diff = abs(root.val - target)
            if diff < res[0]:
                res[0] = diff
                res[1] = root.val

            dfs(root.left, res)
            dfs(root.right, res)
        
        res = [float('inf'), None] # min_diff, val
        dfs(root, res)

        return res[1] # val corresponding to min_diff

"""
Solution: same, but min_diff and val are parameters and return values.
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs(root, min_diff, val):
            if not root:
                return min_diff, val

            diff = abs(root.val - target)
            if diff < min_diff:
                min_diff = diff
                val = root.val

            min_diff, val = dfs(root.left, min_diff, val)
            min_diff, val = dfs(root.right, min_diff, val)

            return min_diff, val
        
        _, val = dfs(root, float('inf'), None)

        return val

###############################################################################
"""
Solution: use inorder traversal to get sorted array of values, then do 
binary search on sorted array.

O(n) time
O(n) extra space
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(node, arr):
            if not node:
                return
            
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
            
        arr = []
        inorder(root, arr)
        print(arr)
        
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] < target:
                lo = mid + 1
            else:
                hi = mid
                
        print(f"lo={lo}")
        
        if lo == 0:
            return arr[0]
        if lo == len(arr):
            return arr[-1]
        
        if target - arr[lo-1] < arr[lo] - target:
            return arr[lo-1]
        
        return arr[lo]

###############################################################################
"""
Solution: use recursive traversal to get array of values, then use
min() on array with lambda. Traversal doesn't need to be inorder.

O(n) time
O(n) extra space
"""
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return min(inorder(root), key=lambda x: abs(target - x))
