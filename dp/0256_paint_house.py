"""
256. Paint House
Easy

There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 0 with color red; costs[1][2] is the cost of painting house 1 with color green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
"""

from typing import List

###############################################################################
"""
Solution: keep track of min costs up to house i if last color picked was
red, blue, or green (index 0, 1, or 2, resp.).

n-by-3 matrix.
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        min0 = min1 = min2 = 0

        for c in costs:
            min0, min1, min2 = c[0] + min(min1, min2),\
                c[1] + min(min0, min2), \
                c[2] + min(min0, min1) 
            
            #print(f"{min0}, {min1}, {min2}")

        return min(min0, min1, min2)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.minCost(arr)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC example; answer = 10"
    arr = [[17,2,17],[16,16,5],[14,3,19]]
    test(arr, comment)

    comment = "LC test case; answer = 26"
    arr = [[3,5,3],[6,17,6],[7,13,18],[9,10,18]]
    test(arr, comment)
