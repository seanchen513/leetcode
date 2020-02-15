"""
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

A sudoku puzzle...

...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

from typing import List
import heapq
import copy

###############################################################################
"""
Solution: assume given board has unique solution.

Use constraint propagation and backtracking.  Try cells with fewer possibilities
first.

Ideas: (1) bitmasks, (2) priority queue, keep updating open,
(3) instead of row, col, box, try grid of possibilities?

Runtime: 36 ms, faster than 97.33% of Python3 online submissions
Memory Usage: 12.9 MB, less than 96.43% of Python3 online submissions
"""
class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		"""
		Do not return anything, modify board in-place instead.
		"""
		def dfs():
			if not open:
				return True

			i, j, k = open[-1]			
			#k = (i//3)*3 + j//3 # box index

			cand = row[i] & col[j] & box[k]
			if not cand:
				return False

			for c in cand:
				board[i][j] = c
				open.pop()

				row[i].discard(c)
				col[j].discard(c)
				box[k].discard(c)

				if dfs():
					return True

				row[i].add(c)
				col[j].add(c)
				box[k].add(c)

				open.append((i,j, k))
				#board[i][j] = c # unnecessary since one of the c's must work

			return False

		# possible digits to use for filling cells in each row, col, or box
		row = [set(str(d) for d in range(1, 10)) for _ in range(9)]
		col = [set(str(d) for d in range(1, 10)) for _ in range(9)]
		box = [set(str(d) for d in range(1, 10)) for _ in range(9)]

		open = [] # list of coordinates where cell is '.'

		for i in range(9):
			#i2 = (i//3)*3
			i2 = i - i % 3
			for j in range(9):
				x = board[i][j]
				if x == '.':
					open.append((i, j, i2 + j//3))
				else:
					row[i].discard(x)
					col[j].discard(x)
					box[i2 + j//3].discard(x)

		# Sort open cells so that those with fewest possibilities will be
		# tried first.
		open_ordered = []
		for i, j, k in open:
			poss = row[i] & col[j] & box[k]
			open_ordered.append((len(poss), i, j, k))
  				  
		open_ordered.sort(reverse=True)
		open = [(i, j, k) for _, i, j, k in open_ordered]
		
		dfs()

###############################################################################
"""
Solution 2: same as sol #1, but passes copies of "open" instead of popping
"open" before dfs() and appending to "open" after.

Runtime: 56 ms, faster than 90.53% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions

Trying cells with fewest possibilities first:
Runtime: 36 ms, faster than 97.33% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
	def solveSudoku(self, board: List[List[str]]) -> None:
		def dfs(open):
			if not open:
				return True

			i, j, k = open.pop()
			#k = (i//3)*3 + j//3 # box index

			cand = row[i] & col[j] & box[k]
			if not cand:
				return False

			for c in cand:
				board[i][j] = c

				row[i].discard(c)
				col[j].discard(c)
				box[k].discard(c)

				if dfs(open[:]):
					return True

				row[i].add(c)
				col[j].add(c)
				box[k].add(c)
				#board[i][j] = c # unnecessary since one of the c's must work

			return False

		# possible digits to use for filling cells in each row, col, or box
		row = [set(str(d) for d in range(1, 10)) for _ in range(9)]
		col = [set(str(d) for d in range(1, 10)) for _ in range(9)]
		box = [set(str(d) for d in range(1, 10)) for _ in range(9)]

		open = [] # list of coordinates where cell is '.'

		for i in range(9):
			#i2 = (i//3)*3
			i2 = i - i % 3
			for j in range(9):
				x = board[i][j]
				if x == '.':
					open.append((i, j, i2 + j//3))
				else:
					row[i].discard(x)
					col[j].discard(x)
					box[i2 + j//3].discard(x)

		# Sort open cells so that those with fewest possibilities will be
		# tried first.
		open_ordered = []
		for i, j, k in open:
			poss = row[i] & col[j] & box[k]
			open_ordered.append((len(poss), i, j, k))
  				  
		open_ordered.sort(reverse=True)
		open = [(i, j, k) for _, i, j, k in open_ordered]
		
		dfs(open)

"""
		# This is slow:
		# Runtime: 124 ms, faster than 79.28% of Python3 online submissions
		def poss(coords):
			i, j = coords[0], coords[1]
			return len( row[i] & col[j] & box[(i//3)*3 + j//3] )

		open.sort(reverse=True, key=poss)
		dfs(open)
"""

###############################################################################
"""
Solution 3: same as sol #2, but update "open" whenever the next cell has
more than one possibility.

Also use heapq instead of sorted list.  This doesn't seem to make a difference.

Runtime: 20 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
	def solveSudoku(self, board: List[List[str]]) -> None:
		def update_open(open):
			open_ordered = []
			for _, i, j, k in open:
				poss = row[i] & col[j] & box[k]
				heapq.heappush(open_ordered, (len(poss), i, j, k))
				#open_ordered.append((len(poss), i, j, k))

			#open_ordered.sort(reverse=True)
			return open_ordered
			
		def dfs(open):
			if not open:
				return True

			_, i, j, k = heapq.heappop(open)
			#_, i, j, k = open.pop()

			cand = row[i] & col[j] & box[k]
			if not cand:
				return False

			for c in cand:
				board[i][j] = c

				row[i].discard(c)
				col[j].discard(c)
				box[k].discard(c)

				# Only update open if the next candidate has more than 1 possibility.
				if open and open[0][0] > 1:
				#if open and open[-1][0] > 1:
					open = update_open(open)

				if dfs(open[:]):
					return True

				row[i].add(c)
				col[j].add(c)
				box[k].add(c)
				#board[i][j] = c # unnecessary since one of the c's must work

			return False

		# possible digits to use for filling cells in each row, col, or box
		row = [set(str(d) for d in range(1, 10)) for _ in range(9)]
		col = [set(str(d) for d in range(1, 10)) for _ in range(9)]
		box = [set(str(d) for d in range(1, 10)) for _ in range(9)]

		open = [] # list of coordinates where cell is '.'

		for i in range(9):
			#i2 = (i//3)*3
			i2 = i - i % 3
			for j in range(9):
				x = board[i][j]
				if x == '.':
					open.append((-1, i, j, i2 + j//3)) # -1 is dummy value
				else:
					row[i].discard(x)
					col[j].discard(x)
					box[i2 + j//3].discard(x)

		open = update_open(open)
		
		dfs(open)

###############################################################################
"""
Solution 4: same as sol #3, but use bitmasks instead of sets.
"""
class Solution4:
	def solveSudoku(self, board: List[List[str]]) -> None:
		def update_open(open):
			open_ordered = []
			for _, i, j, k in open:
				poss = row[i] & col[j] & box[k]
				n_bits = 0
				while poss:
					n_bits += 1
					poss &= (poss - 1)

				heapq.heappush(open_ordered, (n_bits, i, j, k))
				#open_ordered.append(n_bits, i, j, k))
			
			#open_ordered.sort(reverse=True)
			return open_ordered
			
		def dfs(open):
			if not open:
				return True

			_, i, j, k = heapq.heappop(open)
			#_, i, j, k = open.pop()

			cand = row[i] & col[j] & box[k]
			if cand == 0:
				return False
			
			c = 1
			while cand:
				if cand & 1 == 0:
					c += 1
					cand >>= 1
					continue

				board[i][j] = str(c)
				mask = ~(1 << (c-1))

				row[i] &= mask
				col[j] &= mask
				box[k] &= mask

				# Only update open if the next candidate has more than 1 possibility.
				if open and open[0][0] > 1:
				#if open and open[-1][0] > 1:
					open = update_open(open)

				if dfs(open[:]):
					return True

				mask = (1 << (c-1))
				row[i] |= mask
				col[j] |= mask
				box[k] |= mask

				#board[i][j] = c # unnecessary since one of the c's must work
				c += 1
				cand >>= 1

			return False

		# Possible digits to use for filling cells in each row, col, or box.
		row = [0b111111111 for _ in range(9)]
		col = [0b111111111 for _ in range(9)]
		box = [0b111111111 for _ in range(9)]

		open = [] # list of coordinates where cell is '.'

		for i in range(9):
			#i2 = (i//3)*3
			i2 = i - i % 3
			for j in range(9):
				x = board[i][j]
				if x == '.':
					open.append((-1, i, j, i2 + j//3)) # -1 is dummy value
				else:
					mask = ~(1 << int(x)-1)
					row[i] &= mask
					col[j] &= mask
					box[i2 + j//3] &= mask
		
		#print([bin(x) for x in row])
		open = update_open(open)
		
		dfs(open)

###############################################################################
"""
Solution 5: same as sol #4, but keep grid of digit candidates for each cell
rather than by "row", "col", and "box".
"""
class Solution5:
	def solveSudoku(self, board: List[List[str]]) -> None:
		def update_poss(x, i0, j0):
			mask = ~(1 << (int(x)-1))
			#print(f"\nmask = {mask} = {mask:0b}")

			for k in range(9):
				#print(f"Modifying: {i0},{k}")
				#print(f"Modifying: {k},{j0}")
				poss[i0][k] &= mask
				poss[k][j0] &= mask

			box_i = (i0 // 3) * 3 # 0, 3, 6
			box_j = (j0 // 3) * 3 # 0, 3, 6

			#box_i = i0 - (i0 % 3) # 0, 3, 6
			#box_j = j0 - (j0 % 3) # 0, 3, 6

			for i in range(box_i, box_i + 3):
				for j in range(box_j, box_j + 3):
					#print(f"Modifying: {i},{j}")
					poss[i][j] &= mask


		def restore_poss(x, i0, j0):
			mask = (1 << (int(x)-1))
			#print(f"\nmask = {mask} = {mask:0b}")

			for k in range(9):
				poss[i0][k] |= mask
				poss[k][j0] |= mask

			box_i = (i0 // 3) * 3 # 0, 3, 6
			box_j = (j0 // 3) * 3 # 0, 3, 6

			#box_i = i0 - (i0 % 3) # 0, 3, 6
			#box_j = j0 - (j0 % 3) # 0, 3, 6

			for i in range(box_i, box_i + 3):
				for j in range(box_j, box_j + 3):
					poss[i][j] |= mask

		def update_open(open):
			open_ordered = []
			for _, i, j in open:
				cand = poss[i][j]

				n_bits = 0
				while cand:
					n_bits += 1
					cand &= (cand - 1)

				heapq.heappush(open_ordered, (n_bits, i, j))
				#open_ordered.append((n_bits, i, j))
			
			#open_ordered.sort(reverse=True)
			return open_ordered

		def print_poss(c, i, j):
			print(f"c, i,j = {c}, {i},{j}\n")
			row = 0
			
			for r in poss:
				col = 0
				for c in r:
					print(f"{c:4}", end="")
					col += 1
					if col in (3, 6):
						print(" | ", end="")
				print()

				row += 1
				if row in (3, 6):
					print("-"*12 + "-+-" + "-"*12 + "-+-" + "-"*12)

		def dfs(open):
			#nonlocal count
			#count += 1
			#if count == 3:
			#	return
			if not open:
				return True

			_, i, j = heapq.heappop(open)
			#_, i, j = open.pop()

			cand = poss[i][j]
			if not cand:
				return False
			
			c = 1
			while cand:
				if cand & 1:
					board[i][j] = str(c)

					#print("\n### BEFORE UPDATE")
					#print_poss(c, i, j)

					old_poss = copy.deepcopy(poss)
					update_poss(c, i, j)
					#print("\n### AFTER UPDATE")
					#print_poss(c, i, j)

					# Only update open if the next candidate has more than 1 possibility.
					if open and open[0][0] > 1:
					#if open and open[-1][0] > 1:
						open = update_open(open)

					if dfs(open[:]):
						return True

					#restore_poss(c, i, j)				
					for i in range(9):
						for j in range(9):
							poss[i][j] = copy.deepcopy(old_poss[i][j])

					#print("\n### AFTER RESTORE")
					#print_poss(c, i, j)
					#board[i][j] = '.' # unnecessary since one of the c's must work

				c += 1
				cand >>= 1

			return False

		count = 0

		# Possible digits to use for filling each cell.
		poss = [[0b111111111]*9 for _ in range(9)]

		open = [] # list of coordinates where cell is '.'

		for i in range(9):
			for j in range(9):
				x = board[i][j]
				if x == '.':
					open.append((-1, i, j)) # -1 is dummy value
				else:
					update_poss(x, i, j)
		
		#print([bin(x) for x in row])
		open = update_open(open)
		
		#print(open)
		
		for r in poss:
			print(r)
		
		dfs(open)

###############################################################################
"""
Solution 6: same as sol #X, but keep grid of digit candidates for each cell
rather than by "row", "col", and "box".
"""
class Solution6:
	def solveSudoku(self, board: List[List[str]]) -> None:
		def calc_poss():
			
			poss = [
				[set(range(1,10)),set(range(1,10)),set(range(1,10)),
				set(range(1,10)),set(range(1,10)),set(range(1,10)),
				set(range(1,10)),set(range(1,10)),set(range(1,10))] for _ in range(9)]

			#open = [] # list of coordinates where cell is '.'

			for i in range(9):
				for j in range(9):
					x = board[i][j]
					#if x == '.':
					#	open.append((-1, i, j)) # -1 is dummy value
					#else:


					if x != '.':
						poss = update_poss(poss, x, i, j)
			
			return poss
						
		def update_poss(poss, x, i0, j0):
			
			x = int(x)
			for k in range(9):
				poss[i0][k].discard(x)
				poss[k][j0].discard(x)

			box_i = (i0 // 3) * 3 # 0, 3, 6
			box_j = (j0 // 3) * 3 # 0, 3, 6

			#box_i = i0 - (i0 % 3) # 0, 3, 6
			#box_j = j0 - (j0 % 3) # 0, 3, 6

			for i in range(box_i, box_i + 3):
				for j in range(box_j, box_j + 3):
					poss[i][j].discard(x)
			return poss

		def restore_poss(x, i0, j0):
			x = int(x)
			for k in range(9):
				poss[i0][k].add(x)
				poss[k][j0].add(x)

			box_i = (i0 // 3) * 3 # 0, 3, 6
			box_j = (j0 // 3) * 3 # 0, 3, 6

			#box_i = i0 - (i0 % 3) # 0, 3, 6
			#box_j = j0 - (j0 % 3) # 0, 3, 6

			for i in range(box_i, box_i + 3):
				for j in range(box_j, box_j + 3):
					poss[i][j].add(x)

		def update_open(open):
			open_ordered = []
			for _, i, j in open:
				cand = poss[i][j]
				heapq.heappush(open_ordered, (len(cand), i, j))
				#open_ordered.append((len(cand), i, j))
			
			#open_ordered.sort(reverse=True)
			return open_ordered

		def dfs(open, poss):
			#nonlocal poss
			if not open:
				return True

			_, i, j = heapq.heappop(open)
			#_, i, j = open.pop()
			
			cand = list(poss[i][j])
			#if not cand:
			if len(cand) == 0:
				return False
			#old_poss = copy.deepcopy(poss)
			
			for c in cand:
				board[i][j] = str(c)
				#update_poss(c, i, j)
				poss = calc_poss()

				# Only update open if the next candidate has more than 1 possibility.
				if open and open[0][0] > 1:
				#if open and open[-1][0] > 1:
					open = update_open(open)

				if dfs(open[:], poss):
					return True

				#poss = calc_poss()
				#restore_poss(c, i, j)
				#poss = copy.deepcopy(old_poss)

				#board[i][j] = str(c) # unnecessary since one of the c's must work

			return False

		# Possible digits to use for filling each cell.
		#poss = [[set(range(1,10))]*9 for _ in range(9)]
		poss = [
			[set(range(1,10)),set(range(1,10)),set(range(1,10)),
			set(range(1,10)),set(range(1,10)),set(range(1,10)),
			set(range(1,10)),set(range(1,10)),set(range(1,10))] for _ in range(9)]

		open = [] # list of coordinates where cell is '.'

		for i in range(9):
			for j in range(9):
				x = board[i][j]
				if x == '.':
					open.append((-1, i, j)) # -1 is dummy value
				else:
					poss = update_poss(poss, x, i, j)
		
		
		open = update_open(open)
		
		dfs(open, poss)

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

		sol.solveSudoku(grid)

		print(f"\nSolution:\n")
		for row in grid:
			for c in row:
				print(c, end=' ')
			print()
		print()


	sol = Solution()
	#sol = Solution2()
	sol = Solution3() # use heapq
	sol = Solution4() # use bitmasks
	sol = Solution5() # use bitmasks...
	#sol = Solution6() # 

	comment = "LC example"
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

	comment = "LC test case"
	grid = [
		[".",".","9","7","4","8",".",".","."],
		["7",".",".",".",".",".",".",".","."],
		[".","2",".","1",".","9",".",".","."],
		[".",".","7",".",".",".","2","4","."],
		[".","6","4",".","1",".","5","9","."],
		[".","9","8",".",".",".","3",".","."],
		[".",".",".","8",".","3",".","2","."],
		[".",".",".",".",".",".",".",".","6"],
		[".",".",".","2","7","5","9",".","."]]
	test(grid, comment)
	answer = [
		["5","1","9","7","4","8","6","3","2"],
		["7","8","3","6","5","2","4","1","9"],
		["4","2","6","1","3","9","8","7","5"],
		["3","5","7","9","8","6","2","4","1"],
		["2","6","4","3","1","7","5","9","8"],
		["1","9","8","5","2","4","3","6","7"],
		["9","7","5","8","6","3","1","2","4"],
		["8","3","2","4","9","1","7","5","6"],
		["6","4","1","2","7","5","9","8","3"]]
