"""
1143. Longest Common Subsequence
Medium

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 
Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""

###############################################################################
"""
Solution: DP, recursion w/ memoization via functools.lru_cache().

Let dp[i][j] = length of longest common subsequence of
s1(0..i) = s1[:i+1] and 
s2(0..j) = s2[:j+1].

dp[i][j] 
= dp[i-1][j-1] + 1              if s1[i] == s2[j]
= max( dp[i][j-1], dp[i-1][j] ) if s1[i] != s2[j]

(i, j) = (i-1, j-1) + 1
(i, j) = max[(i-1, j), (i, j-1)]

Boundary conditions:

dp[i][0] = length of longest common subsequence of s1(0..i) and ch := s2[0].
Equal to 0 until the first char in s1 that equals ch.
Then equals 1 for the rest of s1.

dp[0][j] = length of longest common subsequence of ch := s1[0] and s2(0..j).
Equal to 0 until the first char in s2 that equals ch.
Then equals 1 for the rest of s2.

DP relations reduce to:
dp[i][0] = 1            if s1[i] == s2[0]
dp[i][0] = dp[i-1][0]   if s1[i] != s2[0]

dp[0][j] = 1            if s1[0] == s2[j]
dp[0][j] = dp[0][j-1]   if s1[0] != s2[j]

Basically, set dp[i][j] to 0 if i == -1 or j == -1.

"""
import functools
class Solution:
    #def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        @functools.lru_cache(None)
        def rec(i, j):
            if i < 0 or j < 0:
                return 0

            if s1[i] == s2[j]:
                return rec(i-1, j-1) + 1

            return max(rec(i-1, j), rec(i, j-1))

        m = len(s1)
        n = len(s2)        

        return rec(m-1, n-1)

###############################################################################
"""
Solution 2: DP, tabulation using 2d table.

Example:
s1 = "ace"
s2 = "xabccde"

    x   a   b   c   c   d   e
a   0   1*  1   1   1   1   1
c   0   1   1   2*  2   2   2
e   0   1   1   2   2   2   3*

* = where s1[i] == s2[j] for first time on row i

    0   1   2   3   4   5   6
0      
1          
2          

        j-1:        j:
==========================
i-1: |  i-1, j-1    i-1, j
i:   |  i,   j-1    i,   j

O(mn) time
O(mn) space: for dp table
"""
class Solution2:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)        

        dp = [[0] * n for _ in range(m)]
        
        ch = s2[0]
        for i in range(m):
            if s1[i] == ch:
                for i2 in range(i, m):
                    dp[i2][0] = 1
                break
        
        ch = s1[0]
        for j in range(n):
            if s2[j] == ch:
                for j2 in range(j, n):
                    dp[0][j2] = 1
                break

        for i in range(1, m):
            ch = s1[i]

            for j in range(1, n):
                if ch == s2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])


        return dp[-1][-1] # dp[m-1][n-1]

"""
Solution 2b: DP, tabulation using 2d table.
Use padded dp table to avoid separate initialization.

Example:
s1 = "ace"
s2 = "xabccde"

         0   1   2   3   4   5   6   7
        pad  x   a   b   c   c   d   e
       --------------------------------
0  pad | 0   0   0   0   0   0   0   0
1   a  | 0   0   1*  1   1   1   1   1
2   c  | 0   0   1   1   2*  2   2   2
3   e  | 0   0   1   1   2   2   2   3*

* = where s1[i] == s2[j] for first time on row i

        j-1:        j:
==========================
i-1: |  i-1, j-1    i-1, j
i:   |  i,   j-1    i,   j

O(mn) time
O(mn) space: for dp table
"""
class Solution2b:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)        

        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            ch = s1[i-1]

            for j in range(1, n+1):
                if ch == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1] # dp[m][n]

###############################################################################
"""
Solution 3: DP tabulation w/ 1d table.

        j-1:        j:
==========================
i-1: |  i-1, j-1    i-1, j
i:   |  i,   j-1    i,   j

O(mn) time
O(min(m,n)) space: for dp table
"""
class Solution3:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # Make s2 the smaller string, so the dp table will be smaller.
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m = len(s1)
        n = len(s2) # n <= m

        dp = [0] * n
        
        # Initialize the dp table by comparing s1[0] and s2[j].
        # This corresponds to the 1st row of the 2d table: dp[0][j].
        ch = s1[0]
        for i in range(n):
            if s2[i] == ch:
                for i2 in range(i, n):
                    dp[i2] = 1
                break
        
        for i in range(1, m):
            ch = s1[i]

            #curr = dp[0] # alternative (2)
            prev = dp[0] # alternative (1)

            if ch == s2[0]: # else dp[0] stays whatever it was before (0 or 1)
                dp[0] = 1

            for j in range(1, n):
                #prev, curr = curr, dp[j] # alternative (2)
                curr = dp[j] # prev is dp[i-1][j-1] in 2d table; alternative (1)

                if ch == s2[j]:
                    dp[j] = prev + 1 # prev = dp[j-1] for i-1
                
                # else:
                #     dp[j] = max(dp[j], dp[j-1])
                elif dp[j] < dp[j-1]: # else dp[j] stays whatever it was before
                    dp[j] = dp[j-1]

                prev = curr # alternative (1)

        return dp[-1] # dp[m-1]
        
"""
Solution 3b: same, but use padded 1d table to avoid separate initialization.

"""
class Solution3b:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # Make s2 the smaller string, so the dp table will be smaller.
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m = len(s1)
        n = len(s2) # n <= m

        dp = [0] * (n+1)
        
        for i in range(1, m+1):
            ch = s1[i-1]

            curr = 0 # temporary holder for old value of dp[j]

            for j in range(1, n+1):
                prev, curr = curr, dp[j] # alternative to using prev/curr

                if ch == s2[j-1]:
                    dp[j] = prev + 1 # prev = dp[j-1] for i-1
                
                # else:
                #     dp[j] = max(dp[j], dp[j-1])
                elif dp[j] < dp[j-1]: # else dp[j] stays whatever it was before
                    dp[j] = dp[j-1]

        return dp[-1] # dp[m]

"""
Solution 3c: same as sol 3b, but prev and curr are coded differently
(same meaning).

"""
class Solution3c:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # Make s2 the smaller string, so the dp table will be smaller.
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        m = len(s1)
        n = len(s2) # n <= m

        dp = [0] * (n+1)
        
        for i in range(1, m+1):
            ch = s1[i-1]

            prev = 0 # prev = dp[j-1] for i-1

            for j in range(1, n+1):
                curr = dp[j] # temporary holder for old value of dp[j]

                if ch == s2[j-1]:
                    dp[j] = prev + 1 # prev = dp[j-1] for i-1
                
                # else:
                #     dp[j] = max(dp[j], dp[j-1])
                elif dp[j] < dp[j-1]: # else dp[j] stays whatever it was before
                    dp[j] = dp[j-1]

                prev = curr

        return dp[-1] # dp[m]

###############################################################################

if __name__ == "__main__":
    def test(s1, s2, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns1 = {s1}")
        print(f"s2 = {s2}")

        res = sol.longestCommonSubsequence(s1, s2)        
            
        print(f"\nresult = {res}\n")


    sol = Solution() # DP recursion, memoized via functools.lru_cache()

    sol = Solution2() # DP tabulation w/ 2d table
    sol = Solution2b() # DP tabulation w/ padded 2d table
    
    #sol = Solution3() # DP tabulation w/ 1d table
    #sol = Solution3b() # same, but use padded 1d table
    sol = Solution3c() # same, but code prev/curr differently

    comment = "LC ex1; answer = 3"
    s1 = "abcde"
    s2 = "ace" 
    test(s1, s2, comment)

    comment = "LC ex2; answer = 3"
    s1 = "abc"
    s2 = "abc" 
    test(s1, s2, comment)

    comment = "LC ex3; answer = 0"
    s1 = "abc"
    s2 = "def" 
    test(s1, s2, comment)

    comment = "LC TC; answer = 1"
    s1 = "bl"
    s2 = "yby"
    test(s1, s2, comment)

    comment = "; answer = 3"
    s1 = "ace"
    s2 = "xabccde"
    test(s1, s2, comment)
