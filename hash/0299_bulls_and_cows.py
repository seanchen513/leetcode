"""
299. Bulls and Cows
Easy

You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""

import collections

###############################################################################
"""
Solution: use dicts to count digits in secret and guess. Keep track of how
many guesses are correct in value and position (bulls). Cows come from looking
at min of corresponding values in both dicts.

O(n) time
O(n) extra space: for dicts

Example:

         c b
secret = 1 1 23
guess  = 0 1 11
           b c

where b = bull and c = cow.

answer = "1A1B"

"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        a = 0 # count of guesses w/ correct digit and position

        d_secret = collections.defaultdict(int)
        d_guess = collections.defaultdict(int)

        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
            else:
                d_secret[secret[i]] += 1
                d_guess[guess[i]] += 1

        b = 0 # count of guesses w/ correct digit but incorrect position

        for digit, cnt in d_secret.items():
            if digit in d_guess:
                b += min(cnt, d_guess[digit])

        return f"{a}A{b}B"

"""
Solution: same idea, but use Counter() and & for Counter.
"""
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        # count of guesses w/ correct digit and position
        a = sum(d1 == d2 for d1, d2 in zip(secret, guess))

        d_secret = collections.Counter(secret)
        d_guess = collections.Counter(guess)
        d = d_secret & d_guess # intersection takes min of corresponding values

        # count of guesses w/ correct digit but incorrect position
        b = sum(d.values()) - a

        return f"{a}A{b}B"

            