"""
296. Best Meeting Point
Hard

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

Example:

Input: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 6 

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance 
             of 2+2+2=6 is minimal. So return 6.
"""

from typing import List
import collections

### Assume there's at least one home.

###############################################################################
"""
Solution: brute force.

O(mnk) time if there are k houses.
O(m^2 n^2) time: nested loops for i, j, and within that a nested loop over 
bases, which might iterate as many as m*n times.

O(mn) extra space: for "bases".

TLE
"""
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        bases = []

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    bases.append((i, j))

        min_d = float('inf')
        #min_pt = (0, 0)

        for i in range(n_rows):
            for j in range(n_cols):
                # Don't use condition "if grid[i][j] == 0" since the people
                # can meet at one of their homes.
                d = 0
                for i0, j0 in bases:
                    d += abs(i - i0) + abs(j - j0)

                if d < min_d:
                    min_d = d
                    #min_pt = (i, j)

        return min_d

###############################################################################
"""
Solution 2: Solve for the min distance in each dimension separately using
brute force.  Then add these min distances.

O(mn + n^2 + m^2) time
O(m + n) extra space

Runtime: 72 ms, faster than 27.18% of Python3 online submissions
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def min_dist(arr):
            n = len(arr)
            #bases = {i: arr[i] for i in range(n) if arr[i] > 0}
            bases = {i: x for i, x in enumerate(arr) if arr[i] > 0}
            min_d = float('inf')
            
            for i in range(n):
                d = 0
                for i0, weight in bases.items():
                    d += abs(i - i0) * weight
                
                if d < min_d:
                    min_d = d
                
            return min_d

        # These comprehensions are faster
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(row) for row in zip(*grid)]

        #row_sums = [0] * n_rows
        #col_sums = [0] * n_cols
        #for i in range(n_rows):
        #    for j in range(n_cols):
        #        row_sums[i] += grid[i][j]
        #        col_sums[j] += grid[i][j]

        return min_dist(row_sums) + min_dist(col_sums)

###############################################################################
"""
Solution 3: Solve for the min distance in each dimension separately by using
sorting to find the median coordinate.

O(mn log mn) time: each of "rows" and "cols" may contain up to mn elements,
and they are sorted.

O(mn) extra space: "rows" and "cols" can hold up to mn elements.

Runtime: 60 ms, faster than 88.89% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        rows = []
        cols = []

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        rows.sort()
        cols.sort()

        r = rows[len(rows) // 2]
        c = cols[len(cols) // 2]
        
        return sum(abs(r - i) + abs(c - j) \
            for i in range(n_rows) for j in range(n_cols) if grid[i][j] == 1)

###############################################################################
"""
Solution 4: Solve each dimension separately.  Find coordinates of homes in 
sorted order, and then calculate their medians.

O(mn) time
O(mn) extra space

Runtime: 64 ms, faster than 69.57% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        rows = []
        cols = []
    
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1: 
                    rows.append(i)

        for j in range(n_cols):
            for i in range(n_rows):
                if grid[i][j] == 1: 
                    cols.append(j)

        r = rows[len(rows) // 2]
        c = cols[len(cols) // 2]
        
        return sum(abs(r - i) + abs(c - j) \
            for i in range(n_rows) for j in range(n_cols) if grid[i][j] == 1)

###############################################################################
""" BEST SOLUTION
Solution 5: Solve each dimension separately.  Find coordinates of homes in 
sorted order with frequencies, and then calculate their medians.

For large grids, the calculation of medians can be improved by starting from
the middle or using bisection.

O(mn) time
O(n + m) extra space

Runtime: 52 ms, faster than 99.03% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution5:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        # These comprehensions are faster than nested loops
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(row) for row in zip(*grid)]

        mid = sum(row_sums) // 2

        s = 0
        for i in range(n_rows):
            s += row_sums[i]
            if s > mid:
                r = i
                break

        s = 0
        for j in range(n_cols):
            s += col_sums[j]
            if s > mid:
                c = j
                break
            
        ### This is O(m + n)
        return sum(abs(r - i)*row_sums[i] for i in range(n_rows)) + \
            sum(abs(c - j)*col_sums[j] for j in range(n_cols))

        ### This is O(mn)
        # return sum(abs(r - i) + abs(c - j) \
        #     for i in range(n_rows) for j in range(n_cols) if grid[i][j] == 1)

###############################################################################
"""
Solution 5b: same as sol #5, but more concise.
"""
class Solution5b:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        res = 0
        
        for grid in (grid, zip(*grid)):
            row_sums = [sum(row) for row in grid]
            mid = sum(row_sums) // 2
            n_rows = len(row_sums)

            s = 0
            for i in range(n_rows):
                s += row_sums[i]
                if s > mid:
                    r = i
                    break

            res += sum(abs(r - i)*row_sums[i] for i in range(n_rows))
                
        return res

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        for row in grid:
            print(row)

        res = sol.minTotalDistance(grid)
        print(f"\nSolution: {res}\n")


    #sol = Solution() # brute force
    #sol = Solution2() # combine 1-d solutions
    #sol = Solution3() # find coordinates oh homes, sort, then use medians
    #sol = Solution4() # find coordinates in sorted order, then use medians
    #sol = Solution5() # BEST SOL; find coords in sorted order w/ freqs
    sol = Solution5b() # same as sol #5b but more concise

    comment = "LC example; answer = 6"
    grid = [
        [1,0,0,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]
    ]
    test(grid, comment)

    comment = "LC test case; answer = 1"
    grid = [
        [1,1]
    ]
    test(grid, comment)

    comment = "Trivial case; answer = 0"
    grid = [
        [1]
    ]
    test(grid, comment)

    comment = "LC test case; answer = 19"
    grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,0,0,1,0],
        [1,1,0,0,0,0,1,0,0],
        [0,0,0,1,1,1,0,0,0]]
    test(grid, comment)

    comment = "LC test case; answer = 49"
    grid = [
        [0,1],
        [0,1],
        [0,1],
        [1,1],
        [0,0],
        [0,1],
        [0,0],
        [0,0],
        [0,0],
        [0,0],
        [1,0],
        [1,0],
        [0,0],
        [0,0],
        [1,1],
        [0,0]]
    test(grid, comment)
