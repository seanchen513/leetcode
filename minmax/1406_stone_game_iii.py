"""
1406. Stone Game III
Hard

Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2 or 3 stones from the first remaining stones in the row.

The score of each player is the sum of values of the stones taken. The score of each player is 0 initially.

The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.

Assume Alice and Bob play optimally.

Return "Alice" if Alice will win, "Bob" if Bob will win or "Tie" if they end the game with the same score.

Example 1:

Input: values = [1,2,3,7]
Output: "Bob"
Explanation: Alice will always lose. Her best move will be to take three piles and the score become 6. Now the score of Bob is 7 and Bob wins.

Example 2:

Input: values = [1,2,3,-9]
Output: "Alice"
Explanation: Alice must choose all the three piles at the first move to win and leave Bob with negative score.
If Alice chooses one pile her score will be 1 and the next move Bob's score becomes 5. The next move Alice will take the pile with value = -9 and lose.
If Alice chooses two piles her score will be 3 and the next move Bob's score becomes 3. The next move Alice will take the pile with value = -9 and also lose.
Remember that both play optimally so here Alice will choose the scenario that makes her win.

Example 3:

Input: values = [1,2,3,6]
Output: "Tie"
Explanation: Alice cannot win this game. She can end the game in a draw if she decided to choose all the first three piles, otherwise she will lose.

Example 4:

Input: values = [1,2,3,-1,-2,-3,7]
Output: "Alice"

Example 5:

Input: values = [-1,-2,-3]
Output: "Tie"
 
Constraints:

1 <= values.length <= 50000
-1000 <= values[i] <= 1000

"""

from typing import List
import collections

###############################################################################
"""
Solution: minmax game, DP using memoized recursion.

TLE w/o memoization.

Runtime: 2896 ms, faster than 86.26% of Python3 online submissions
Memory Usage: 220.7 MB, less than 100.00% of Python3 online submissions
"""
import functools
class Solution:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        @functools.lru_cache(None)
        def play(i=0):
            if i >= n:
                return 0

            return max(
                arr[i] - play(i+1),
                sum(arr[i:i+2]) - play(i+2),
                sum(arr[i:i+3]) - play(i+3)
            )

        n = len(arr)
        s = play()

        if s > 0:
            return "Alice"
        if s < 0:
            return "Bob"

        return "Tie"

"""
Solution1b: same but avoid array slicing.

Runtime: 2752 ms, faster than 90.04% of Python3 online submissions
Memory Usage: 220.8 MB, less than 100.00% of Python3 online submissions
"""
import functools
class Solution1b:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        @functools.lru_cache(None)
        def play(i=0):
            if i >= n:
                return 0

            if i < n - 2:
                return max(
                    arr[i] - play(i+1),
                    arr[i] + arr[i+1] - play(i+2),
                    arr[i] + arr[i+1] + arr[i+2] - play(i+3)
                )

            elif i == n - 2:
                return max(
                    arr[-2] - arr[-1],
                    arr[-2] + arr[-1]
                )

            elif i == n - 1:
                return arr[-1]

        n = len(arr)
        s = play()

        if s > 0:
            return "Alice"
        if s < 0:
            return "Bob"

        return "Tie"

"""
Solution 1c: memoized recursion using suffix sums.

play(i) = how many total stones the current player can get starting from now 
to the end of the game if he has to choose starting from pile i.
(ie, pretend the game starts now at pile i).

"""
import functools
class Solution1c:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        @functools.lru_cache(None)
        def play(i=0):
            if i >= n:
                return 0

            # return max(
            #     sums[i] - play(i+1),
            #     sums[i] - play(i+2),
            #     sums[i] - play(i+3)
            # )
            return sums[i] - min(
                play(i+1),
                play(i+2),
                play(i+3)
            )

        n = len(arr)
        sums = [0] * (n+1) # suffix sums

        for i in range(n-1, -1, -1):
            sums[i] = sums[i+1] + arr[i]

        s = play()

        # dp[0] = number of stones Alice has
        # sums[0] = total number of stones
        if s * 2 > sums[0]: # Alice has more than half the stones
            return "Alice"
        if s * 2 < sums[0]:
            return "Bob"

        return "Tie"

###############################################################################
"""
Solution 2: tabulation using 1d table.

Runtime: 2340 ms, faster than 94.67% of Python3 online submissions
Memory Usage: 17.5 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        n = len(arr)
        neg_inf = float('-inf')
        dp = [neg_inf] * (n+1)

        dp[n] = 0 # dummy value
        dp[n-1] = arr[-1]
        if n > 1:
            dp[n-2] = max(arr[-2] - arr[-1], arr[-2] + arr[-1])

        for i in range(n-1, -1, -1):
            dp[i] = max(
                arr[i] - dp[i+1],
                sum(arr[i:i+2]) - dp[i+2],
                sum(arr[i:i+3]) - dp[i+3]
            )

        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"

        return "Tie"

"""
Solution 2b: same, but use inner loop.

Based on:
https://leetcode.com/problems/stone-game-iii/discuss/564260/JavaC%2B%2BPython-DP-O(1)-Space

O(n) time
O(n) extra space
"""
class Solution2b:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        n = len(arr)
        neg_inf = float('-inf')
        dp = [neg_inf] * n + [0]

        for i in range(n-1, -1, -1):
            take = 0

            ### Want k < 3 and 
            ### k < end = n - i is same as i + k < n
            # end = min(3, n - i)

            # for k in range(end): 
            #     take += arr[i+k]
            #     dp[i] = max(dp[i], take - dp[i+k+1])

            ###
            # i + k < i + 3 and i + k < n
            end = min(i+3, n)

            for k in range(i, end):
                take += arr[k]
                dp[i] = max(dp[i], take - dp[k+1])


        if dp[0] > 0:
            return "Alice"
        if dp[0] < 0:
            return "Bob"

        return "Tie"

"""
Solution 3c: use suffix sums.

Con: the sums can become very big (pos or neg).

dp[i] = how many total stones the current player can get starting from now 
to the end of the game if he has to choose starting from pile i.
(ie, pretend the game starts now at pile i).

Based on:
https://leetcode.com/problems/stone-game-iii/discuss/564342/JavaC%2B%2BPython-Dynamic-Programming

O(n) time
O(n) extra space
"""
class Solution3c:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        n = len(arr)
        neg_inf = float('-inf')
        dp = [neg_inf] * n + [0]
        sums = [0] * (n+1) # suffix sums

        for i in range(n-1, -1, -1):
            sums[i] = sums[i+1] + arr[i]

        for i in range(n-1, -1, -1):
            end = min(i+3, n)

            for k in range(i, end):
                dp[i] = max(dp[i], sums[i] - dp[k+1])
                #dp[i] = max(dp[i], (sums[i] - sums[k+1]) - (dp[k+1] - sums[k+1]))

        # dp[0] = number of stones Alice has
        # sums[0] = total number of stones
        if dp[0] * 2 > sums[0]: # Alice has more than half the stones
            return "Alice"
        if dp[0] * 2 < sums[0]:
            return "Bob"

        return "Tie"

###############################################################################
"""
Solution 3: tabulation using O(1) space.

To calculate dp[i], only need dp[i+1], dp[i+2], and dp[i+3].
Use 4 dp variables for readibility, although can be reduced to 3.

O(n) time
O(1) extra space

"""
class Solution3:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        n = len(arr)

        if n == 1:
            dp = arr[0]
        else:
            dp3 = 0 # dummy value
            dp2 = arr[-1]
            dp1 = max(arr[-2] - arr[-1], arr[-2] + arr[-1])

            for i in range(n-3, -1, -1):
                dp = max(
                    arr[i] - dp1,
                    sum(arr[i:i+2]) - dp2,
                    sum(arr[i:i+3]) - dp3
                )

                dp1, dp2, dp3 = dp, dp1, dp2

        if dp > 0:
            return "Alice"
        if dp < 0:
            return "Bob"

        return "Tie"

"""
Solution 3b: same, but use dp array of length 3.
"""
class Solution3b:
    #def stoneGameIII(self, stoneValue: List[int]) -> str:
    def stoneGameIII(self, arr: List[int]) -> str:
        n = len(arr)
        dp = [0] * 3

        for i in range(n-1, -1, -1):
            dp[i % 3] = max(sum(arr[i:i+k]) - dp[(i+k) % 3] for k in (1,2,3) )

        def cmp(a,b): return (a>b)-(a<b) 
        return ["Tie", "Alice", "Bob"][cmp(dp[0], 0)]

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.stoneGameIII(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # memo
    sol = Solution1b() # same, but avoid array slicing
    
    sol = Solution2() # tabulation using 1d table
    sol = Solution2b() # same but use inner loop

    sol = Solution3() # tabulation using O(1) space
    sol = Solution3b() # same, but use dp array of length 3

    comment = "LC ex1; answer = Bob"
    arr = [1,2,3,7]
    test(arr, comment)

    comment = "LC ex2; answer = Alice"
    arr = [1,2,3,-9]
    test(arr, comment)

    comment = "LC ex3; answer = Tie"
    arr = [1,2,3,6]
    test(arr, comment)

    comment = "LC ex4; answer = Alice"
    arr = [1,2,3,-1,-2,-3,7]
    test(arr, comment)

    comment = "LC ex5; answer = Tie"
    arr = [-1,-2,-3]
    test(arr, comment)

    comment = "LC TC; answer = Bob"
    arr = [-2]
    test(arr, comment)

    comment = "LC TC; answer = Alice"
    arr = [1,-2,3,-4,5,-6,7]
    test(arr, comment)

    comment = "LC TC; answer = Alice"
    arr = [6,-9,11,6,9,-3,-17,-10,15,-14,-10,9,3,4,-4,17,2,3,-9,-16,17,2,5]
    test(arr, comment)

    comment = "LC TC; answer = Alice" # TC's solution w/o memoization
    arr = [7,-17,3,-14,6,3,12,-7,-7,0,0,-17,-11,7,-8,-6,13,-5,-8,6,-11,2,8]
    test(arr, comment)
