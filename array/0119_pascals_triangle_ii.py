"""
119. Pascal's Triangle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

from typing import List

###############################################################################
"""
Solution 1: use combinatorial recurrence relation.

C(n,k) = C(n, k-1) * (n - k + 1) / k

O(n) time
O(n) extra space: for result
"""
class Solution:
    #def getRow(self, rowIndex: int) -> List[int]:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]

        row = [1]

        x = 1
        for k in range(1, n+1):
            x = int(x * (n - k + 1) / k)
            row.append(x)

        return row

###############################################################################
"""
Solution 2: memory-efficient DP

Approach 3 here:
https://leetcode.com/problems/pascals-triangle-ii/solution/

Compared to regular DP:
1. Same time/space complexities.
2. One array instead of two. So memory consumption is roughly half.
3. No time wasted in swapping references to vectors for previous and current row.
4. Locality of reference.  Since every read is for consecutive memory locations 
in the array, we get a performance boost.

O(n^2) time
O(n) extra space: for result only
"""
class Solution2:
    #def getRow(self, rowIndex: int) -> List[int]:
    def getRow(self, n: int) -> List[int]:
        # if n == 0:
        #     return [1]

        row = [1]*(n+1)

        for i in range(n):
            for j in range(i, 0, -1):
                row[j] += row[j-1]

        return row

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"n = {n}")
        
        res = sol.getRow(n)

        print(f"\nres = {res}\n")


    sol = Solution() # combinatorial recurrence relation
    sol = Solution2() # memory-efficient DP

    comment = "LC ex1; answer = [1,3,3,1]"
    n = 3
    test(n, comment)
   
    comment = "trivial case"
    n = 0
    test(n, comment)

    comment = "trivial case"
    n = 1
    test(n, comment)

    comment = ""
    n = 2
    test(n, comment)

    comment = "LC max n=33"
    n = 33
    test(n, comment)
