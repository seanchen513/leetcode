"""
79. Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:

board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""

from typing import List

"""
NOT USED:

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        dx = [-1, 1,  0, 0]
        dy = [ 0, 0, -1, 1]

"""
###############################################################################
"""
Solution: backtracking w/ recursion and visited set.

O(mn * 4^w) time, where board is m-by-n, and word has length w
O(w = O(mn) extra space: for visited set and recursion stack

Runtime: 308 ms, faster than 87.56% of Python3 online submissions
Memory Usage: 15.3 MB, less than 17.02% of Python3 online submissions
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def rec(s, r, c): # recursive backtracking function
            # if not s:
            #     return True

            if not (0 <= r < m and 0 <= c < n):
                return False
            
            if (r,c) in visited or s[0] != board[r][c]:
                return False
            
            visited.add((r,c))
            
            if len(s) == 1:
                return True
            
            s1 = s[1:]
            if (rec(s1, r-1, c) or rec(s1, r+1, c) or 
                rec(s1, r, c-1) or rec(s1, r, c+1)
               ):
                return True
            
            # backtrack
            visited.remove((r,c))

            return False
                    
        m = len(board)
        n = len(board[0])
        
        visited = set()
        s0 = word[0]
        
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == s0 and rec(word, i, j):    
                    return True

        return False

###############################################################################
"""
Solution: instead of visited set, mark visited cells on board with sentinel char.
Also, pass index in word instead of passing substrings (suffixes).
Also, check bounds before calling backtrack fn recursively.

O(mn * 4^w) time, where board is m-by-n, and word has length w
O(w = O(mn) extra space: for recursion stack

Runtime: 260 ms, faster than 96.82% of Python3 online submissions
Memory Usage: 14.8 MB, less than 27.66% of Python3 online submissions

Also, check character before calling backtrack fn:
Runtime: 212 ms, faster than 98.95% of Python3 online submissions
Memory Usage: 15.1 MB, less than 17.02% of Python3 online submissions
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def rec(i, r, c):
            # if word[i] != board[r][c]:
            #     return False
            
            board[r][c] = '#' # mark cell as visited using sentinel char
            i += 1

            if i == w:
                return True
            
            # if ((r > 0 and rec(i, r-1, c)) or 
            #     (r+1 < m and rec(i, r+1, c)) or 
            #     (c > 0 and rec(i, r, c-1)) or 
            #     (c+1 < n and rec(i, r, c+1))
            # ): 
            #     return True

            ch = word[i]
            if ((r > 0 and ch == board[r-1][c] and rec(i, r-1, c)) or 
                (r+1 < m and ch == board[r+1][c] and rec(i, r+1, c)) or 
                (c > 0 and ch == board[r][c-1] and rec(i, r, c-1)) or 
                (c+1 < n and ch == board[r][c+1] and rec(i, r, c+1))
            ): 
                return True

            # backtrack            
            i -= 1
            board[r][c] = word[i]

            return False
                    
        m = len(board)
        n = len(board[0])
        
        w = len(word)
        s0 = word[0]
        
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == s0 and rec(0, i, j):    
                    return True

        return False
    
###############################################################################
"""
Solution: backtracking using DFS iteration, which uses stack.
Use "seen" set to track visited board cells.

Runtime: 272 ms, faster than 95.87% of Python3 online submissions
Memory Usage: 30.3 MB, less than 6.38% of Python3 online submissions
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        w = len(word)
        s0 = word[0]

        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == s0:
                    
                    stack = [(i, j, 1, {(i,j)})] # 1 = next index in word to check
                    
                    while stack:
                        r, c, k, seen = stack.pop()
                        #print(f"{r}, {c}, {k}")

                        if k == w:
                            return True

                        ch = word[k]
                        k += 1

                        r1 = r - 1
                        if r > 0 and (r1, c) not in seen and ch == board[r1][c]:
                            stack.append((r1, c, k, seen.union({(r1, c)})))
                            
                        r1 = r + 1
                        if r1 < m and (r1, c) not in seen and ch == board[r1][c]:
                            stack.append((r1, c, k, seen.union({(r1, c)})))
                            
                        c1 = c - 1
                        if c > 0 and (r, c1) not in seen and ch == board[r][c1]:
                            stack.append((r, c1, k, seen.union({(r, c1)})))
                            
                        c1 = c + 1
                        if c1 < n and (r, c1) not in seen and ch == board[r][c1]:
                            stack.append((r, c1, k, seen.union({(r, c1)})))
                            
        return False
    