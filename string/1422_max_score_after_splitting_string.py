"""
1422. Maximum Score After Splitting a String
Easy

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:

Input: s = "011101"
Output: 5 

Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:

Input: s = "1111"
Output: 3
 
Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""

from typing import List

###############################################################################
"""
Solution: precompute total count of 1's and use it to calculate
suffix count of 1's.

O(n) time
O(1) extra space

LC ex1:

0 1 1 1 0 1
1 1 1 1 2 2     count of 0's
0 1 2 3 3 4     count of 1's = i + 1 - (count of 0's)

4 3 2 1 1 0     (total count of 1's) - current count of 1's
                = suffix count of 1's up to i+1 (ie, not including current index)

5 4 3 2 3 2     score = (count of 0's) + (total count of 1's) - current count of 1's
                = (count of 0's) + (total count of 1's) - (i + 1 - (count of 0's))
                = 2*(count of 0's) + (total count of 1's) - i - 1
                = [2*(count of 0's) - i] + (total count of 1's) - 1

n = 6
total 0's = 2
total 1's = 4

"""
class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        mx = 0

        zeros2x = 0 # count of 0's, but doubled
        ones = 1 if s[-1] == '1' else 0

        for i in range(n-1): # exclude last index because split is after i
            if s[i] == '0':
                zeros2x += 2
            else:
                ones += 1

            mx = max(mx, zeros2x - i)

        return mx + ones - 1

"""
Solution 1b: same, but use s.count('1').
"""
class Solution1b:
    def maxScore(self, s: str) -> int:
        n = len(s)
        mx = 0

        #t = sum(int(ch) for ch in s) # sum of digits = (count of 1's)
        zeros2x = 0 # count of 0's, but doubled

        for i in range(n-1): # exclude last index because split is after i
            if s[i] == '0':
                zeros2x += 2

            mx = max(mx, zeros2x - i)

        return mx + s.count('1') - 1

###############################################################################
"""
Solution 2: precompute suffix count of 1's. Then traverse array, counting 0's.
Score at each index is count of 0's, plus suffix count of 1's at next index.

O(n) time
O(n) extra space

LC ex1:
s = "011101"

prefix count of 1's = 0, 1, 2, 3, 3, 4

0  1  1  1  0  1     s
0  1  2  3  3  4     prefix count of 1's
4* 4  3  2  1  1     suffix count of 1's
 /  /  /  /  /
1  1  1  1  2  2*    count of 0's
5  4  3  2  3        score

* = ignored values

Split       0's on L    1's on R
0 - 11101   1           4
01 - 1101   1           3
011 - 101   1           2
0111 - 01   1           2
01110 - 1   2           1

"""
class Solution2:
    def maxScore(self, s: str) -> int:
        n = len(s)
        mx = 0
        
        # suffix count of 1's
        ones = [0] * n
        if s[-1] == '1':
            ones[-1] = 1 

        for i in range(n-2, -1, -1):
            ones[i] = ones[i+1] + (s[i] == '1')

        # 
        zeros = 0

        for i in range(n-1): # exclude last index because split is after i
            if s[i] == '0':
                zeros += 1

            mx = max(mx, zeros + ones[i+1])

        return mx

###############################################################################
"""
Solution 3: brute force using slicing and string.count().

O(n^2) time
O(n) extra space: for string slicing
"""
class Solution3:
    def maxScore(self, s: str) -> int:
        n = len(s)
        mx = 0
        
        for i in range(1, n):
            mx = max(mx, s[:i].count('0') + s[i:].count('1'))
            
        return mx

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr={arr}")

        res = sol.maxScore(s)

        print(f"\nres = {res}\n")


    sol = Solution() # precompute total count of 1's; use to calc suffix count of 1's
    sol = Solution2() # precompute suffix count of 1's
    sol = Solution3() # brute force using slicing and string.count()

    comment = "LC ex1; answer = 5"
    s = "011101"
    test(s, comment)

    comment = "LC ex2; answer = 5"
    s = "00111"
    test(s, comment)

    comment = "LC ex3; answer = 3"
    s = "1111"
    test(s, comment)

    comment = "LC TC; answer = 1"
    s = "00"
    test(s, comment)
