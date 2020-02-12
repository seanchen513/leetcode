"""
453. Minimum Moves to Equal Array Elements
Easy

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

from typing import List

###############################################################################
"""
Solution: Incrementing n-1 elements by 1 is the same as incrementing all n 
elements by 1 and then decrement one element by 1.  For the sake of just having
equal array elements, this is the same as just decrementing one element by 1.
If we can only decrement, then we need to make all elements equal to the 
minimum element.
"""
class Solution:
    def minMoves(self, arr: List[int]) -> int:
        min_val = min(arr)

        return sum(x - min_val for x in arr)

###############################################################################
"""
Solution 2: same as sol #1, but moved operations around.
"""
class Solution2:
    def minMoves(self, arr: List[int]) -> int:
        return sum(arr) - min(arr) * len(arr)

###############################################################################
"""
Solution 3: same as sol #1, but one pass.
"""
class Solution3:
    def minMoves(self, arr: List[int]) -> int:
        min_val = float('inf')
        s = 0

        for x in arr:
            if x < min_val:
                min_val = x
            s += x

        return s - min_val * len(arr)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(arr)

        res = sol.minMoves(arr)
        print(f"\nSolution: {res}\n")


    sol = Solution()
    sol2 = Solution()
    sol3 = Solution()

    comment = "LC example; answer = 3"
    arr = [1,2,3]
    test(arr, comment)
