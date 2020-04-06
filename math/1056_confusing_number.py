"""
1056. Confusing Number
Easy

Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

Example 1:

Input: 6
Output: true
Explanation: 
We get 9 after rotating 6, 9 is a valid number and 9!=6.

Example 2:

Input: 89
Output: true
Explanation: 
We get 68 after rotating 89, 86 is a valid number and 86!=89.

Example 3:

Input: 11
Output: false
Explanation: 
We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.

Example 4:

Input: 25
Output: false
Explanation: 
We get an invalid number after rotating 25.
 
Note:

0 <= N <= 10^9
After the rotation we can ignore leading zeros, for example if after rotation we have 0008 then this number is considered as just 8.
"""

###############################################################################
"""
"""
class Solution:
    def confusingNumber(self, n: int) -> bool:
        n2 = 0 # the resulting integer when n is flipped

        d = {'0': 0, '1': 1, '6': 9, '8': 8, '9': 6}

        s = str(n)
        if any(ch not in d for ch in s):
            return False

        # We process the last (right-most) digit in n first.
        # It ends up as the first digit in n2, but flipped.
        for ch in reversed(s):
            n2 = n2 * 10 + d[ch]

        #print(f"n2 = {n2}")

        return n2 != n

"""
"""
class Solution1b:
    def confusingNumber(self, n: int) -> bool:
        n2 = 0 # the resulting integer when n is flipped

        d = {'0': 0, '1': 1, '6': 9, '8': 8, '9': 6}

        # We process the last (right-most) digit in n first.
        # It ends up as the first digit in n2, but flipped.
        for ch in reversed(str(n)):
            if ch not in d:
                return False

            n2 = n2 * 10 + d[ch]

        #print(f"n2 = {n2}")

        return n2 != n

###############################################################################
"""
Solution 2: same idea, but build flipped integer as string.
"""
class Solution2:
    def confusingNumber(self, n: int) -> bool:
        s = "" # the resulting integer (as a string) when n is flipped

        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        # We process the last (right-most) digit in n first.
        # It ends up as the first digit in n2, but flipped.
        for ch in reversed(str(n)):
            if ch not in d:
                return False

            s += d[ch]

        return s != str(n)

###############################################################################
"""
Solution 3: same idea, but build flipped integer as list of 1-char strings.
"""
class Solution3:
    def confusingNumber(self, n: int) -> bool:
        s = [] # the resulting integer (as list of 1-char strings) when n is flipped

        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        # We process the last (right-most) digit in n first.
        # It ends up as the first digit in n2, but flipped.
        for ch in reversed(str(n)):
            if ch not in d:
                return False

            s += [d[ch]]

        return ''.join(s) != str(n)

###############################################################################
"""
Solution 4: use 2 pointers, and use flag to indicate when a flipped digit
is not equal to the digit in the corresponding position in the original int.
"""
class Solution4:
    def confusingNumber(self, n: int) -> bool:
        s = str(n)
        i = 0
        j = len(s) - 1

        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        flag = False

        while i <= j:
            if (s[i] not in d) or (s[j] not in d):
                return False

            if d[s[i]] != s[j] or d[s[j]] != s[i]:
                flag = True

            i += 1
            j -= 1

        return flag

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"n = {n}")

        res = sol.confusingNumber(n)
        
        print(f"\nres = {res}\n")


    sol = Solution() # build as integer
    sol = Solution1b() 

    sol = Solution2() # same idea, but build as string
    sol = Solution3() # same idea, but build as list of 1-char strings

    sol = Solution4() # use 2 ptrs and flag

    comment = "LC ex1; answer = True"
    n = 6
    test(n, comment)

    comment = "LC ex2; answer = True"
    n = 89
    test(n, comment)

    comment = "LC ex3; answer = False"
    n = 11
    test(n, comment)

    comment = "LC TC; answer = False"
    n = 916
    test(n, comment)
