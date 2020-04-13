"""
1025. Divisor Game
Easy

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < N and N % x == 0.
Replacing the number N on the chalkboard with N - x.
Also, if a player cannot make a move, they lose the game.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example 1:

Input: 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:

Input: 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 
Note:

1 <= N <= 1000
"""

###############################################################################
"""
Solution: minmax using recursion, memoized.

Player left with 1 loses.
Player to get to 1 wins.

2: win
3: lose, can only choose 1
4: win by choosing 1
5: lose, can only choose 1
6: win by choosing 1 or 3
7: lose, can only choose 1
8: win by choosing 1
9: lose, can only choose 1 or 3
10: win by choosing 1 or 5
11: lose, can only choose 1


"""
import functools
class Solution:
    def divisorGame(self, n: int) -> bool:
        @functools.lru_cache(None)
        def rec(n): # return value is whether current player can win
            if n == 1:
                return False # current player wins?

            end = n // 2 + 1 # largest possible proper divisor is n//2 when n even

            for i in range(1, end):
                if n % i == 0:
                    if not rec(n - i): # other player cannot win
                        return True # current player's goal is to win

            return False

        return rec(n)

"""
Solution 1b: same, but rewrite loop.
"""
import functools
class Solution1b:
    def divisorGame(self, n: int) -> bool:
        @functools.lru_cache(None)
        def rec(n): # return value is whether current player can win
            if n == 1:
                return False # current player wins?

            end = n // 2 + 1

            return any(not rec(n - i) for i in range(1, end) if n % i == 0)

        return rec(n)

###############################################################################
"""
Solution: first player can always win if n is even, and always loses if
n is odd.

If n even: can choose 1 or an even number less than n that divides n.
Choose 1. This gives the other place an odd number, and forces the other
player to return an even number. Eventually, this player gets 2, chooses 1,
and wins.

If n odd: all divisors are odd. No which which one is chosen, the other
play is left with an even number.
"""
class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
