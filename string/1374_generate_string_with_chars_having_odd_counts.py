"""
1374. Generate a String With Characters That Have Odd Counts
Easy

Given an integer n, return a string with n characters such that each character in such string occurs an odd number of times.

The returned string must contain only lowercase English letters. If there are multiples valid strings, return any of them.  

Example 1:

Input: n = 4
Output: "pppz"
Explanation: "pppz" is a valid string since the character 'p' occurs three times and the character 'z' occurs once. Note that there are many other valid strings such as "ohhh" and "love".

Example 2:

Input: n = 2
Output: "xy"
Explanation: "xy" is a valid string since the characters 'x' and 'y' occur once. Note that there are many other valid strings such as "ag" and "ur".

Example 3:

Input: n = 7
Output: "holasss"
 
Constraints:

1 <= n <= 500
"""

###############################################################################

class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 0:
            return ""
        
        if n % 2 == 1: # odd n
            return "a" * n
        
        # even n
        return "a" * (n-1) + "b"

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.generateTheString(n)

        print(f"\nres = {res}")


    sol = Solution()

    comment = "LC ex1"
    n = 4
    test(n, comment)

    comment = "LC ex2"
    n = 2
    test(n, comment)

    comment = "LC ex3"
    n = 7
    test(n, comment)
