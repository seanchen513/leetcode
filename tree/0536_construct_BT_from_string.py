"""
536. Construct Binary Tree from String
Medium

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   

Note:
There will only be '(', ')', '-' and '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".
"""

#import sys
#sys.path.insert(1, '../tree/')

from binary_tree import TreeNode, print_tree, array_to_bt, array_to_bt_lc
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

###############################################################################
"""
Solution: iterative using stack to store tree nodes.

Extra: added code to allow nodes to have a right child while not having a
left child.

O(n) time
O(h) extra space: for stack

Example:
4(2(3)(1) )(6(5) )
     3  1 2    5 6 stack pops
at end, stack ~ [4]

Runtime: 92 ms, faster than 99.41% of Python3 online submissions
Memory Usage: 14.5 MB, less than 33.33% of Python3 online submissions
"""
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        stack = []
        i = 0

        while i < n:
            if s[i] == ')':
                if s[i-1] != '(': # to deal with non-nodes specified by ()                
                    stack.pop()
                i += 1

            elif s[i] != '(': # '-' or digit
                # read from ( to next ( or )
                start = i
                while i < n and s[i] not in ['(', ')']:
                    i += 1

                node = TreeNode(int(s[start:i]))

                if stack:
                    parent = stack[-1]
                    if parent.left or s[start-3:start-1] == '()':
                        parent.right = node
                    else:
                        parent.left = node

                stack.append(node)
            
            else:
                i += 1

        return stack[-1] if stack else None

"""
Solution 1b: same but index i is handled differently.
"""
class Solution1b:
    def str2tree(self, s: str) -> TreeNode:
        n = len(s)
        stack = []
        i = 0

        while i < n:
            if s[i] == ')':
                if s[i-1] != '(': # to deal with non-nodes specified by ()
                    stack.pop()

            elif s[i] != '(': # '-' or digit
                # read from ( to next ( or )
                start = i
                while i+1 < n and s[i+1] not in ['(', ')']:
                   i += 1

                node = TreeNode(int(s[start:i+1]))

                if stack:
                    parent = stack[-1]
                    if parent.left or s[start-3:start-1] == '()':
                        parent.right = node
                    else:
                        parent.left = node

                stack.append(node)
            
            i += 1

        return stack[-1] if stack else None

###############################################################################
"""
Solution 2: recursion on string index, and return node and index.

O(n) time
O(h) extra space

Runtime: 84 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 14.5 MB, less than 33.33% of Python3 online submissions
"""
class Solution2:
    def str2tree(self, s: str) -> TreeNode:
        def dfs(i):
            # Check if subtree is empty.
            if s[i] in ['(', ')']:
               return None, i

            start = i
            
            # while i < n and (s[i] == '-' or s[i].isdigit()):
            while i < n and s[i] not in ['(', ')']:
                i += 1

            # if start == i: # alternative to checking s[i] at start
            #     return None, i

            node = TreeNode(int(s[start:i]))

            if i < n and s[i] == '(': # left subtree
                i += 1 # skip '('
                node.left, i = dfs(i)
                i += 1 # skip ')'
            
            if i < n and s[i] == '(': # right subtree
                i += 1 # skip '('
                node.right, i = dfs(i)
                i += 1 # skip ')'
            
            return node, i

        if not s:
            return None
        
        n = len(s)
        
        return dfs(0)[0]

###############################################################################
"""
Solution 3: recursion; use net count of parentheses to find numbers.

Cases for string
1. empty string
2. int
3. int (left subtree)
4. int (left subtree) (right subtree)

O() time
O() extra space

Runtime: 260 ms, faster than 10.11% of Python3 online submissions
Memory Usage: 14.5 MB, less than 33.33% of Python3 online submissions
"""
class Solution3:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None

        # Find first '('
        i = s.find('(')
        if i < 0:
            return TreeNode(int(s))

        # Find index j of char ')' that ends left subtree
        net = 0
        j = i

        while j < len(s):
            if s[j] == '(':
                net += 1
            elif s[j] == ')':
                net -= 1

            if net == 0:
                break
                
            j += 1

        root = TreeNode(int(s[:i]))
        root.left = self.str2tree(s[i+1:j]) # exclude parentheses at this level
        root.right = self.str2tree(s[j+2:-1]) # exclude parentheses at this level

        return root

"""
Solution 3b: same, but pass string indices instead of string copies.

Runtime: 176 ms, faster than 40.24% of Python3 online submissions
Memory Usage: 14.3 MB, less than 33.33% of Python3 online submissions
"""
class Solution3b:
    def str2tree(self, s: str) -> TreeNode:
        def dfs(start, end):
            if start >= end:
                return None

            # Find first '('
            i = s.find('(', start, end)
            if i < 0:
                return TreeNode(int(s[start:end]))

            # Find index j of char ')' that ends left subtree
            net = 0

            for j in range(i, end):
                if s[j] in d:
                    net += d[s[j]]

                if net == 0:
                    break

            root = TreeNode(int(s[start:i]))
            root.left = dfs(i+1, j) # exclude parentheses at this level
            root.right = dfs(j+2, end-1) # exclude parentheses at this level

            return root
        
        d = {'(': 1, ')': -1}
        
        return dfs(0, len(s))

###############################################################################
"""
Solution 4: Python hack using eval().

Change string like '4(2(3)(1))(6(5))' to 't(4,t(2,t(3),t(1)),t(6,t(5)))'
and evaluate with eval().

https://leetcode.com/problems/construct-binary-tree-from-string/discuss/100404/Python-hack

"""
class Solution4:
    def str2tree(self, s):
        def t(val=None, left=None, right=None):
            if not val:
                return None

            return TreeNode(val, left, right)

        return eval('t(' + s.replace('(', ',t(') + ')') if s else None

"""
Solution 4b: original version that doesn't work if there are nodes with
a right child but no left child.
"""
class Solution4b:
    def str2tree(self, s):
        def t(val, left=None, right=None):
            return TreeNode(val, left, right)

        return eval('t(' + s.replace('(', ',t(') + ')') if s else None

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\nstring = {s}")

        res = sol.str2tree(s)

        print()
        print_tree(res)
        print()


    sol = Solution() # iterative using stack to store tree nodes
    #sol = Solution1b() # same but treat string index differently

    #sol = Solution2() # recursion on string index, and return node and index.
       
    #sol = Solution3() # recursion; use net count of parentheses to find numbers.
    #sol = Solution3b() # same, but pass string indices instead of substrings
    
    #sol = Solution4() # Python hack using eval()
    #sol = Solution4b() # original version that doesn't work for...
    
    comment = "LC example; answer = [4,2,6,3,1,5]"
    s = "4(2(3)(1))(6(5))"
    test(s, comment)

    comment = "LC TC; answer = [4,2,6,3,null,5,7]"
    s = "4(2(3))(6(5)(7))"
    test(s, comment)

    comment = "LC TC; answer = [1,2,null,3,null,4,null,5,null,6,null,7,null,8]"
    s = "1(2(3(4(5(6(7(8)))))))"
    test(s, comment)

    comment = "LC TC with negative int"
    s = "-4(2(3)(1))(6(5)(7))"
    test(s, comment)

    comment = "an empty left subtree (not part of problem)"
    s = "4(2()(3))(6(5)(7))"
    test(s, comment)

    comment = "empty left and right subtrees specified by ()"
    s = "4(2()())(6(5)(7))"
    test(s, comment)

    comment = "empty left subtree specified by ()"
    s = "4(2()(0()(8)))(6(5)(7))"
    test(s, comment)

    comment = ""
    s = "1()(2()(3()(4())))"
    test(s, comment)
