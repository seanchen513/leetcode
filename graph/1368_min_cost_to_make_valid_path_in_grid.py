"""
1368. Minimum Cost to Make at Least One Valid Path in a Grid
Hard

Given a m x n grid. Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell. The sign of grid[i][j] can be:
1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])

Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0). A valid path in the grid is a path which starts from the upper left cell (0,0) and ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:

Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output: 3
Explanation: You will start at point (0, 0).
The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
The total cost = 3.

Example 2:

Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
Output: 0
Explanation: You can follow the path from (0, 0) to (2, 2).

Example 3:

Input: grid = [[1,2],[4,3]]
Output: 1

Example 4:

Input: grid = [[2,2,2],[2,2,2]]
Output: 3

Example 5:

Input: grid = [[4]]
Output: 0
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
"""

from typing import List
import collections

###############################################################################
"""
Solution: BFS + DFS.

BFS at constant cost: at any time, all the elements in the queue have the 
same cost.  DFS to find all unvisited cells that can be reached from each 
cell in queue at no extra cost.

https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/discuss/524886/JavaC%2B%2BPython-BFS-and-DFS

O(mn) time, where grid is m-by-n.
O(mn) extra space

Runtime: 344 ms, faster than 91.62% of Python3 online submissions
Memory Usage: 24.4 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        inf = float('inf')
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # DP table of min cost to reach (r,c) from (0,0).
        # Also serves as visited check.
        dp = [[inf]*n_cols for _ in range(n_rows)]

        cost = 0 # current cost
        q = [] # queue of cells (r,c) in grid; for BFS

        # Visit all cells reachable from (r,c) by following path given by arrows.
        def dfs(r, c):
            # Don't do anything if out of bounds or visited before.
            if not (0 <= r < n_rows and 0 <= c < n_cols and dp[r][c] == inf):
                return

            dp[r][c] = cost
            q.append((r, c))
            
            # Visit neighbor cell in direction of arrow.
            # Subtract one because direction values are 1-based.
            dr, dc = directions[ grid[r][c] - 1 ]
            dfs(r + dr, c + dc)

        # Find all cells that can be reached from (0,0) at 0 cost and add them to q.
        dfs(0, 0)
        
        # BFS
        while q:
            q_prev = q
            q = []

            cost += 1           

            # For each cell in queue q_prev, visit neighboring cells that have
            # not yet been visited.
            for r, c in q_prev:
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        return dp[-1][-1]

"""
Solution 1b: BFS using costs dict as visited check.

Based on:
https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/discuss/524828/Python-O(MN)-simple-BFS-with-explanation

Runtime: 360 ms, faster than 85.53% of Python3 online submissions
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions
"""
class Solution1b:
    def minCost(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        costs = {}

        # queue of cells (r,c) in grid; for BFS
        q = collections.deque( [(0,0,0)] ) 

        while q:
            r, c, cost = q.popleft()
            
            while 0 <= r < n_rows and 0 <= c < n_cols and (r, c) not in costs:
                costs[r, c] = cost

                # for dr, dc in directions:
                #     r2, c2 = r+dr, c+dc
                #     q.append((r2, c2, cost + 1))

                q.extend( [(r+dr, c+dc, cost + 1) for dr, dc in directions] )

                dr, dc = directions[grid[r][c] - 1] # 0-cost direction
                r += dr
                c += dc

        return costs[n_rows-1, n_cols-1]

###############################################################################
"""
Solution 2: 0-1 BFS using deque.

Put 0-cost edges in front of queue, and 1-cost edges in back of queue, so that 
vertices are processed in increasing order of weights.

Based on:
https://www.geeksforgeeks.org/0-1-bfs-shortest-path-binary-graph/

O(mn) time, where grid is m-by-n
O(mn) extra space

Runtime: 308 ms, faster than 97.39% of Python3 online submissions
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def minCost(self, grid: List[List[int]]) -> int:
        n_rows, n_cols = len(grid), len(grid[0])
        inf = float('inf')
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # costs table of min cost to reach (r,c) from (0,0)
        costs = [[inf]*n_cols for _ in range(n_rows)]

        q = collections.deque( [(0,0)] ) # deque for BFS; start with cell (0,0)
        costs[0][0] = 0

        while q:
            r, c = q.popleft()
            cost = costs[r][c]
            dir = directions[grid[r][c] - 1] # 0-cost direction

            for dr, dc in directions:
                r2, c2 = r+dr, c+dc
                if not (0 <= r2 < n_rows and 0 <= c2 < n_cols):
                    continue

                if (dr, dc) == dir:
                    if cost < costs[r2][c2]:
                        costs[r2][c2] = cost
                        q.appendleft((r2, c2)) # put 0-cost edges in front of queue

                else: # 1-cost edge
                    if cost + 1 < costs[r2][c2]:
                        costs[r2][c2] = cost + 1
                        q.append((r2, c2)) # put 1-cost edges in back of queue

        return costs[-1][-1]

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        for row in grid:
            print(row)
        print()

        res = sol.minCost(grid)

        print(f"\nres = {res}")


    sol = Solution() # BFS + DFS
    sol = Solution1b()

    sol = Solution2() # 0-1 BFS

    comment = "LC ex1; answer = 3"
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
    test(grid, comment)

    comment = "LC ex2; answer = 0"
    grid = [[1,1,3],[3,2,2],[1,1,4]]
    test(grid, comment)

    comment = "LC ex3; answer = 1"
    grid = [[1,2],[4,3]]
    test(grid, comment)

    comment = "LC ex4; answer = 3"
    grid = [[2,2,2],[2,2,2]]
    test(grid, comment)
    
    comment = "LC ex4; answer = 0"
    grid = [[4]]
    test(grid, comment)

    # comment = "LC test case; answer = 18"
    # grid = [[3,4,3],[2,2,2],[2,1,1],[4,3,2],[2,1,4],[2,4,1],[3,3,3],[1,4,2],[2,2,1],[2,1,1],[3,3,1],[4,1,4],[2,1,4],[3,2,2],[3,3,1],[4,4,1],[1,2,2],[1,1,1],[1,3,4],[1,2,1],[2,2,4],[2,1,3],[1,2,1],[4,3,2],[3,3,4],[2,2,1],[3,4,3],[4,2,3],[4,4,4]]
    # test(grid, comment)
