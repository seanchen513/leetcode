"""
462. Minimum Moves to Equal Array Elements II
Medium

Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""

from typing import List

###############################################################################
"""
Solution 1: use sorting to find median.

O(n log n) time: due to sorting
O(n) extra space: if don't modify input array

Runtime: 76 ms, faster than 78.40% of Python3 online submissions
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def minMoves2(self, arr: List[int]) -> int:
        s = sorted(arr)
        median = s[len(arr) // 2]

        return sum(abs(x - median) for x in s)

###############################################################################
"""
Solution 2: use sorting, but don't use median.

Suppose we want to adjust all array elts to k.  Then the min elt has to 
move k - min times, and the max elt has to move max - k times.  This totals
to max - min, which is independent of k.  Keep repeating this for the min and 
max of the remaining elements.  If there is one element left, it's value
isn't changed, and in fact it's the median.

O(n log n) time: due to sorting
O(n) extra space: if don't modify input array
"""
class Solution2:
    def minMoves2(self, arr: List[int]) -> int:
        n = len(arr) - 1
        m = len(arr) // 2

        s = sorted(arr)

        #return sum(s[n-i] - s[i] for i in range(m))

        # ~0 is -1, ~1 is -2, ~2 is -3, etc.
        return sum(s[~i] - s[i] for i in range(m))


###############################################################################
"""
Solution 3: Use quick-select o find median.

O(n^2) time worst case.  O(n) avg case.
O(1) extra space

TLE
"""
class Solution3:
    def minMoves2(self, arr: List[int]) -> int:
        def partition(left, right):
            pivot_val = arr[right]
            i = left
            for j in range(left, right+1):
                if arr[j] < pivot_val:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1
                    
            arr[i], arr[right] = arr[right], arr[i]
            return i

        def select(left, right, k):
            if left == right:
                return arr[left]

            pivot = partition(left, right)
            if k == pivot:
                return arr[k]
            elif k < pivot:
                return select(left, pivot - 1, k)
            else:
                return select(pivot + 1, right, k)


        n = len(arr)
        median = select(0, n-1, n//2)

        return sum(abs(x - median) for x in arr)

###############################################################################
"""
Solution 4: use median of medians to select pivot for quick-select.

NOT DONE

https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/solution/

O(n) time
O(1) extra space
"""
class Solution4:
    def minMoves2(self, arr: List[int]) -> int:
        def partition(l, r, val):
            pass

        def find_median(l, len):
            pass

        def kth_smallest(l, r, k):
            pass

        n = len(arr)
        median = kth_smallest(0, n, n//2 + 1)

        return sum(abs(x - median) for x in arr)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(arr)

        res = sol.minMoves2(arr)
        print(f"\nSolution: {res}\n")


    #sol = Solution()
    sol = Solution2()
    #sol = Solution3() # quick-select

    comment = "LC example; answer = 2"
    arr = [1,2,3]
    test(arr, comment)

    comment = "LC test case; answer = 14"
    arr = [1,0,0,8,6]
    test(arr, comment)
