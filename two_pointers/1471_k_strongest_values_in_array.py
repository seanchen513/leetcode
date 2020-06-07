"""
1471. The k Strongest Values in an Array
Medium

Given an array of integers arr and an integer k.

A value arr[i] is said to be stronger than a value arr[j] if |arr[i] - m| > |arr[j] - m| where m is the median of the array.
If |arr[i] - m| == |arr[j] - m|, then arr[i] is said to be stronger than arr[j] if arr[i] > arr[j].

Return a list of the strongest k values in the array. return the answer in any arbitrary order.

Median is the middle value in an ordered integer list. More formally, if the length of the list is n, the median is the element in position ((n - 1) / 2) in the sorted list (0-indexed).

    For arr = [6, -3, 7, 2, 11], n = 5 and the median is obtained by sorting the array arr = [-3, 2, 6, 7, 11] and the median is arr[m] where m = ((5 - 1) / 2) = 2. The median is 6.
    For arr = [-7, 22, 17, 3], n = 4 and the median is obtained by sorting the array arr = [-7, 3, 17, 22] and the median is arr[m] where m = ((4 - 1) / 2) = 1. The median is 3.

Example 1:

Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]

Explanation: Median is 3, the elements of the array sorted by the strongest are [5,1,4,2,3]. The strongest 2 elements are [5, 1]. [1, 5] is also accepted answer.
Please note that although |5 - 3| == |1 - 3| but 5 is stronger than 1 because 5 > 1.

Example 2:

Input: arr = [1,1,3,5,5], k = 2
Output: [5,5]

Explanation: Median is 3, the elements of the array sorted by the strongest are [5,5,1,1,3]. The strongest 2 elements are [5, 5].

Example 3:

Input: arr = [6,7,11,7,6,8], k = 5
Output: [11,8,6,6,7]

Explanation: Median is 7, the elements of the array sorted by the strongest are [11,8,6,6,7,7].
Any permutation of [11,8,6,6,7] is accepted.

Example 4:

Input: arr = [6,-3,7,2,11], k = 3
Output: [-3,11,2]

Example 5:

Input: arr = [-7,22,17,3], k = 2
Output: [22,17]

Constraints:

    1 <= arr.length <= 10^5
    -10^5 <= arr[i] <= 10^5
    1 <= k <= arr.length

"""

from typing import List

###############################################################################
"""
Solution: first sort to find "median". Then use 2 pointers on sorted array
to find where boundaries of k strongest values are.

In the sorted array, the "median" is near the middle. The strongest values
will be towards the ends of the sorted array.

O(n log n) time: due to sorting.
O(n) extra space if don't modify input array.

"""
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        s = sorted(arr)

        m = s[(n-1)//2] # "median" per LeetCode

        # bounds of inclusive range, outside of which are the strongest values
        i = 0
        j = n - 1

        for _ in range(k):
            if s[j] - m >= m - s[i]: # s[j] is stronger
                j -= 1
            else:
                i += 1

        return s[:i] + s[j+1:]

###############################################################################
"""
Solution 2: first sort to find "median". Then sort a second time with custom
comparator.

Values are stronger if further from median, or if tie, if value greater.

Return strongest k values.

O(n log n) time: due to sorting.
O(n) extra space if don't modify input array.

This is slower than sol 1 because it sorts twice.
"""
import functools
class Solution2:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        s = sorted(arr)

        m = s[(n-1)//2]

        def comp(x, y):
            d = abs(x - m) - abs(y - m)
            
            if d == 0:
               return x - y
            
            return d

        s = sorted(arr, key=functools.cmp_to_key(comp), reverse=True)

        return s[:k]

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        res = sol.getStrongest(arr, k)

        print(f"\nres = {res}\n")

    sol = Solution() # sort once to find median; then use 2 ptrs...
    #sol = Solution2() # sort twice; the 2nd time w/ a custom comparator
    
    comment = "LC ex1; answer = [5,1]"
    arr = [1,2,3,4,5]
    k = 2
    test(arr, k, comment)

    comment = "LC ex2; answer = [5,5]"
    arr = [1,1,3,5,5]
    k = 2
    test(arr, k, comment)

    comment = "LC ex3; answer = [11,8,6,6,7]"
    arr = [6,7,11,7,6,8]
    k = 5
    test(arr, k, comment)

    comment = "LC ex4; answer = [-3,11,2]"
    arr = [6,-3,7,2,11]
    k = 3
    test(arr, k, comment)
    
    comment = "LC ex5; answer = [22,17]"
    arr = [-7,22,17,3]
    k = 2
    test(arr, k, comment)
    