"""
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

from typing import List

###############################################################################
"""
Solution: use backtracking with recursion.

Instead of passing new strings, use preallocated list of strings (list of 
length 2*n, and each string of length 1) and pass index for next parenthesis.

Only builds up expression as long as it remains valid.  Use "left" and
"right" counts for this, and pass them.

Number of elements in the result is the nth Catalan number C(2n,n)/(n+1),
which is bounded asymptotically by (4^n)/(n^(3/2)).

O(4^n / sqrt(n)) time: each sequence has at most n steps during backtracking.

O(same?) extra space for recursion.

Runtime: 20 ms, faster than 99.51% of Python3 online submissions
Memory Usage: 13.1 MB, less than 95.56% of Python3 online submissions
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(left=0, right=0, i=0):
            # i = index of next parentheses to add

            if i == n2:
                res.append("".join(s))
                return               

            if left < n:
                s[i] = "("
                rec(left + 1, right, i + 1)

            if left > right:
                s[i] = ")"
                rec(left, right + 1, i + 1)

        n2 = n * 2
        s = [""] * n2
        res = [] # list of results
        
        rec()

        return res   

###############################################################################
"""
Solution 1b: backtracking using recursion.  Use net count...
"""
class Solution1b:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(net=0, i=0):
            # net = number of opening parentheses minus number of closing ones
            # i = index of next parentheses to add

            if i == n2:
                if net == 0:
                    res.append("".join(s))
                return               

            if net < n2: # ie, not == n
                s[i] = "("
                rec(net + 1, i + 1)

            if net > 0: # ie, not == 0
                s[i] = ")"
                rec(net - 1, i + 1)

        n2 = n * 2
        s = [""] * n2
        res = [] # list of results
        
        rec()

        return res   

###############################################################################
"""
Solution 1c: backtracking using recursion.  Pass modified strings.
"""
class Solution1c:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(s="", left=0, right=0):
            if len(s) == n2:
                res.append("".join(s))
                return               

            if left < n:
                rec(s + "(", left + 1, right)

            if left > right:
                rec(s + ")", left, right + 1)

        n2 = n * 2
        s = [""] * n2
        res = [] # list of results

        rec()

        return res

###############################################################################
"""
Solution 2: Use closure number, recursive.

Intuition: To enumerate something, generally we want to express it as a sum of
disjoint subsets that are easier to count.

Consider the closure number of a valid parentheses sequence S: the least 
index >= 0 so that S[0], S[1], ..., S[2*index+1] is valid. 
Clearly, every parentheses sequence has a unique closure number. 
We can try to enumerate them individually.

Algorithm:
For each closure number c, we know the starting and ending brackets must be at 
index 0 and 2*c + 1.  Then, the 2*c elements between must be a valid sequence, 
plus the rest of the elements must be a valid sequence.

https://leetcode.com/problems/generate-parentheses/solution/

O(4^n / sqrt(n)) time: each sequence has at most n steps during backtracking.

O(4^n / sqrt(n)) extra space.

Runtime: 28 ms, faster than 90.43% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        
        res = []
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-c-1):
                    res.append(f"({left}){right}")

        return res

###############################################################################
"""
Solution 2b: Use closure number, iterative.

O(n^2) time
O(4^n / sqrt(n)) extra space

https://leetcode.com/problems/generate-parentheses/discuss/10127/An-iterative-method

Runtime: 28 ms, faster than 90.43% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution2b:
    def generateParenthesis(self, n: int) -> List[str]:
        # results for c = 0, 1, 2, ..., n
        all_res = [[""]] # base case: c = 0
        
        for i in range(1, n+1):
            res = []
            
            for c in range(i):    
                for left in all_res[c]:
                    for right in all_res[i-c-1]:
                        res.append(f"({left}){right}")

            all_res.append(res)

        return all_res[-1]

###############################################################################
"""
Solution 3: Use bits to represent parentheses.

This isn't faster.
"""
class Solution3:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(left=0, right=0, i=0):
            nonlocal s
            # i = index of next parentheses to add

            if i == n2:
                # convert bits to string of parentheses
                #res.append( f"{s:b}" )
                res.append( f"{s:b}".replace("1", "(").replace("0", ")") )
                return               

            if left < n:
                s &= ~(1 << i) # set ith bit 0
                rec(left + 1, right, i + 1)

            if left > right:
                s |= (1 << i) # set ith bit 1
                rec(left, right + 1, i + 1)

        if n == 0: # without this, would return [')']
            return []

        n2 = n * 2
        s = 0 # n2 bits
        res = [] # list of results
        
        rec()

        return res   

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"n = {n}")

        res = sol.generateParenthesis(n)
        print(f"\nSolution: {res}\n")


    sol = Solution() # backtracking; recursion; pass left, right, and index
    #sol = Solution1b() # backtracking, recursion; pass net and index
    #sol = Solution1c() # backtracking; recursion; pass modified strings
    #sol = Solution2() # use closure number, recursive
    #sol = Solution2b() # use closure number, iterative
    sol = Solution3() # use bits

    comment = ""
    n = 0
    test(n, comment)

    comment = ""
    n = 1
    test(n, comment)

    comment = ""
    n = 2
    test(n, comment)

    comment = "LC example"
    n = 3
    test(n, comment)
