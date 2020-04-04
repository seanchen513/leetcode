"""
1402. Reducing Dishes
Hard

A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by its satisfaction level  i.e.  time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.

Example 1:

Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total Like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14). Each dish is prepared in one unit of time.

Example 2:

Input: satisfaction = [4,3,2]
Output: 20
Explanation: Dishes can be prepared in any order, (2*1 + 3*2 + 4*3 = 20)

Example 3:

Input: satisfaction = [-1,-4,-5]
Output: 0
Explanation: People don't like the dishes. No dish is prepared.

Example 4:

Input: satisfaction = [-2,5,-1,0,3,-3]
Output: 35

Constraints:

n == satisfaction.length
1 <= n <= 500
-10^3 <= satisfaction[i] <= 10^3
"""

from typing import List

###############################################################################
"""
Solution: greedy. Sort in reverse so we choose the most satisfying dishes
first.

time[i] * s[i]

O(n log n) time: for sorting
O(1) extra space: if sort in place; otherwise O(n)
"""
class Solution:
    #def maxSatisfaction(self, satisfaction: List[int]) -> int:
    def maxSatisfaction(self, s: List[int]) -> int:
        total = 0
        res = 0

        for sat in reversed(sorted(s)):
            # Once total + sat < 0, it stays < 0. Reason:
            # new res < res.
            # new total < total.
            # next iteration: new sat < sat, 
            # so (new total) + (new sat) < total + sat.
            if total + sat < 0:
                break

            res += total + sat 
            total += sat

        return res


"""
LC ex1:

-1 -8 0 5 -9
   x       x
1     2 3

sorted
-9 -8 -1 0 5
x  x  1  2 3
      -1 0 15 = 14


start:
5   sum = 5
1
5 = 5

0 5 sum = 5
1 2
0 10 = 10

-1 0 5     sum = 4
1  2 3
-1 0 15 = 14

prev + sum + new = 10 + 5 - 1 = 14

-8 -1 0 5 
1   2 3 4
-8 -2 0 20 = 10

prev + sum + new = 14 + 4 - 8 = 10
"""

"""
LC TC:

[-1,-8,0,5,-7]
ans = 14

sorted
-8 -7 -1 0 5

-1 0 5 sum = 4
1  2 3 
-1 0 15 = 14

-7 -1 0 5
1  2  3 4
-7 -2 0 20 = 11

prev + sum + new = 14 + 4 -7 = 11

"""

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.maxSatisfaction(arr)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = 14"
    arr = [-1,-8,0,5,-9]
    test(arr, comment)

    comment = "LC ex2; answer = 20"
    arr = [4,3,2]
    test(arr, comment)

    comment = "LC ex3; answer = 0"
    arr = [-1,-4,-5]
    test(arr, comment)

    comment = "LC ex4; answer = 35"
    arr = [-2,5,-1,0,3,-3]
    test(arr, comment)

    comment = "LC TC; answer = 14"
    arr = [-1,-8,0,5,-7]
    test(arr, comment)
