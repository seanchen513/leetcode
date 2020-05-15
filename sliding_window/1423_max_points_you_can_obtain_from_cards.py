"""
1423. Maximum Points You Can Obtain from Cards
Medium

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.

Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.

Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 

Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
 
Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length
"""

from typing import List

###############################################################################
"""
Solution: look for complement subarray with minimum sum.

Cases:
k from left: complement is n-k from right
k from right: complement is n-k from left
some from left and some from right: complement is n-k from middle

O(n) time
O(1) extra space (ignore array slicing for arr[:m])
"""
class Solution:
    #def maxScore(self, cardPoints: List[int], k: int) -> int:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        m = n - k # size of complement array

        s = sum(arr[:m]) # sum of complement array
        mn = s # min sum of complement array
        total_sum = s

        # last start index satisfies: (n-1) - last + 1 = m
        # so last = n - m = n - (n-k) = k
        #for i in range(1, k+1): # start index of complement array

        for i in range(m, n): # end index of complement array
            total_sum += arr[i]
            s += arr[i] - arr[i-m]

            if s < mn:
                mn = s

        return total_sum - mn

###############################################################################
"""
Solution 2: brute force
"""
class Solution2:
    #def maxScore(self, cardPoints: List[int], k: int) -> int:
    def maxScore(self, arr: List[int], k: int) -> int:
        n = len(arr)
        mx = s = sum(arr[:k])
        if k == n:
            return mx
        
        for i in range(k): 
            s -= arr[k-1-i]
            s += arr[n-1-i]

            mx = max(mx, s)

        return mx

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        print(f"k = {k}")

        res = sol.maxScore(arr, k)

        print(f"\nres = {res}\n")


    sol = Solution() # look for complement subarray with min sum
    #sol = Solution2() # brute force

    comment = "LC ex1; answer = 12"
    arr = [1,2,3,4,5,6,1]
    k = 3
    test(arr, k, comment)

    comment = "LC ex2; answer = 4"
    arr = [2,2,2]
    k = 2
    test(arr, k, comment)

    comment = "LC ex3; answer = 55"
    arr = [9,7,7,9,7,7,9]
    k = 7
    test(arr, k, comment)

    comment = "LC ex4; answer = 1"
    arr = [1,1000,1]
    k = 1
    test(arr, k, comment)

    comment = "LC ex5; answer = 202"
    arr = [1,79,80,1,1,1,200,1]
    k = 3
    test(arr, k, comment)
