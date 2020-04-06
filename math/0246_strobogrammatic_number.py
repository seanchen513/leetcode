"""
246. Strobogrammatic Number
Easy

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true

Example 2:

Input:  "88"
Output: true

Example 3:

Input:  "962"
Output: false
"""

###############################################################################
"""
Solution:

Only valid digits and what they need to map to are:
0: 0
1: 1
6: 9
8: 8
9: 6

Suffices to iterate through half the string:

n = 1
indices: 0
check range(1)

n = 2
indices: 01
check range(1)

n = 4
indices: 0123
check range(2)

n = 5
indices: 01234
check range(3)

"""
class Solution:
    def isStrobogrammatic(self, s: str) -> bool:
        n = len(s)
        end = (n + 1) // 2

        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        if any(ch not in d for ch in s):
            return False

        for i in range(end):
            if s[i] != d[s[n-i-1]]:
                return False

        return True

###############################################################################
"""
Solution: same idea, but using 2 explicit pointers.
"""
class Solution2:
    def isStrobogrammatic(self, s: str) -> bool:
        n = len(s)

        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        i = 0
        j = len(s) - 1

        while i <= j:
            if (s[i] not in d) or (s[j] not in d):
                return False

            if s[i] != d[s[j]]:
                return False

            i += 1
            j -= 1

        return True

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(s)

        res = sol.isStrobogrammatic(s)
        
        print(f"\nres = {res}\n")


    sol = Solution() 
    sol = Solution2() # same idea, but use 2 explicit ptrs

    comment = "LC ex1; answer = True"
    s = "69"
    test(s, comment)

    comment = "LC ex2; answer = True"
    s = "88"
    test(s, comment)

    comment = "LC ex3; answer = False"
    s = "962"
    test(s, comment)
