"""
130. Surrounded Regions
Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

from typing import List
import collections
import itertools

import sys
sys.path.insert(1, '../union_find/')
from union_find import UnionFind, SimpleUnionFind

###############################################################################
"""
Solution: recursion starting with border 'O' cells.

O(mn) time
O(m+n) extra space for recursion stack

Runtime: 140 ms, faster than 87.96% of Python3 online submissions
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def rec(r, c):
            if 0 < r < n_rows - 1 and 0 < c < n_cols - 1 and board[r][c] == 'O':
                board[r][c] = 'D' # don't flip
                rec(r+1, c)
                rec(r-1, c)
                rec(r, c+1)
                rec(r, c-1)

        if not board:
            return

        n_rows = len(board)
        n_cols = len(board[0])

        if n_rows < 3 or n_cols < 3:
            return

        for r in range(n_rows):
            if board[r][0] == 'O':
                rec(r, 1)
            if board[r][n_cols - 1] == 'O':
                rec(r, n_cols - 2)

        for c in range(1, n_cols - 1):
            if board[0][c] == 'O':
                rec(1, c)
            if board[n_rows - 1][c] == 'O':
                rec(n_rows - 2, c)

        # Check interior only since DFS only flipped interior squares.
        for r in range(1, n_rows - 1):
            for c in range(1, n_cols - 1):
                if board[r][c] == 'D': # don't flip
                    board[r][c] = 'O'
                else: # flip
                    board[r][c] = 'X'

###############################################################################
"""
Solution 2: BFS iterative, using deque.

Adds only interior cells to queue, not border cells.
Alternative name for 'D' (don't flip) could be 'E' (escaped).
In the end, only need to check interior cells.

O(mn) time
O(m+n) extra space

Runtime: 132 ms, faster than 99.38% of Python3 online submissions
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n_rows = len(board)
        n_cols = len(board[0])

        if n_rows < 3 or n_cols < 3:
            return

        # Initialize queue with interior cells adjacent to border 'O' cells.
        q = collections.deque([])

        for r, c in range(1, n_rows - 1):
            if board[r][0] == 'O':
                q.append((r, 1))
            if board[r][n_cols - 1] == 'O':
                q.append((r, n_cols - 2))

        for c in range(1, n_cols - 1):
            if board[0][c] == 'O':
                q.append((1, c))
            if board[n_rows - 1][c] == 'O':
                q.append((n_rows - 2, c))

        # BFS
        while q:
            r, c = q.popleft()

            if 0 < r < n_rows - 1 and 0 < c < n_cols - 1 and board[r][c] == 'O':
                board[r][c] = 'D' # don't flip
                q.append((r+1, c))
                q.append((r-1, c))
                q.append((r, c+1))
                q.append((r, c-1))

        # Check interior only since BFS only marked interior cells.
        for r in range(1, n_rows - 1):
            for c in range(1, n_cols - 1):
                if board[r][c] == 'D': # don't flip
                    board[r][c] = 'O'
                else: # flip
                    board[r][c] = 'X'
        
"""
Solution 2b: same as sol 2, but adds border cells to queue as well.  
Therefore, the "if" statement in the loop must include border cells.
In the end, have to check entire board.  In this variation, need to make
sure O's on border are marked, so they won't be flipped.
"""
class Solution2b:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n_rows = len(board)
        n_cols = len(board[0])

        if n_rows < 3 or n_cols < 3:
            return

        # Initialize queue with border squares that are 'O'.
        q = collections.deque([])

        border = list(itertools.product(range(n_rows), [0, n_cols - 1])) \
            + list(itertools.product([0, n_rows - 1], range(n_cols)))

        for r, c in border:
            if board[r][c] == 'O':
                q.append((r, c))

        # BFS
        while q:
            r, c = q.popleft()

            ### Alternative
            if 0 <= r < n_rows and 0 <= c < n_cols and board[r][c] == 'O':
                board[r][c] = 'D' # don't flip
                q.append((r+1, c))
                q.append((r-1, c))
                q.append((r, c+1))
                q.append((r, c-1))
            
            ### Alternative
            # if board[r][c] == 'O':
            #     board[r][c] = 'D' # don't flip
            #     if r+2 < n_rows: q.append((r+1, c))
            #     if r-1 > 0: q.append((r-1, c))
            #     if c+2 < n_cols: q.append((r, c+1))
            #     if c-1 > 0: q.append((r, c-1))

        ### Have to check entire board.
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == 'D': # don't flip
                    board[r][c] = 'O'
                else: # flip
                    board[r][c] = 'X'

###############################################################################
"""
Solution 3: use union find by rank w/ path compression.

https://leetcode.com/problems/surrounded-regions/discuss/41617/Solve-it-using-Union-Find

TLE if use simple union find.

Runtime: 324 ms, faster than 8.27% of Python3 online submissions
Memory Usage: 14.9 MB, less than 40.00% of Python3 online submissions
"""
class Solution3:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n_rows = len(board)
        n_cols = len(board[0])

        if n_rows < 3 or n_cols < 3:
            return

        dummy = n_rows * n_cols # index for dummy node
        #uf = SimpleUnionFind(dummy + 1)
        uf = UnionFind(dummy + 1)

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == 'O':
                    i = r * n_cols + c
                    
                    # Connect border 'O' cells to dummy node.
                    if r in (0, n_rows-1) or c in (0, n_cols-1):
                        uf.union(i, dummy)
                    else: # connect interior 'O' cells to neighbor 'O' cells
                        if board[r-1][c] == 'O':
                            uf.union(i, i - n_cols)
                        if board[r+1][c] == 'O':
                            uf.union(i, i + n_cols)
                        if board[r][c-1] == 'O':
                            uf.union(i, i - 1)
                        if board[r][c+1] == 'O':
                            uf.union(i, i + 1)

        for r in range(1, n_rows - 1):
            for c in range(1, n_cols - 1):
                if board[r][c] == 'O' and not uf.connected(r * n_cols + c, dummy):
                    board[r][c] = 'X'

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        for row in grid:
            #print(row)
            print(' '.join(row))
        print()

        sol.solve(grid)

        print()
        for row in grid:
        #     print(row)
            print(' '.join(row))
        print()


    sol = Solution() # recursion starting w/ border 'O' cells
    
    sol = Solution2() # BFS using queue
    sol = Solution2b()
    
    sol = Solution3() # union find

    comment = "LC example"
    grid = [
        ['X','X','X','X'],
        ['X','O','O','X'],
        ['X','X','O','X'],
        ['X','O','X','X']]
    test(grid, comment)

    comment = "LC test case"
    grid = [[]]
    test(grid, comment)

    comment = "LC test case"
    grid = [
        ['O','O'],
        ['O','O']]
    test(grid, comment)

    comment = "LC test case"
    grid = [
        ['O','O','O'],
        ['O','O','O'],
        ['O','O','O']]
    test(grid, comment)

    comment = "LC test case"
    grid = [
        ["X","O","X","X"],
        ["O","X","O","X"],
        ["X","O","X","O"],
        ["O","X","O","X"],
        ["X","O","X","O"],
        ["O","X","O","X"]]
    test(grid, comment)

    comment = "LC test case"
    grid = [
        ["X","O","O","X","X","X","O","X","X","O","O","O","O","O","O","O","O","O","O","O"],
        ["X","O","O","X","X","O","O","X","O","O","O","X","O","X","O","X","O","O","X","O"],
        ["O","O","O","X","X","X","X","O","X","O","X","X","O","O","O","O","X","O","X","O"],
        ["O","O","O","X","X","O","O","X","O","O","O","X","X","X","O","O","X","O","O","X"],
        ["O","O","O","O","O","O","O","X","X","X","O","O","O","O","O","O","O","O","O","O"],
        ["X","O","O","O","O","X","O","X","O","X","X","O","O","O","O","O","O","X","O","X"],
        ["O","O","O","X","O","O","O","X","O","X","O","X","O","X","O","X","O","X","O","X"],
        ["O","O","O","X","O","X","O","O","X","X","O","X","O","X","X","O","X","X","X","O"],
        ["O","O","O","O","X","O","O","X","X","O","O","O","O","X","O","O","O","X","O","X"],
        ["O","O","X","O","O","X","O","O","O","O","O","X","O","O","X","O","O","O","X","O"],
        ["X","O","O","X","O","O","O","O","O","O","O","X","O","O","X","O","X","O","X","O"],
        ["O","X","O","O","O","X","O","X","O","X","X","O","X","X","X","O","X","X","O","O"],
        ["X","X","O","X","O","O","O","O","X","O","O","O","O","O","O","X","O","O","O","X"],
        ["O","X","O","O","X","X","X","O","O","O","X","X","X","X","X","O","X","O","O","O"],
        ["O","O","X","X","X","O","O","O","X","X","O","O","O","X","O","X","O","O","O","O"],
        ["X","O","O","X","O","X","O","O","O","O","X","O","O","O","X","O","X","O","X","X"],
        ["X","O","X","O","O","O","O","O","O","X","O","O","O","X","O","X","O","O","O","O"],
        ["O","X","X","O","O","O","X","X","X","O","X","O","X","O","X","X","X","X","O","O"],
        ["O","X","O","O","O","O","X","X","O","O","X","O","X","O","O","X","O","O","X","X"],
        ["O","O","O","O","O","O","X","X","X","X","O","X","O","O","O","X","X","O","O","O"]]
    test(grid, comment)
