"""
36. Valid Sudoku
Medium

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being 
	modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

from typing import List

###############################################################################
"""
Solution: use helper function that uses set to check for duplicates by 
checking length of set.
"""
class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		def dups(arr):
			digits = [d for d in arr if d != '.']
			return len(digits) != len(set(digits))

		if any(dups(row) for row in board) or any(dups(row) for row in zip(*board)):
			return False

		#blocks = [[[]]*3 for _ in range(3)] # doesn't work correctly
		blocks = [[[],[],[]] for _ in range(3)]

		# for i in range(9):
		# 	for j in range(9):
		# 		blocks[i // 3][j // 3].append( board[i][j] )

		for i in range(0, 9, 3):
			i2 = i // 3
			for j in range(0, 9, 3):
				j2 = j // 3
				for di in range(3):
					blocks[i2][j2].extend( board[i + di][j:j+3] )
					#blocks[i//3][j//3].extend( board[i + di][j:j+3] )
				
		return not any(dups(b) for r in blocks for b in r)

###############################################################################
"""
Solution 2: use helper function that uses set to check for duplicates.
"""
class Solution2:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		def dups(arr):
			seen = set()
			for x in arr:
				if x in seen:
					return True
					
				if x != '.':
					seen.add(x)

			return False

		if any(dups(row) for row in board) or any(dups(row) for row in zip(*board)):
			return False

		blocks = [[[],[],[]] for _ in range(3)]

		# for i in range(9):
		# 	for j in range(9):
		# 		blocks[i // 3][j // 3].append( board[i][j] )

		for i in range(0, 9, 3):
			i2 = i // 3
			for j in range(0, 9, 3):
				j2 = j // 3
				for di in range(3):
					blocks[i2][j2].extend( board[i + di][j:j+3] )
					#blocks[i//3][j//3].extend( board[i + di][j:j+3] )

		return not any(dups(b) for r in blocks for b in r)
		
###############################################################################
"""
Solution 3: early exit while checking blocks.
"""
class Solution3:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		def dups(arr):
			digits = [d for d in arr if d != '.']
			return len(digits) != len(set(digits))

		if any(dups(row) for row in board) or any(dups(row) for row in zip(*board)):
			return False

		for i in range(0, 9, 3):
			for j in range(0, 9, 3):
				block = []
				for di in range(3):
					block.extend( board[i + di][j:j+3] )
				
				if dups(block):
					return False
		
		return True

###############################################################################
"""
Solution 4: single traversal through board, early exit, but uses 3 sets.
"""
class Solution4:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		# Using [set()]*9 doesn't work correctly.		
		rows = [set() for _ in range(9)]
		cols = [set() for _ in range(9)]
		blocks = [set() for _ in range(9)]
		
		for i in range(9):
			for j in range(9):
				x = board[i][j]
				if x == '.':
					continue

				if x in rows[i]:
					return False
				rows[i].add(x)

				if x in cols[j]:
					return False
				cols[j].add(x)

				block_index = (i // 3) * 3 + j // 3
				if x in blocks[block_index]:
					return False
				blocks[block_index].add(x)

		return True

###############################################################################
"""
Solution 5: three traversals through board, early exit.  Uses one set at a time.
"""
class Solution5:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		# Using [set()]*9 doesn't work correctly.		
		seen = [set() for _ in range(9)]
		
		# Check rows.
		for r in range(9):
			for c in range(9):
				x = board[r][c]
				if x == '.':
					continue

				if x in seen[r]:
					return False
				
				seen[r].add(x)

		# Check columns.
		seen = [set() for _ in range(9)]
		for c in range(9):
			for r in range(9):
				x = board[r][c]
				if x == '.':
					continue

				if x in seen[c]:
					return False
				
				seen[c].add(x)

		# Check blocks.
		seen = [set() for _ in range(9)]
		for i in range(9):
			for j in range(9):
				x = board[i][j]
				if x == '.':
					continue

				block_index = (i // 3) * 3 + j // 3
				if x in seen[block_index]:
					return False
				
				seen[block_index].add(x)

		return True

###############################################################################

if __name__ == "__main__":
	def test(grid, comment=None):
		print("="*80)
		if comment:
			print(comment, "\n")

		for row in grid:
			for c in row:
				print(c, end=' ')
			print()

		res = sol.isValidSudoku(grid)
		print(f"\nSolution: {res}\n")


	sol = Solution()
	sol = Solution2()
	sol = Solution3() # eearly exit while checking blocks
	sol = Solution4() # single traversal of board, but uses 3 sets at a time.
	sol = Solution5() # 3 traversals of board, uses one set at a time.

	comment = "LC ex1; answer = True"
	grid = [
		["5","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]]
	test(grid, comment)

	comment = "LC ex2; answer = False"
	grid = [
		["8","3",".",".","7",".",".",".","."],
		["6",".",".","1","9","5",".",".","."],
		[".","9","8",".",".",".",".","6","."],
		["8",".",".",".","6",".",".",".","3"],
		["4",".",".","8",".","3",".",".","1"],
		["7",".",".",".","2",".",".",".","6"],
		[".","6",".",".",".",".","2","8","."],
		[".",".",".","4","1","9",".",".","5"],
		[".",".",".",".","8",".",".","7","9"]]
	test(grid, comment)
