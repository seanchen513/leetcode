"""
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

import sys
sys.path.insert(1, '../union_find/')

from union_find import UnionFind, SimpleUnionFind

from typing import List
import collections

###############################################################################
"""
Solution: Recursion using visited matrix.

O(mn) time: every cell is looped through.

O(mn) extra space: visited matrix is size mn, and recursion goes mn levels 
deep if all cells are land.

Runtime: 148 ms, faster than 61.28% of Python3 online submissions
Memory Usage: 13.9 MB, less than 59.83% of Python3 online submissions
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(i, j):
            if not (0 <= i < n_rows) or not (0 <= j < n_cols) \
                or visited[i][j] or grid[i][j] == "0":
                return 0

            visited[i][j] = 1

            visit(i+1, j)
            visit(i-1, j)
            visit(i, j+1)
            visit(i, j-1)

            return 1

        if not grid:
            return 0

        n_rows = len(grid)
        n_cols = len(grid[0])
        visited = [[0]*n_cols for _ in range(n_rows)]
        
        n_islands = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1" and not visited[i][j]:
                    n_islands += visit(i, j)

        return n_islands

###############################################################################
"""
Solution: Recursion, modifies input grid, using it as a visited matrix.

0: water
1: unvisited land
2: visited land (or could just use state 0 for this)

O(mn) time: every cell is looped through.
O(mn) extra space: recursion goes mn levels deep if all cells are land.

Runtime: 140 ms, faster than 82.24% of Python3 online submissions
Memory Usage: 14 MB, less than 40.17% of Python3 online submissions
"""
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(i, j):
            if not (0 <= i < n_rows) or not (0 <= j < n_cols) or grid[i][j] != "1":
                return 0

            grid[i][j] = 2 # mark as visited; can also use 0

            visit(i+1, j)
            visit(i-1, j)
            visit(i, j+1)
            visit(i, j-1)

            return 1

        if not grid:
            return 0

        n_rows = len(grid)
        n_cols = len(grid[0])
        
        n_islands = 0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == "1":
                    n_islands += visit(i, j)

        return n_islands

"""
Solution 2b: Recursion, modifies input grid, using it as a visited matrix.  
Made visit() not return a value (default None), and increment n_islands 
counter in loop instead.  Check bounds before calling recursively.

O(mn) time: every cell is looped through.
O(mn) extra space: recursion goes mn levels deep if all cells are land.

Runtime: 124 ms, faster than 98.33% of Python3 online submissions
Memory Usage: 15 MB, less than 9.40% of Python3 online submissions
"""
class Solution2b:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(r, c):
            if grid[r][c] != "1":
                return

            grid[r][c] = 2 # mark as visited; can also use 0

            if r + 1 < m: 
                visit(r + 1, c)
            if r > 0: 
                visit(r - 1, c)
            if c + 1 < n: 
                visit(r, c + 1)
            if c > 0: 
                visit(r, c - 1)

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        n_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    n_islands += 1
                    visit(i, j)

        return n_islands

###############################################################################
"""
Solution: BFS using deque.

O(mn) time: every cell is looped through.

O(min(m,n)) extra space: BFS grows like diamond, limited by smaller of row
or column size.

Runtime: 116 ms, faster than 99.84% of Python3 online submissions
Memory Usage: 13.6 MB, less than 96.58% of Python3 online submissions
"""
class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        n_islands = 0
        q = collections.deque([])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    n_islands += 1
                    grid[i][j] = "2" # mark as visited

                    #q = collections.deque([(i, j)])
                    q.append((i, j))

                    while q:
                        #print(len(q))
                        r, c = q.popleft()

                        if (r+1 < m) and grid[r+1][c] == "1":
                            q.append((r+1, c))
                            grid[r+1][c] = "2" # mark as visited
                        
                        if (r > 0) and grid[r-1][c] == "1":
                            q.append((r-1, c))
                            grid[r-1][c] = "2" # mark as visited
                        
                        if (c+1 < n) and grid[r][c+1] == "1":
                            q.append((r, c+1))
                            grid[r][c+1] = "2" # mark as visited
                        
                        if (c > 0) and grid[r][c-1] == "1":
                            q.append((r, c-1))
                            grid[r][c-1] = "2" # mark as visited

        return n_islands

###############################################################################
"""
Solution: Union find.

Each island is a connected component. The count of islands is the count of
components in the union find.

The subset count in "uf" is initialized to the total number of grid cells.
We adjust the count within the loop.

(If we instead init'd the union find to be the number of land cells,
then we would need to also adjust the indices we used for the
arguments to our union calls.)

Grid coordinates (r, c) is mapped to UF index r * n_cols + c.

Use input grid as visited matrix by changing land "1" to "2".

Visit every cell. If water cell, decrement UF count.
If unvisited land cell, mark as visited, and union w/ its neighbors to the
right and below if they are land cells.
"""
class Solution4:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n_rows = len(grid)
        n_cols = len(grid[0])
        
        #n_land = sum([row.count("1") for row in grid])
        #print(f"n_land = {n_land}")

        #uf = SimpleUnionFind(n_rows * n_cols)
        uf = UnionFind(n_rows * n_cols)

        # Suffices to check in the two directions (right, down) of our loops.
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "0":
                    uf.n -= 1

                elif grid[r][c] == "1":
                    grid[r][c] = "2" # mark as visited

                    # Union (r, c) w/ (r+1, c) if land cell
                    if (r+1 < n_rows) and grid[r+1][c] == "1":
                        uf.union(r*n_cols + c, (r+1)*n_cols + c)

                    #if (r-1 >= 0) and grid[r-1][c] == "1":
                    #    uf.union(r*n_cols + c, (r-1)*n_cols + c)

                    # Union (r, c) w/ (r, c+1) if land cell
                    if (c+1 < n_cols) and grid[r][c+1] == "1":
                        uf.union(r*n_cols + c, r*n_cols + c+1)

                    #if (c-1 >= 0) and grid[r][c-1] == "1":
                    #    uf.union(r*n_cols + c, r*n_cols + c-1)

        return uf.n

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
        
        res = s.numIslands(grid)

        print()
        for i in range(len(arr)):
            print(arr[i])

        print(f"\nresult = {res}")


    s = Solution() # recursion, use visited matrix
    s = Solution2() # recursion, use input grid as visited matrix
    s = Solution2b() # some optimizations
    s = Solution3() # BFS using deque
    s = Solution4() # union find

    comment = "single cell, land; answer = 1"
    arr = ["1"]
    test(arr, comment)

    comment = "single cell, water; answer = 0"
    arr = ["0"]
    test(arr, comment)

    comment = "single row; answer = 5"
    arr = [
        "1011010111001"]
    test(arr, comment)

    comment = "single column; answer = 3"
    arr = [
        "1","0","1", "1", "0", "0", "1"]
    test(arr, comment)

    comment = "all land; answer = 1"
    arr = [
        "11111",
        "11111"]
    test(arr, comment)

    comment = "all water; answer = 0"
    arr = [
        "00",
        "00",
        "00"]
    test(arr, comment)

    comment = "LC ex1; answer = 1"
    arr = [
        "11110",
        "11010",
        "11000",
        "00000"]
    test(arr, comment)

    comment = "LC ex2; answer = 3"
    arr = [
        "11000",
        "11000",
        "00100",
        "00011"]
    test(arr, comment)

    comment = "LC test case: empty grid; answer = 0"
    arr = []
    test(arr, comment)

    comment = "cycles of land; answer = 1"
    arr = [
        "11111",
        "10101",
        "10101",
        "11111"]
    test(arr, comment)
    