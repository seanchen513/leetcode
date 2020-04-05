"""
994. Rotting Oranges
Easy

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 
Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

from typing import List
import collections

###############################################################################
"""
Solution: BFS using lists, and counter for fresh oranges.

O(n) time, where n = size of grid
O(n) extra space: for queues

"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = []
        fresh_count = 0
        
        # Fill q with rotten oranges, and count fresh oranges
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2: # rotten
                    q.append((r, c))
                elif grid[r][c] == 1: # fresh
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
        
        time = 0
        dir = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh_count > 0:
            time += 1
            q2 = []

            for r, c in q:
                for dr, dc in dir:
                    r2 = r + dr
                    c2 = c + dc
                    if 0 <= r2 < m and 0 <= c2 < n and grid[r2][c2] == 1: # fresh
                        grid[r2][c2] = 2 # turn rotten
                        fresh_count -= 1
                        q2.append((r2, c2))

            q = q2

        if fresh_count == 0:
            return time

        return -1

"""
Solution 1b: same, but with early return
"""
class Solution1b:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = []
        fresh_count = 0
        
        # Fill q with rotten oranges, and count fresh oranges
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2: # rotten
                    q.append((r, c))
                elif grid[r][c] == 1: # fresh
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
        
        time = 0
        dir = [(1,0), (-1,0), (0,1), (0,-1)]

        while 1:
            time += 1
            q2 = []

            for r, c in q:
                for dr, dc in dir:
                    r2 = r + dr
                    c2 = c + dc
                    if 0 <= r2 < m and 0 <= c2 < n and grid[r2][c2] == 1: # fresh
                        grid[r2][c2] = 2 # turn rotten
                        fresh_count -= 1
                        q2.append((r2, c2))

                        if fresh_count == 0:
                            return time
            
            if not q2:
                return -1

            q = q2

###############################################################################
"""
Solution: BFS using deque, and no counter for fresh oranges.

O(n) time, where n = size of grid
O(n) extra space: for queues

"""
class Solution2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = collections.deque([])
        
        # Fill q with rotten oranges
        for r, row in enumerate(grid):
            for c, state in enumerate(row):
                if state == 2: # rotten
                    q.append((r, c, 0))

        time = 0
        dir = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c, time = q.popleft()
            
            for dr, dc in dir:
                r2 = r + dr
                c2 = c + dc
                if 0 <= r2 < m and 0 <= c2 < n and grid[r2][c2] == 1: # fresh
                    grid[r2][c2] = 2 # turn rotten
                    q.append((r2, c2, time + 1))

        if any(1 in row for row in grid):
            return -1

        return time

"""
Solution 2b: same, but use neighbors() generator function.
"""
class Solution2b:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = collections.deque([])
        
        # Fill q with rotten oranges
        for r, row in enumerate(grid):
            for c, state in enumerate(row):
                if state == 2: # rotten
                    q.append((r, c, 0))
        
        def neighbors(r, c):
            for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):
                if 0 <= nr < m and 0 <= nc < n:
                    yield nr, nc

        time = 0

        while q:
            r, c, time = q.popleft()
            
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1: # fresh
                    grid[nr][nc] = 2 # turn rotten
                    q.append((nr, nc, time + 1))

        if any(1 in row for row in grid):
            return -1

        return time

###############################################################################
"""
Solution 3: Pythonic

https://leetcode.com/problems/rotting-oranges/discuss/388104/Python-10-lines-BFS-beat-97

"""
class Solution3:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rotting = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        time = 0
        
        while fresh:
            if not rotting: 
                return -1
            
            rotting = {(i+di, j+dj) for i, j in rotting 
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)] 
                if (i+di, j+dj) in fresh}
            
            fresh -= rotting
            
            time += 1
        
        return time     

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.orangesRotting(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # BFS using lists, and counter for fresh oranges
    sol = Solution1b() # same, but with early return
    
    sol = Solution2() # BFS using deque
    sol = Solution2b() # same, but use neighbors() generator fn
    
    sol = Solution3() # Pythonic
    
    comment = "LC ex1; answer = 4"
    arr = [[2,1,1],[1,1,0],[0,1,1]]
    test(arr, comment)

    comment = "LC ex2; answer = -1"
    arr = [[2,1,1],[0,1,1],[1,0,1]]
    test(arr, comment)

    comment = "LC ex3; answer = 0"
    arr = [[0,2]]
    test(arr, comment)
    
    comment = "LC TC; answer = 0"
    arr = [[0]]
    test(arr, comment)
