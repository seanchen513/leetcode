"""
1271. Hexspeak
Easy

A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.

Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

Example 1:

Input: num = "257"
Output: "IOI"
Explanation:  257 is 101 in hexadecimal.

Example 2:

Input: num = "3"
Output: "ERROR"

Constraints:

1 <= N <= 10^12
There are no leading zeros in the given string.
All answers must be in uppercase letters.
"""

###############################################################################
"""
Solution 1: use mod and integer division.
"""
class Solution:
    def toHexspeak(self, num: str) -> str:        
        n = int(num)
        res = []

        d = {0: "O", 1: "I",
            10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        
        while n:
            k = n % 16
            if k not in d:
                return "ERROR"
            
            res.append(d[k])
            
            n //= 16
            
        return ''.join(reversed(res))

###############################################################################
"""
Solution 2: use hex().
"""
class Solution2:
    def toHexspeak(self, num: str) -> str:        
        n = hex(int(num))[2:]
        res = []

        d = {"0": "O", "1": "I", "a": "A", "b": "B",
            "c": "C", "d": "D", "e": "E", "f": "F"}
        
        for ch in n:
            if ch not in d:
                return "ERROR"

            res.append(d[ch])

        return ''.join(res)
