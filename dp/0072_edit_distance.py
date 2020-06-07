"""
72. Edit Distance
Hard

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3

Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

###############################################################################
"""
Solution: memoized recursion.
"""
import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @functools.lru_cache(None)
        def rec(i, j):
            if i == 0:
                return j
            if j == 0:
                return i

            # if word1[i-1] == word2[j-1]:
            #     return rec(i-1, j-1) # signifantly faster
            #     #return min(rec(i-1, j) + 1, rec(i, j-1) + 1, rec(i-1, j-1))
            # else:
            #     return min(rec(i-1, j), rec(i, j-1), rec(i-1, j-1)) + 1
    
            return min(rec(i-1, j) + 1, rec(i, j-1) + 1, rec(i-1, j-1) + (word1[i-1] != word2[j-1]))

        return rec(len(word1), len(word2))

###############################################################################
"""
Solution 2: DP tabulation using 2d table.

O(mn) time
O(mn) extra space
"""
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        ### if one of the strings is empty
        # if m * n == 0:
        #    return m + n
        if not word1:
            return n
        if not word2:
            return m
        
        # dp table to store the conversion history
        d = [[0] * (n+1) for _ in range(m+1)]
        
        # init boundaries
        for i in range(m+1):
            d[i][0] = i
        for j in range(n+1):
            d[0][j] = j

        # DP compute        
        for i in range(1, m+1): # word1
            for j in range(1, n+1): # word2           
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                    #d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1])
                else:
                    d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
        
                #d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (word1[i-1] != word2[j-1]))

        return d[m][n] # dp[-1][-1]

"""
LC example:

horse
ros

horse
r * *

       #   R   O   S
       0   1   2   3
----+-----------------
# 0 |  0   1   2   3
H 1 |  1   1   2   3
O 2 |  2   2   1   2
R 3 |  3   2   2   2
S 4 |  4   3   3   2
E 5 |  5   4   4   3*


dp[0][j] = edit distance from '' to 'ros'[j]
dp[i][0] = edit distance from 'horse'[i] to ''

left: d[i][j-1]
- delete char from word1 (or insert char in word2)

up: d[i-1][j]
- insert char in word1 (or delete char from word2)

diagonal (left-up): d[i-1][j-1]
- if last chars of substrings match, ie, word1[i-1] == word2[j-1],
then d[i][j] = d[i-1][j-1]
- if last chars don't match, then substitute last char

Example of calculating last cell:

        j-1         j
    +----------+----------+
    | i-1, j-1 | i-1, j   |
i-1 | 3 + 1    | 2 + 1    |  |
    | or 3     |          |  |
    +----------+----------+  | insert char in word1
    | i, j-1   | i, j     |  v
i   | 4 + 1    | min(*)   |
    |          | = 3      |
    +----------+----------+
            ------->         diagonal: last chars match already,
    insert char in word2     OR substitute last char


###

  int en     tion
ex    e cu   tion

inten tion
ex* cu

"""

###############################################################################
"""
Solution 3: DP tabulation using 1d table.

O(mn) time
O(n) extra space
"""
class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if not word1:
            return n
        if not word2:
            return m
        
        # dp table
        d = [j for j in range(n+1)]
        
        # DP compute
        for i in range(1, m+1): # word1
            prev = d[0]

            # We don't care about the rest of the values of d since we don't make 
            # use of them below; they will be overwritten.
            d[0] = i # corresponds to d[i][j=0] in 2d table

            for j in range(1, n+1): # word2
                temp = d[j] # for use in next iteration; corresponds to d[i-1][j-1] in 2d table

                if word1[i-1] == word2[j-1]:
                    d[j] = prev # why???
                    #d[j] = min(d[j] + 1, d[j-1] + 1, prev)

                    ### corresponds to following for 2d table:
                    #d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1])
                
                else:
                    d[j] = min(d[j], d[j-1], prev) + 1

                    ### corresponds to following for 2d table:
                    #d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
        
                #d[j] = min(d[j] + 1, d[j-1] + 1, prev + (word1[i-1] != word2[j-1]))
                
                ### corresponds to following for 2d table:
                #d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + (word1[i-1] != word2[j-1]))

                prev = temp

        return d[n] # dp[-1]

###############################################################################

if __name__ == "__main__":
    def test(w1, w2, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nword1 = {w1}")
        print(f"word2= {w2}")

        res = sol.minDistance(w1, w2)

        print(f"\nres = {res}\n")


    sol = Solution() # memo'ized recursion
    sol = Solution2() # DP tabulation w/ 2d table
    sol = Solution3() # DP tabulation w/ 1d table

    comment = "LC ex1; answer = 3"
    word1 = "horse"
    word2 = "ros"
    test(word1, word2, comment)

    comment = "LC ex2; answer = 5"
    word1 = "intention"
    word2 = "execution"
    test(word1, word2, comment)

    comment = "; answer = 3"
    word1 = "kitten"
    word2 = "sitting"
    test(word1, word2, comment)
