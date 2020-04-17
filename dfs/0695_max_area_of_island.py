"""
695. Max Area of Island
Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]

Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
"""

from typing import List

###############################################################################
"""
Solution: recursion to visit all unvisited land cells. Use input grid as
visited matrix.

O(mn) time
O(mn) extra space: for recursion stack

Runtime: 132 ms, faster than 91.05% of Python3 online submissions
Memory Usage: 16.2 MB, less than 27.27% of Python3 online submissions 
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def visit(r, c, count=0):
            if not (0 <= r < m and 0 <= c < n):
                return count
            
            if grid[r][c] != 1:
                return count
            
            grid[r][c] = 2

            count = visit(r-1, c, count)
            count = visit(r+1, c, count)
            count = visit(r, c-1, count)
            count = visit(r, c+1, count)
            
            return count + 1
            
        m = len(grid)
        n = len(grid[0])
        mx = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = visit(i, j)
                    if area > mx:
                        mx = area
                        
        return mx

###############################################################################
"""
Solution 2: DFS using stack.

Runtime: 112 ms, faster than 99.86% of Python3 online submissions
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        mx = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    stack = [(i, j)]
                    grid[i][j] = 2 # mark as visited

                    while stack:
                        r, c = stack.pop()
                        ### cannot just mark here alone, otherwise a land cell
                        ### can be put on the stack and then visited more than
                        ### once via other cells.
                        #grid[r][c] = 2 # mark as visited
                        area += 1

                        if r > 0 and grid[r-1][c] == 1:
                            stack.append((r-1, c))
                            grid[r-1][c] = 2 # mark as visited
                        if r+1 < m and grid[r+1][c] == 1:
                            stack.append((r+1, c))
                            grid[r+1][c] = 2 # mark as visited
                        if c > 0 and grid[r][c-1] == 1:
                            stack.append((r, c-1))
                            grid[r][c-1] = 2 # mark as visited
                        if c+1 < n and grid[r][c+1] == 1:
                            stack.append((r, c+1))
                            grid[r][c+1] = 2 # mark as visited

                    if area > mx:
                        mx = area

        return mx                        

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        if not arr:
            grid = []
        else:
            n_cols = len(arr[0])
            grid = [[s[j] for j in range(n_cols)] for s in arr]
        
        res = s.maxAreaOfIsland(grid)

        print()
        for i in range(len(arr)):
            print(arr[i])

        print(f"\nresult = {res}\n")


    s = Solution() # recursion, using input grid as visited matrix
    s = Solution2() # DFS using stack
    # s = Solution3() # BFS using deque
    # s = Solution4() # union find

    comment = "LC ex1; answer = 6"
    arr = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    test(arr, comment)

    comment = "LC ex2; answer = 0"
    arr = [[0,0,0,0,0,0,0,0]]
    test(arr, comment)

    comment = "LC TC; answer = 4"
    arr = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]
    test(arr, comment)

    comment = "single cell, land; answer = 1"
    arr = [[1]]
    test(arr, comment)
