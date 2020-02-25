"""
414. Third Maximum Number
Easy

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

from typing import List

###############################################################################
"""
Solution 1: use max1, max2, max3.

O(n) time
O(1) extra space
"""
class Solution:
    def thirdMax(self, arr: List[int]) -> int:
        max1 = max2 = max3 = float('-inf') # 3 largest numbers, decreasing

        for x in arr:
            if x > max1:
                max1, max2, max3 = x, max1, max2
            elif max2 < x < max1:
                max2, max3 = x, max2
            elif max3 < x < max2:
                max3 = x

        print(f"max1, max2, max3 = {max1}, {max2}, {max3}")

        return max3 if max3 > float('-inf') else max1

###############################################################################
"""
Solution 2: use set.

O(n) time
O(n) extra space
"""
class Solution2:
    def thirdMax(self, arr: List[int]) -> int:
        s = set(arr)
        if len(s) < 3:
            return max(s)
        
        s.remove(max(s))
        s.remove(max(s))
        
        return max(s)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.thirdMax(arr)

        print(f"\nres = {res}")


    sol = Solution() # use max1, max2, max3
    sol = Solution2() # use set

    comment = "LC ex1; answer = 1"
    arr = [3,2,1]
    test(arr, comment)

    comment = "LC ex2; answer = 2"
    arr = [1,2]
    test(arr, comment)

    comment = "LC ex3; answer = 1"
    arr = [2,2,3,1]
    test(arr, comment)

