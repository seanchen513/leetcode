"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false

Constraints:

-2^31 <= x <= 2^31 - 1
 
Follow up: Could you solve it without converting the integer to a string?
"""

###############################################################################
"""
Solution 1: build up the integer in reverse, then compare

O(log n) time, where n is the given integer
O(1) extra space
"""      
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        y = x # copy of x to work with, so can preserve x to compare with at end
        z = 0 # build up to be palindrome of x

        while y > 0:
            z = z * 10 + y % 10
            y //= 10
            
        return z == x

###############################################################################
"""
Solution 2: convert int to string, then compare string to its reversal

O(n) time
O(n) extra space: for string and its reversal

"""      
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        
        return s == s[::-1]
        #return s == "".join(reversed(s)) # also works
        #return s == str(reversed(s)) # does NOT work for strings       

###############################################################################
"""
Solution 3: convert int to string, then use two pointers to compare
characters in string

O(n) time
O(n) extra space: for string
"""      
class Solution3:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        s = str(x)
        #s = f"{x}"
        #s = "{}".format(x)
        
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
            
        return True

###############################################################################

if __name__ == "__main__":
    def test(x, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"x = {x}")

        res = sol.isPalindrome(x)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution2()
    #sol = Solution3()

    comment = "LC example 1; answer = True"
    x = 121
    test(x, comment)

    comment = "LC example 2; answer = False"
    x = -121
    test(x, comment)

    comment = "LC example 3; answer = False"
    x = 10
    test(x, comment)

    comment = "LC example 4; answer = False"
    x = -101
    test(x, comment)
