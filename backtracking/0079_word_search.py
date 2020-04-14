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

O(mn * 4^w) time, where board is m-by-n, and word has length w
O(w = O(mn) extra space: for recursion stack

Runtime: 300 ms, faster than 89.50% of Python3 online submissions
Memory Usage: 15.5 MB, less than 14.89% of Python3 online submissions
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def rec(i, r, c):
            #if i >= w:
            #    return True
            
            if not (0 <= r < m and 0 <= c < n):
                return False
            
            if word[i] != board[r][c]:
                return False
            
            board[r][c] = '#' # mark cell as visited using sentinel char

            if i == w - 1:
                return True
            
            i += 1
            if (rec(i, r-1, c) or rec(i, r+1, c) or 
                rec(i, r, c-1) or rec(i, r, c+1)
               ):
                return True

            # backtrack            
            i -= 1
            board[r][c] = word[i]

            return False
                    
        m = len(board)
        n = len(board[0])
        s0 = word[0]
        w = len(word)
        
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch == s0 and rec(0, i, j):    
                    return True

        return False
    