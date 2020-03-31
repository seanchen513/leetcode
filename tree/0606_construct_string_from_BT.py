"""
606. Construct String from Binary Tree
Easy

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

###############################################################################
"""
Solution: recursion, preorder. Only add parentheses when calling the 
recursive function (other than the first time).

O(n) time
O(h) extra space ~ O(n)
"""
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(root):
            if not root:
                return ""
            
            s = str(root.val)

            if not root.left and not root.right:
                return s
            
            if not root.right:
                return s + "(" + dfs(root.left) + ")"

            #if not root.left:
            #    return s + "()(" + dfs(root.right) + ")"
            
            return s + "(" + dfs(root.left) + ")(" +  dfs(root.right) + ")"
         
        return dfs(t)

"""
Solution: same, but instead of concatenating strings, append strings 
to a list. At the end, join the strings in the list.
"""
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def dfs(root):
            if not root:
                return
            
            s = str(root.val)

            if not root.left and not root.right:
                lst.append(s)
                return
            
            if not root.right:
                lst.append(s + "(")
                dfs(root.left)
                lst.append(")")
                return
            
            lst.append(s + "(")
            dfs(root.left)
            lst.append(")(")
            dfs(root.right)
            lst.append(")")

        lst = []
        dfs(t)

        return ''.join(lst)

###############################################################################
"""
Solution: iterative preorder traversal using stack. Use visited set to track
when the subtree of a node has been traversed so that we can add a closing
parenthesis.
"""
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""

        stack = [t]
        s = []
        visited = set()

        while stack:
            t = stack[-1]

            if t in visited:
                stack.pop()
                s.append(")")

            else:
                visited.add(t)
                s.append("(" + str(t.val))

                if (not t.left) and t.right:
                    s.append("()")
                if t.right:
                    stack.append(t.right)
                if t.left:
                    stack.append(t.left)

        return "".join(s)[1:-1] # remove outer parentheses
