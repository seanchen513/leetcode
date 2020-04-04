"""
1399. Count Largest Group
Easy

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 

Return how many groups have the largest size.

Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Example 3:

Input: n = 15
Output: 6

Example 4:

Input: n = 24
Output: 5
 
Constraints:
1 <= n <= 10^4
"""

import collections

###############################################################################
"""
Solution: brute force

For each integer from 1 to n, sum its digits.
Use a dict that maps sum of digits to a list of integers having that sum.
Find the max length among all lists (dict values).
Count how many dict entries (groups) have that max length.

sum of digits = 0, ..., 9
num groups = 1, ..., 10

O(nd) ~ O(n log n) time, where d is number of digits in n
O(n) extra space: for dict
"""
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def size(i):
            s = 0
            while i:
                s += i % 10
                i //= 10
            return s

        d = collections.defaultdict(list)

        for i in range(1, n+1):
            d[size(i)] += [i]
        
        mx = 0
        for v in d.values():
            if len(v) > mx:
                mx = len(v)

        count = 0
        for v in d.values():
            if len(v) == mx:
                count += 1

        return count

"""
Solution 1b: concise version of sol 1.
"""
class Solution1b:
    def countLargestGroup(self, n: int) -> int:

        d = collections.defaultdict(list)

        for i in range(1, n+1):
            size = sum(int(digit) for digit in str(i))
            # size = sum(list(map(int, str(i))))
            d[size] += [i]

        mx = len(max(d.values(), key=lambda x: len(x)))

        return sum(len(v) == mx for v in d.values())

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.countLargestGroup(n)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution1b() # concise version

    comment = "LC ex1; answer = 4"
    n = 13
    test(n, comment)

    comment = "LC ex1; answer = 2"
    n = 2
    test(n, comment)

    comment = "LC ex1; answer = 6"
    n = 15
    test(n, comment)

    comment = "LC ex4; answer = 5"
    n = 24
    test(n, comment)
