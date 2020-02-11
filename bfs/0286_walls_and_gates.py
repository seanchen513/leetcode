"""
286. Walls and Gates
Medium

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

"""

from typing import List
import collections

###############################################################################
"""
Solution: BFS.

O(mn) time
O(mn) extra space: 
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []

        INF = float('inf')
        #INF = 2**31 - 1

        n_rows = len(rooms)
        n_cols = len(rooms[0])
        gates = []

        for i in range(n_rows):
            for j in range(n_cols):
                if rooms[i][j] == 0:
                    gates += [(i, j, 0)] # 3rd index is distance to gate

        q = collections.deque(gates) 

        while q:
            i, j, d = q.popleft()
            rooms[i][j] = min(d, rooms[i][j])
            
            # Instead of checking, eg, rooms[i-1][j] == INF, can check > d.
            if i-1 >= 0 and rooms[i-1][j] == INF:
                q.append((i-1, j, d+1))
            if i+1 < n_rows and rooms[i+1][j] == INF:
                q.append((i+1, j, d+1))
            if j-1 >= 0 and rooms[i][j-1] == INF:
                q.append((i, j-1, d+1))
            if j+1 < n_cols and rooms[i][j+1] == INF:
                q.append((i, j+1, d+1))

###############################################################################
"""
Solution 2: same as sol #1, but just rewrite for directions list.  Slower.
"""
class Solution2:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []

        INF = float('inf')
        #INF = 2**31 - 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        n_rows = len(rooms)
        n_cols = len(rooms[0])
        gates = []

        for i in range(n_rows):
            for j in range(n_cols):
                if rooms[i][j] == 0:
                    gates += [(i, j, 0)] # 3rd index is distance to gate

        q = collections.deque(gates) 

        while q:
            i, j, d = q.popleft()
            rooms[i][j] = min(d, rooms[i][j])

            for dir in directions:
                r, c = i + dir[0], j + dir[1]

                # Instead of checking, eg, rooms[i-1][j] == INF, can check > d.
                if (not 0 <= r < n_rows) or (not 0 <= c < n_cols) or (rooms[r][c] != INF):
                    continue
                
                q.append((r, c, d+1))

###############################################################################
"""
Solution 3: DFS.

To deal with multiple gates, instead of checking, eg, rooms[i][j+1] == INF,
to see if it's ok to add to the stack, check rooms[i][j+1] > d.  If this
condition holds, it means the room was visited before, possibly from another
gate, but that it is a shorter distance from the "current" gate.
"""
class Solution3:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return []

        #INF = float('inf')
        #INF = 2**31 - 1

        n_rows = len(rooms)
        n_cols = len(rooms[0])
        stack = [] 

        for i in range(n_rows):
            for j in range(n_cols):
                if rooms[i][j] == 0:
                    stack += [(i, j, 0)] # 3rd index is distance to gate

        while stack:
            i, j, d = stack.pop()
            rooms[i][j] = min(d, rooms[i][j])

            if i-1 >= 0 and rooms[i-1][j] > d:
                stack.append((i-1, j, d+1))
            if i+1 < n_rows and rooms[i+1][j] > d:
                stack.append((i+1, j, d+1))
            if j-1 >= 0 and rooms[i][j-1] > d:
                stack.append((i, j-1, d+1))
            if j+1 < n_cols and rooms[i][j+1] > d:
                stack.append((i, j+1, d+1))

###############################################################################

if __name__ == "__main__":
    def test(rooms, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print("\nRooms before:\n")
        for row in rooms:
            for cell in row:
                print(f"{cell:5}", end="")
            print()

        s.wallsAndGates(rooms)

        print("\nRooms after:\n")
        for row in rooms:
            for cell in row:
                print(f"{cell:5}", end="")
            print()


    s = Solution() # BFS
    #s = Solution2() # BFS with directions array
    #s = Solution3() # DFS

    INF = float('inf')
    #INF = 2**31 - 1

    comment = "LC ex1"
    rooms = [
        [INF, -1,  0,INF],
        [INF,INF,INF, -1],
        [INF, -1,INF, -1],
        [  0, -1,INF,INF]]
    test(rooms, comment)
    
    comment = "LC test case"
    rooms = []
    test(rooms, comment)
    