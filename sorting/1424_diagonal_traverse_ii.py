"""
1424. Diagonal Traverse II
Medium

Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]

Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
There at most 10^5 elements in nums.

"""

from typing import List
import collections

###############################################################################
"""
Solution: Traverse all elements and append to list as (r+c, c, row[c]).
Then sort list and output values (3rd elt of tuple).

0,0  0,1   0,2   0,3
1,0  1,1   1,2   
2,0  2,1
3,0

Elements of the same diagonal have the same sum r+c.
Within a diagonal, elements with smaller c or larger r come first.

sum = r+c = 0, 1, 2, ...
r = sum, sum-1, ..., 0

"""
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        res = []

        for r in range(m):
            row = nums[r]
            n = len(row)

            for c in range(n):
                res.append((r+c, c, row[c]))

        res.sort()

        return [x for _, _, x in res]

###############################################################################
"""
Solution 2: use dict to map diagonal sum r+c to list of values. Then traverse
dict keys (diagonal sums) in sorted order. Elements of each list d[k] need
to be added to output in reverse order.

LC ex1:

1 2 3
4 5 6
7 8 9

after parsing 1st row:
0: 1
1: 2
2: 3

after parsing 2n row:
0: 1
1: 2, 4
2: 3, 5
3: 6

after parsing 3rd row:
0: 1
1: 2, 4
2: 3, 5, 7
3: 6, 8
4: 9

"""
class Solution2:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        d = collections.defaultdict(list)

        for r in range(m):
            row = nums[r]
            
            # for c in range(len(row)):
            #     d[r+c].append(row[c])
            for c, x in enumerate(row):
                d[r+c].append(x)
                
        res = []

        for k in sorted(d): # k = sum of diagonal
            res.extend(reversed(d[k]))

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        res = sol.findDiagonalOrder(arr)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution2()

    comment = "LC ex1; answer = [1,4,2,7,5,3,8,6,9]"
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    test(arr, comment)

    comment = "LC ex2; answer = [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]"
    arr = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    test(arr, comment)

    comment = "LC ex3; answer = [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]"
    arr = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
    test(arr, comment)

    comment = "LC ex4; answer = [1,2,3,4,5,6]"
    arr = [[1,2,3,4,5,6]]
    test(arr, comment)
    