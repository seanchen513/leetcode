"""
85. Maximal Rectangle
Hard

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

from typing import List

###############################################################################
"""
Solution: use monotone stack

O(mn) time
O(n) extra space: for heights array and stack
"""
class Solution:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])

        heights = [0] * n
        mx = 0

        for i in range(m):
            # Update heights for current row.
            for j in range(n):
                if mat[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            #heights = [heights[j] + 1 if mat[i][j] == '1' else 0 for j in range(n)]

            #
            stack = []

            for j in range(n):
                while stack and heights[j] < heights[stack[-1]]:
                    ht = heights[stack.pop()]
                    
                    #left = stack[-1] if stack else -1
                    #width = j - left - 1
                    width = j - stack[-1] - 1 if stack else j

                    mx = max(mx, ht * width)

                stack.append(j)

            while stack:
                ht = heights[stack.pop()]
                width =  n - stack[-1] - 1 if stack else n
                mx = max(mx, ht * width)

        return mx

"""
Solution 1b: same, but use dummy values...

"""
class Solution1b:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])

        heights = [0] * (n+1)
        mx = 0

        for i in range(m):
            # Update heights for current row.
            for j in range(n):
                if mat[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            #heights = [heights[j] + 1 if mat[i][j] == '1' else 0 for j in range(n)] + [0]

            #
            stack = [-1]

            for j in range(n+1):
                while heights[j] < heights[stack[-1]]:
                    ht = heights[stack.pop()]                   
                    width = j - stack[-1] - 1

                    mx = max(mx, ht * width)

                stack.append(j)

        return mx

"""
Solution 1c: same, but precalculate heights. Calculate largest possible histograms
first, and stop early if cannot possibly get a larger area.

"""
class Solution1c:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        mx = 0

        H = [[0] * (n+1) for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] == '1':
        #             H[i][j] = H[i-1][j] + 1
                    
        #             mx = max(mx, H[i][j])
        #             if H[i][j] > mx:
        #                 mx = H[i][j]

        for c in range(n):
            count = 0
            for r in range(m):
                if mat[r][c] == '1':
                    count += 1
                    H[r][c] = count

                    #mx = max(mx, count)
                    if count > mx:
                        mx = count

                else:
                    count = 0

        ###

        for i in range(m-1, -1, -1):
            if (i+1) * n <= mx:
                break

            heights = H[i]
            stack = [-1]

            for j in range(n+1):
                while heights[j] < heights[stack[-1]]:
                    ht = heights[stack.pop()]                   
                    width = j - stack[-1] - 1

                    #mx = max(mx, ht * width)
                    if ht * width > mx:
                        mx = ht * width

                stack.append(j)

        return mx

"""
Solution 1d: ...count 1s and check for early break

"""
class Solution1d:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])
        mx = 0

        H = [[0] * (n+1) for _ in range(m)]
        ones = [0] * m
        
        # for i, row in enumerate(mat):
        #     for j, cell in enumerate(row):
        #         if cell == '1':
        #             ones[i] += 1
        #             H[i][j] = H[i-1][j] + 1
                    
        #             #mx = max(mx, H[i][j])
        #             if H[i][j] > mx:
        #                 mx = H[i][j]

        for c in range(n):
            count = 0
            for r in range(m):
                if mat[r][c] == '1':
                    ones[r] += 1
                    
                    count += 1
                    H[r][c] = count
                    
                    if count > mx:
                        mx = count
                else:
                    count = 0
        
        #ones = [sum(mat[r][c] == '1' for c in range(n)) for r in range(m)]
        #ones = [sum(c == '1' for c in row) for row in mat]
        
        # Calculate running sums of 1's.
        for i in range(1, m):
            ones[i] += ones[i-1]        

        #print(ones)

        for i in range(m-1, -1, -1):
            if ones[i] <= mx:
                break

            heights = H[i]
            stack = [-1]

            for j in range(n+1):
                while heights[j] < heights[stack[-1]]:
                    ht = heights[stack.pop()]                   
                    width = j - stack[-1] - 1

                    #mx = max(mx, ht * width)
                    if ht * width > mx:
                        mx = ht * width

                stack.append(j)

        return mx

###############################################################################
"""
Solution 2: DP tabulation...

Each cell (i,j) that has value 1 is associated with a rectangle with 
base equal to the current row i, and with height equal to the number of 
consecutive 1s going up. The rectangle stretches as far left and right as 
possible, as long as the same height can be maintained.

height = number of consecutive 1's from current cell going up

left = index of inside left border of rectangle with height same as height
of current bar, height[j]

right = index of outside right border of rectangle with height same as height
of current bar, height[j]

DP recurrence relations:

left(i,j) = max(left(i-1,j), cur_left) # cur_left can be determined from current row

right(i,j) = min(right(i-1,j), cur_right) # cur_right can be determined from current row

height(i,j) 
    = height(i-1,j) + 1     if mat[i][j] == '1'
    = 0                     if mat[i][j] == '0'

https://leetcode.com/problems/maximal-rectangle/discuss/29054/Share-my-DP-solution

"""
class Solution2:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])

        height = [0] * n

        left = [0] * n # default value of 0 ensures max calc's work; also...
        right = [n] * n # default value of n ensures min calc's work; also...
        
        mx = 0

        for i in range(m):
            cur_left = 0
            cur_right = n

            # compute height (can do this from either side)
            # compute left (from left to right)
            for j in range(n):
                if mat[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1

            # compute right (from right to left)
            # compute area of rectangle (can do this from either side)
            for j in range(n-1, -1, -1):
                if mat[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                    mx = max(mx, (right[j] - left[j]) * height[j])
                else:
                    right[j] = n
                    cur_right = j

        return mx

###############################################################################
"""
IDEA:

LC example:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

4*5 = 20 total cells
13 1's, 7 0's

Possible areas considering just size of matrix:
1 * (1,2,3,4,5)
2 * (2,3,4,5)
3 * (4, 5)
4 * 5

Possible areas if also consider there are only 13 1's:
1 * (1,2,3,4,5)
2 * (2,3,4,5)
3 * 4


L matrix
length of 1's starting from... and going right...
1 0 1 0 0
1 0 1 2 3
1 2 3 4 5
1 0 0 1 0

H matrix
height of 1's start from... and going down...
1 0 1 0 0
2 0 2 1 1
3 1 3 2 2
4 0 0 3 0

L:
1 2 3
3 4 5*

H:
2 1 1
3 2 2

###
What is biggest rectangle ending at (2, 4) ?
From coords, we know possibilities are (1->3) * (1->5).

L[2][4] = 5
H[2][4] = 2

L-shape:
? ? ? ? Y
* * * * X

Possible areas: 1*5, 2*(1->5)
Check L[1][4] = 3.
So shape is:
0 0 * * 3
* * * * X

What if L was < H ? Or L = H ?

###
What is biggest rectangle ending at (2, 2)?
From coords, we know possibilities are (1->3) * (1->3).

L[2][2] = 3
H[2][2] = 3

L-shape:
? ? *
? ? *
* * X

Check L's above:
? ? 1       0 0 1
? ? 1   ->  0 0 1
* * X       * * X

Look at running mins of L's, traversing up: 3, 1, 1.

Check H's to left:
? ? *       * 0 *
? ? *   ->  * 0 *
3 1 X       3 1 X

Look at running mins of H's, traversing left: 3, 1, 3.

"""

"""
Solution 3: brute force

m * n matrix

At (r, c).
Largest possible matrix starting at (r, c) is:
(m - r) * (n - c)
If this is < mx, then return.

To check largest matrix starting at (r, c):
1. Check that mat[r][c] == 1.
2. Check how far we can go right. L
3. Check how far we can go down. H
4. Go row by row. Take running min of lengths of 1s, and multiply by
running height. Stop when hit first 0 that starts a row.

* Not necessary but improves LC running time:
Precalculate D matrix. D[r][c] tells us how far we can go down with 1's from
cell (r, c). The product L * R at (r, c) is an upper bound to any rectangle 
starting at (r, c). Updating mx while doing this precalculation of D can also
help to increase mx before further calculations.

"""
class Solution3:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])

        mx = 0 # max area of any rectangle of 1's

        # precalculate how far we can go right with 1s from each cell
        R = [[0] * n for _ in range(m)]

        for r in range(m):
            count = 0
            for c in range(n-1, -1, -1):
                if mat[r][c] == '1':
                    count += 1
                    R[r][c] = count
                    mx = max(mx, count)
                else:
                    count = 0

        # precalculate how far we can go down with 1s from each cell
        D = [[0] * n for _ in range(m)]

        for c in range(n):
            count = 0
            for r in range(m-1, -1, -1):
                if mat[r][c] == '1':
                    count += 1
                    D[r][c] = count
                    mx = max(mx, count)
                else:
                    count = 0

        # print()
        # for row in R:
        #     print(row)
        # return

        # print()
        # for row in D:
        #     print(row)
        # #return

        # print(f"mx = {mx}")

        for r in range(m):
            max_height = m - r
            if max_height * n <= mx:
                break
                
            for c in range(n):
                if max_height * (n - c) <= mx:
                    break

                if mat[r][c] == '0':
                    continue

                min_l = R[r][c] # length, going right
                if min_l * D[r][c] <= mx: # D[r][c] is height of 1's, going down
                    continue

                i = r + 1
                while i < m and mat[i][c] == '1':
                    min_l = min(min_l, R[i][c])
                    mx = max(mx, min_l * (i - r + 1))
                    i += 1

        return mx

"""
Solution 3b: same, but combine calculations of R and D in one nested loop.

Approx same LC run time.
"""
class Solution3b:
    def maximalRectangle(self, mat: List[List[str]]) -> int:
        if not mat:
            return 0

        m = len(mat)
        n = len(mat[0])

        mx = 0 # max area of any rectangle of 1's

        # precalculate how far we can go right with 1s from each cell
        R = [[0] * n for _ in range(m)]
        # precalculate how far we can go down with 1s from each cell
        D = [[0] * n for _ in range(m)]

        for r in range(m-1, -1, -1):
            count = 0
            for c in range(n-1, -1, -1):
                if mat[r][c] == '1':
                    count += 1
                    R[r][c] = count

                    if r == m-1:
                        D[r][c] = 1
                    else:
                        D[r][c] = D[r+1][c] + 1

                    mx = max(mx, count, D[r][c])

                else:
                    count = 0

        # print()
        # for row in R:
        #     print(row)
        # return

        # print()
        # for row in D:
        #     print(row)
        #return

        # print(f"mx = {mx}")

        for r in range(m):
            max_height = m - r
            if max_height * n <= mx:
                break
                
            for c in range(n):
                if max_height * (n - c) <= mx:
                    break

                if mat[r][c] == '0':
                    continue

                min_l = R[r][c] # length, going right
                if min_l * D[r][c] <= mx: # D[r][c] is height of 1's, going down
                    continue

                i = r + 1
                while i < m and mat[i][c] == '1':
                    min_l = min(min_l, R[i][c])
                    mx = max(mx, min_l * (i - r + 1))
                    i += 1

        return mx

###############################################################################

if __name__ == "__main__":
    def test(grid, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        if len(grid) < 20 and grid and len(grid[0]) < 20:
            print()
            for row in grid:
                for x in row:
                    print(f"{x:3}", end="")
                print()

        ### Convert grid values to strings.
        for i in range(len(grid)):
            grid[i] = list(map(str, grid[i]))

        res = sol.maximalRectangle(grid)

        print(f"\nres = {res}\n")


    sol = Solution() 
    #sol = Solution1b() # use dummy values
    #sol = Solution1c() #  
    sol = Solution1d() # 
    
    sol = Solution2() # DP, ...
    
    #sol = Solution3() # brute force
    #sol = Solution3b() # brute force, but combine calcs of R and D in one nested loop

    comment = "LC example; answer = 6"
    grid = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    test(grid, comment)
    
    comment = "; answer = 6"
    grid = [
        [1,0,1,0,0],
        [1,0,1,1,1],
        [1,1,1,1,1],
        [1,0,0,1,0]]
    test(grid, comment)

    comment = "LC TC; answer = 0"
    grid = []
    test(grid, comment)

    comment = "LC TC; answer = 4"
    grid = [["1","1"],["1","1"]]
    test(grid, comment)

    comment = "; answer = 6"
    grid = [
        [0,0,0,1,0,0,0], 
        [0,0,1,1,1,0,0], 
        [0,1,1,1,1,1,0]]
    test(grid, comment)

    comment = "; answer = 6"
    grid = [
        [0,1,1,1,1,1,0],
        [0,0,1,1,1,0,0],
        [0,0,0,1,0,0,0]]
    test(grid, comment)

    comment = "; answer = 12"
    grid = [
        [1,1,1,0,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [0,0,0,0,1,1,1,1],
        [0,0,0,0,1,1,1,1]]
    test(grid, comment)

    comment = "; answer = 1,000,000"
    grid = [[1] * 1000  for _ in range(1000)]
    test(grid, comment)
