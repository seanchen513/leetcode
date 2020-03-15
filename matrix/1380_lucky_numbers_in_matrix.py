"""
1380. Lucky Numbers in a Matrix
Easy

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""

from typing import List

###############################################################################
"""
Solution 1: brute force

O(mn) time: since all matrix elements are distinct.
O(min(m,n)) extra space: for output
"""
class Solution:
    def luckyNumbers (self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        
        for i in range(m):
            mn = min(mat[i])
            
            for j in range(n):    
                if mat[i][j] == mn:    
                    if all(mat[k][j] <= mn for k in range(m)):
                        res.append(mn)
      
        return res

###############################################################################
"""
Solution 2: use a set to hold mins from each row, and another set to hold
maxes from each column.  Then take set intersection.

O(mn) time
O(m+n) extra space: for sets
"""
class Solution2:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})

###############################################################################

if __name__ == "__main__":
    def test(mat, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        for row in mat:
            for x in row:
                print(f"{x:3}", end="")
            print()

        res = sol.luckyNumbers(mat)

        print(f"\nres = {res}\n")


    sol = Solution() # brute force
    sol = Solution2() # use sets to hold mins and maxes, and take set intersection

    comment = "LC ex1; answer = [15]"
    mat = [[3,7,8],[9,11,13],[15,16,17]]
    test(mat, comment)

    comment = "LC ex2; answer = [12]"
    mat = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    test(mat, comment)

    comment = "LC ex3; answer = [7]"
    mat = [[7,8],[1,2]]
    test(mat, comment)
