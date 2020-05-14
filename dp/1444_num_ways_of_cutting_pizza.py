"""
1444. Number of Ways of Cutting a Pizza
Hard

Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""

from typing import List

###############################################################################
"""
Solution: DP memo.

Runtime: 404 ms, faster than 57.31% of Python3 online submissions
Memory Usage: 18.9 MB, less than 100.00% of Python3 online submissions
"""
import functools
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @functools.lru_cache(None)
        def calc_d(r, c): # num apples in row/col starting at (r,c)
            dr = [0] * m
            dc = [0] * n

            for i in range(r, m):    
                p = pizza[i]
                dr[i] = p[c:].count('A')

                for j in range(c, n):
                    if p[j] == 'A':
                        #dr[i] += 1
                        dc[j] += 1

            return dr, dc

        @functools.lru_cache(None)
        def rec(r, c, k, n_apples):
            if k > n_apples:
                return 0

            if k == 1:
                return 1

            count = 0
            dr, dc = calc_d(r, c)

            # horizontal cut that creates bottom half starting at row i+1
            s = 0 # count of apples up to row i
            for i in range(r, m-1):
                s += dr[i]

                if s > 0:
                    count += rec(i+1, c, k-1, n_apples - s)

            # vertical cut that creates right half starting at column j+1
            s = 0 # count of apples up to column j
            for j in range(c, n-1):
                s += dc[j]

                if s > 0:
                    count += rec(r, j+1, k-1, n_apples - s)

            return count % mod

        m = len(pizza)
        n = len(pizza[0])
        mod = 10**9 + 7

        n_apples = sum(row.count('A') for row in pizza)

        return rec(0, 0, k, n_apples)

###############################################################################
"""
Solution 2: same, but precalculate dr and dc matrices.

Runtime: 212 ms, faster than 95.91% of Python3 online submissions
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions
"""
import functools
class Solution2:
    def ways(self, pizza: List[str], k: int) -> int:
        @functools.lru_cache(None)
        def rec(r, c, k, n_apples):
            if k > n_apples:
                return 0

            if k == 1:
                return 1

            count = 0

            # horizontal cut that creates bottom half starting at row i+1
            s = 0 # count of apples up to row i
            for i in range(r, m-1):
                s += dr[i][c]

                if s > 0:
                    count += rec(i+1, c, k-1, n_apples - s)

            # vertical cut that creates right half starting at column j+1
            s = 0 # count of apples up to column j
            for j in range(c, n-1):
                s += dc[r][j]

                if s > 0:
                    count += rec(r, j+1, k-1, n_apples - s)

            return count % mod

        m = len(pizza)
        n = len(pizza[0])
        mod = 10**9 + 7

        # Precalculate matrices giving num apples in row/col starting at (r,c).
        # Dummy final row and dummy final column of 0's.
        dr = [[0] * (n+1) for _ in range(m+1)]
        dc = [[0] * (n+1) for _ in range(m+1)]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                dr[r][c] = dr[r][c+1] + (pizza[r][c] == 'A')
                dc[r][c] = dc[r+1][c] + (pizza[r][c] == 'A')

        n_apples = sum(dr[r][0] for r in range(m))

        return rec(0, 0, k, n_apples)

###############################################################################
"""
Solution 3: same, but precalculate matrix giving num apples starting at (r,c).

horizontal cut
valid if 
- num apples above cut > 0
- num apples below cut > 0

let n = num_apples

num apples in row starting at (r,c)
= n[r][c] - n[r+1][c]

num apples in column starting at (r,c)
= n[r][c] - n[r][c+1]


O(k*m*n*(m+n)) time: there are k*m*n total states, and each state needs max of
m+n cuts

O(k*m*n) extra space: for memoization of k*m*n total states.

These are probably not tight bounds.

Runtime: 236 ms, faster than 88.05% of Python3 online submissions
Memory Usage: 15.4 MB, less than 100.00% of Python3 online submissions
"""
import functools
class Solution3:
    def ways(self, pizza: List[str], k: int) -> int:
        @functools.lru_cache(None)
        def rec(r, c, k):
            if k > num_apples[r][c]:
                return 0

            if k == 1:
                return 1

            count = 0

            # horizontal cut that creates bottom half starting at row i+1
            s = 0 # count of apples up to row i
            for i in range(r, m-1):
                s += num_apples[i][c] - num_apples[i+1][c] # dr[i][c] in other sols

                if s > 0:
                    count += rec(i+1, c, k-1)

            # vertical cut that creates right half starting at column j+1
            s = 0 # count of apples up to column j
            for j in range(c, n-1):
                s += num_apples[r][j] - num_apples[r][j+1] # dc[r][j] in other sols

                if s > 0:
                    count += rec(r, j+1, k-1)

            return count % mod

        m = len(pizza)
        n = len(pizza[0])
        mod = 10**9 + 7

        # Precalculate matrix giving num apples starting at (r,c).
        # Dummy final row and dummy final column of 0's.
        num_apples = [[0] * (n+1) for _ in range(m+1)]
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                num_apples[r][c] = (num_apples[r][c+1] + num_apples[r+1][c]
                    - num_apples[r+1][c+1] + (pizza[r][c] == 'A'))
                
        #for row in num_apples:
        #    print(row)

        return rec(0, 0, k)

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        res = sol.ways(arr, k)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution2()
    sol = Solution3()

    comment = "LC ex1; answer = 3"
    arr = ["A..","AAA","..."]
    k = 3
    test(arr, k, comment)

    comment = "LC ex2; answer = 1"
    arr = ["A..","AA.","..."]
    k = 3
    test(arr, k, comment)

    comment = "LC ex3; answer = 1"
    arr = ["A..","A..","..."]
    k = 1
    test(arr, k, comment)

    comment = "LC TC; answer = 39"
    arr = ["AAAA.","A..A.","AA.AA"]
    k = 5
    test(arr, k, comment)

    """
    . A . . A
    A . A . .
    A . A A .
    A A A A .
    A . A A .
    """
    comment = "LC TC; answer = 153"
    arr = [".A..A","A.A..","A.AA.","AAAA.","A.AA."]
    k = 5
    test(arr, k, comment)

    comment = "LC TC; answer = 641829390"
    arr = ["..A.A.AAA...AAAAAA.AA..A..A.A......A.AAA.AAAAAA.AA","A.AA.A.....AA..AA.AA.A....AAA.A........AAAAA.A.AA.","A..AA.AAA..AAAAAAAA..AA...A..A...A..AAA...AAAA..AA","....A.A.AA.AA.AA...A.AA.AAA...A....AA.......A..AA.","AAA....AA.A.A.AAA...A..A....A..AAAA...A.A.A.AAAA..","....AA..A.AA..A.A...A.A..AAAA..AAAA.A.AA..AAA...AA","A..A.AA.AA.A.A.AA..A.A..A.A.AAA....AAAAA.A.AA..A.A",".AA.A...AAAAA.A..A....A...A.AAAA.AA..A.AA.AAAA.AA.","A.AA.AAAA.....AA..AAA..AAAAAAA...AA.A..A.AAAAA.A..","A.A...A.A...A..A...A.AAAA.A..A....A..AA.AAA.AA.AA.",".A.A.A....AAA..AAA...A.AA..AAAAAAA.....AA....A....","..AAAAAA..A..A...AA.A..A.AA......A.AA....A.A.AAAA.","...A.AA.AAA.AA....A..AAAA...A..AAA.AAAA.A.....AA.A","A.AAAAA..A...AAAAAAAA.AAA.....A.AAA.AA.A..A.A.A...","A.A.AA...A.A.AA...A.AA.AA....AA...AA.A..A.AA....AA","AA.A..A.AA..AAAAA...A..AAAAA.AA..AA.AA.A..AAAAA..A","...AA....AAAA.A...AA....AAAAA.A.AAAA.A.AA..AA..AAA","..AAAA..AA..A.AA.A.A.AA...A...AAAAAAA..A.AAA..AA.A","AA....AA....AA.A......AAA...A...A.AA.A.AA.A.A.AA.A","A.AAAA..AA..A..AAA.AAA.A....AAA.....A..A.AA.A.A...","..AA...AAAAA.A.A......AA...A..AAA.AA..A.A.A.AA..A.",".......AA..AA.AAA.A....A...A.AA..A.A..AAAAAAA.AA.A",".A.AAA.AA..A.A.A.A.A.AA...AAAA.A.A.AA..A...A.AAA..","A..AAAAA.A..A..A.A..AA..A...AAA.AA.A.A.AAA..A.AA..","A.AAA.A.AAAAA....AA..A.AAA.A..AA...AA..A.A.A.AA.AA",".A..AAAA.A.A.A.A.......AAAA.AA...AA..AAA..A...A.AA","A.A.A.A..A...AA..A.AAA..AAAAA.AA.A.A.A..AA.A.A....","A..A..A.A.AA.A....A...A......A.AA.AAA..A.AA...AA..",".....A..A...A.A...A..A.AA.A...AA..AAA...AA..A.AAA.","A...AA..A..AA.A.A.AAA..AA..AAA...AAA..AAA.AAAAA...","AA...AAA.AAA...AAAA..A...A..A...AA...A..AA.A...A..","A.AA..AAAA.AA.AAA.A.AA.A..AAAAA.A...A.A...A.AA....","A.......AA....AA..AAA.AAAAAAA.A.AA..A.A.AA....AA..",".A.A...AA..AA...AA.AAAA.....A..A..A.AA.A.AA...A.AA","..AA.AA.AA..A...AA.AA.AAAAAA.....A.AA..AA......A..","AAA..AA...A....A....AA.AA.AA.A.A.A..AA.AA..AAA.AAA","..AAA.AAA.A.AA.....AAA.A.AA.AAAAA..AA..AA.........",".AA..A......A.A.AAA.AAAA...A.AAAA...AAA.AAAA.....A","AAAAAAA.AA..A....AAAA.A..AA.A....AA.A...A.A....A..",".A.A.AA..A.AA.....A.A...A.A..A...AAA..A..AA..A.AAA","AAAA....A...A.AA..AAA..A.AAA..AA.........AA.AAA.A.","......AAAA..A.AAA.A..AAA...AAAAA...A.AA..A.A.AA.A.","AA......A.AAAAAAAA..A.AAA...A.A....A.AAA.AA.A.AAA.",".A.A....A.AAA..A..AA........A.AAAA.AAA.AA....A..AA",".AA.A...AA.AAA.A....A.A...A........A.AAA......A...","..AAA....A.A...A.AA..AAA.AAAAA....AAAAA..AA.AAAA..","..A.AAA.AA..A.AA.A...A.AA....AAA.A.....AAA...A...A",".AA.AA...A....A.AA.A..A..AAA.A.A.AA.......A.A...A.","...A...A.AA.A..AAAAA...AA..A.A..AAA.AA...AA...A.A.","..AAA..A.A..A..A..AA..AA...A..AA.AAAAA.A....A..A.A"]
    k = 8
    test(arr, k, comment)
