"""
118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import List

###############################################################################
"""
Solution 1:

This can be considered DP.

O(n^2) time, where n = number of rows.
O(n^2) extra space for result.
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        res = [[1]]
        
        for r in range(1, numRows): # row num 1 to numRows-1
            row = [1]
            
            for j in range(1, r):
                row.append(res[-1][j-1] + res[-1][j])
            
            row.append(1)
            res.append(row)
            
        return res

"""
Solution 1b: same as sol 1, but Pythonic.

https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.

  0 1 3 3 1
+ 1 3 3 1 0
-----------
= 1 4 6 4 1

"""
class Solution1b:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for _ in range(1, numRows): # row num 1 to numRows-1
            res += [list(map(lambda x,y: x+y, res[-1] + [0], [0] + res[-1]))]

        return res if numRows else []

"""
Solution 1c: same as sol 1b, but use operator.add instead of lambda.
"""
import operator
class Solution1c:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for _ in range(1, numRows): # row num 1 to numRows-1
            row = map(operator.add, res[-1] + [0], [0] + res[-1])
            res.append(list(row))

        return res if numRows else []

"""
Solution 1d: same as sol 1, but use zip.
"""
class Solution1d:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for _ in range(1, numRows): # row num 1 to numRows-1
            row = [x + y for x, y in zip(res[-1] + [0], [0] + res[-1])]
            res.append(row)

        return res if numRows else []

###############################################################################
"""
Solution 2: use combinatorial recurrence relation.

LC: when doing x *= (r - k + 1)/k and taking int() afterwards, get wrong 
answer for n = 15, probably due to issue with division.

C(n,k) = C(n, k-1) * (n - k + 1) / k
"""
        
class Solution2:
    def generate(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        
        res = [[1]]

        for r in range(1, n):
            row = [1]

            x = 1
            for k in range(1, r+1):
                x = int(x * (r - k + 1) / k)
                row.append(x)

            res.append(row)

        return res

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"n = {n}")
        
        res = sol.generate(n)

        print(f"\nres = {res}")


    sol = Solution() # DP
    sol = Solution1b() # DP, Pythonic w/ lambda
    sol = Solution1c() # DP, Pythonic w/ oeprator.add
    sol = Solution1c() # DP, Pythonic w/ zip

    #sol = Solution2() # use combinatorial recurrence relation

    comment = "LC ex1"
    n = 5
    test(n, comment)
   
    comment = "trivial case"
    n = 0
    test(n, comment)

    comment = "trivial case"
    n = 1
    test(n, comment)
