"""
1432. Max Difference You Can Get From Changing an Integer
Medium

You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888

Example 2:

Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8

Example 3:

Input: num = 123456
Output: 820000

Example 4:

Input: num = 10000
Output: 80000

Example 5:

Input: num = 9288
Output: 8700

Constraints:

1 <= num <= 10^8
"""

from typing import List

###############################################################################
"""
Solution: greedily maximize difference a - b by maximizing a and minimizing b.

O(k) time, where k = number of digits in n
O(k) extra space: for string

"""
class Solution:
    def maxDiff(self, n: int) -> int:
        #if n < 10: # max diff is 9 - 1 = 8
        #    return 8
        
        s = str(n)

        # For "a", find the first digit that is not 9, and replace all occurences
        # of it with 9. If all digits are 9, then no digits are replaced.
        a = s

        for d in s:
            if d != '9':
                a = s.replace(d, '9')
                break

        # For "b":
        # (Case 1) If first digit is 1, we can't replace it to make a smaller
        # valid integer. So look for the first digit that is > 1, and replace
        # all occurences of it with 0. If all digits are 0 or 1, then no digits
        # are replaced.
        # (Case 2) If first digit is not 1, then replace all occurences of 
        # that digit with 1.
        
        if s[0] == '1':
            b = s

            for d in s:
                if d != '0' and d != '1':
                    b = s.replace(d, '0')
                    break

        else:
            d = s[0]
            b = s.replace(d, '1')            

        # print(f"\na = {a}")
        # print(f"b = {b}")

        return int(a) - int(b)

"""

LC ex3:
123456

923456 = a  replaced 1 with 9
103456 = b  1st digit is 1; next digit > 1 is 2; replaced 2 with 0
------
820000

LC ex4:
10000

90000 = a   replaced 1 with 9
10000 = b   1st digit 1; no digits > 1 found after 1st digit, so no replacements
-----
80000

LC ex5:
9288

9988 = a    replaced 2 with 9
1288 = b    1st digit not 1, so replaced 1st digit 9 with 1
----
8700

LC TC: 
1101057

9909057 = a     replaced 1 with 9
1101007 = b     replaced 5 with 0
-------
8808050

"""
       
###############################################################################
"""
Solution 2: brute force

O(100k) = O(k) time, where k = num digits in n
O(k) extra space: for strings

"""
class Solution2:
    def maxDiff(self, n: int) -> int:
        s = str(n)
        mn = float('inf') # b
        mx = float('-inf') # a

        for i in '0123456789':
            for j in '0123456789':
                t = s.replace(i, j)
                if t[0] == '0':
                    continue

                mn = min(mn, int(t))
                mx = max(mx, int(t))

        return mx - mn

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.maxDiff(n)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = 888"
    n = 555
    test(n, comment)

    comment = "LC ex2; answer = 8"
    n = 9
    test(n, comment)

    comment = "LC ex3; answer = 820000"
    n = 123456
    test(n, comment)

    comment = "LC ex4; answer = 80000"
    n = 10000
    test(n, comment)

    comment = "LC ex5; answer = 8700"
    n = 9288
    test(n, comment)

    comment = "LC TC; answer = 8808050"
    n = 1101057
    test(n, comment)

    comment = "test that b == n; answer = 80808"
    n = 10101
    test(n, comment)

    comment = "test that a == n; answer = 88888"
    n = 99999
    test(n, comment)
