"""
877. Stone Game
Medium

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Example 1:

Input: [5,3,4,5]
Output: true

Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 
Note:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""

from typing import List

###############################################################################
"""
Solution: DP, memoized.

Change game so whenever Lee scores points, it deducts from Alex's score instead.

dp(i, j) = largest score Alex can achieve when piles remaining are i..j.

Recurse in terms of dp(i+1, j) and dp(i, j-1).
This approach can output the correct answer because states form a DAG.

If Alex's turn, then she takes piles[i] or piles[j], increasing the score by
that amount. We are left with piles i+1,...,j or i,...,j-1. 
We want the max score.

If Lee's turn, then he takes piles[i] or piles[j], *decreasing* the score by
that amount. We want the *min* score.

https://leetcode.com/problems/stone-game/solution/

"""
import functools
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.lru_cache(None)
        def rec(start, end):
            if start > end:
                return 0

            if (n - end + start) % 2 == 1: # 1st player's turn for even or odd n
            #if (end - start) % 2 == 1: # 1st player's turn for even n
                return max(piles[start] + rec(start+1, end),
                    piles[end] + rec(start, end-1))
            
            else: # 2nd player's turn
                return min(-piles[start] + rec(start+1, end),
                    -piles[end] + rec(start, end-1))

        n = len(piles)

        return rec(0, n-1) > 0

"""
Solution 1b: same idea, but recursive function returns net score from
both player's side, alternating player with each recursive call.
"""
import functools
class Solution1b:
    def stoneGame(self, piles: List[int]) -> bool:
        @functools.lru_cache(None)
        def rec(start, end):
            if start > end:
                return 0

            return max(piles[start] - rec(start+1, end),
                piles[end] - rec(start, end-1))
            
        n = len(piles)

        return rec(0, n-1) > 0

###############################################################################
"""
Solution: DP, tabulation.

dp(i, j) = max score 1st player (Alex) can get if piles i..j are available

If pick piles[i], then result is piles[i] - dp[i+1][j].
If pick piles[j], then result is piles[j] - dp[i][j+1].

Choose the max of these.

O(n^2) time
O(n^2) extra space

https://leetcode.com/problems/stone-game/discuss/154610/DP-or-Just-return-true
"""
class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0]*n for _ in range(n)]

        for i in range(n): 
            dp[i][i] = piles[i]

        for d in range(1, n): # game w/ d+1 num of piles left
            for i in range(n-d): # start index of piles left
                dp[i][i+d] = max(piles[i] - dp[i+1][i+d],
                    piles[i+d] - dp[i][i+d-1])
        
        return dp[0][-1] > 0

###############################################################################
"""
Solution 3: DP, tabulation w/ 1d table.

In 2d tabulation solution, dp(i, i+d) depended on dp(i+1, i+d) and dp(i, i+d-1).
In both cases, there's one less pile.

Ie, dp(i) for d+1 piles depends on dp(i) and dp(i+1) for d piles.
If d and i are being processed in increasing order, then we can just use
a 1d table.

O(n^2) time
O(n) extra space
"""
class Solution3:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]

        for d in range(1, n): # game w/ d+1 num of piles left
            for i in range(n-d): # start index of piles left
                dp[i] = max(piles[i] - dp[i+1], piles[i+d] - dp[i])

        return dp[0] > 0

###############################################################################
"""
Solution 4: math.

Alex (first player) always wins the 2-pile game.

4-piles: a, b, c, d
If Alex takes a, then she can always take c.
If Alex takes d, then she can always take b.
Exactly one of a+c and b+d is larger, so Alex can pick accordingly.

n piles: a1, a2, ..., an, where n is even.
This can be partition into two sums: the even terms and the odd terms.
Exactly one of these sums is larger, so Alex can pick accordingly.

Therefore, Alex can always win.
"""
class Solution4:
    def stoneGame(self, piles: List[int]) -> bool:
        return True

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.stoneGame(arr)
        

        print(f"\nres = {res}\n")


    sol = Solution() # memo
    sol = Solution1b() # memo, alternate

    sol = Solution2() # tabulation w/ 2d table
    #sol = Solution3() # tabulation w/ 1d table
    
    #sol = Solution4() # math

    comment = "LC ex; answer = True"
    arr = [5,3,4,5]
    test(arr, comment)

    comment = "LC TC; answer = True"
    arr = [3,2,10,4]
    test(arr, comment)

    comment = "LC TC; answer = True"
    arr = [7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24]
    test(arr, comment)
