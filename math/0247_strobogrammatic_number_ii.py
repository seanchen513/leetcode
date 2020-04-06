"""
247. Strobogrammatic Number II
Medium

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
"""

from typing import List

###############################################################################
"""
Solution: build all strobogrammatic numbers of length n iteratively.
Build prefixes and suffixes for each number.

Note: "00" is not a valid length 2 strobogrammatic number. 
The integer 0 corresponds to "0", which has length 1.
In general, the first char in a strobogrammatic number cannot be "0".

Range of indices to process:

n = 1
indices: 0

n = 2
indices: 0 1
range(1)

n = 3
indices: 0 1 2
range(1)

n = 4
indices: 01 23
range(2)

n = 5
indices: 01 2 34
range(2)

"""
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        res = [('', '')] # tuples of prefix and suffix for each number

        for i in range(n//2):
            new_res = []

            for ch in d:
                if i == 0 and ch == '0': # don't use '0' as first digit
                    continue

                for s1, s2 in res:
                    new_res.append((s1 + ch, d[ch] + s2))
    
            res = new_res

        if n % 2 == 1:
            return [s1 + ch + s2 for s1, s2 in res for ch in ['0','1','8']]

        return [s1 + s2 for s1, s2 in res]

"""
Solution 1b: same idea, but written differently.

Update "res" using list comprehensions, and avoid using temp list "new_res".
"""
class Solution1b:
    def findStrobogrammatic(self, n: int) -> List[str]:
        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        res = [('', '')] # tuples of prefix and suffix for each number

        for i in range(n//2):
            if i == 0: # don't use '0' as first digit
                res = [(s1 + ch, d[ch] + s2) for s1, s2 in res 
                    for ch in ('1','6','8','9')]
            else:
                res = [(s1 + ch, d[ch] + s2) for s1, s2 in res for ch in d]
 
        if n % 2 == 1:
            return [s1 + ch + s2 for s1, s2 in res for ch in ['0','1','8']]

        return [s1 + s2 for s1, s2 in res]

###############################################################################
"""
Solution 2: build iteratively, from middle of each number to both ends.
"""
class Solution2:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = ['0', '1', '8'] if (n % 2 == 1) else ['']
        
        if n < 2:
            return res

        while len(res[0]) < n:
            new_res = []

            for s in res:
                if len(s) < n - 2: # don't use '0' on last iteration
                    new_res.append('0' + s + '0')

                new_res.append('1' + s + '1')
                new_res.append('6' + s + '9')
                new_res.append('8' + s + '8')
                new_res.append('9' + s + '6')

            res = new_res

        return res

"""
Solution 2b: same as sol 1b, but with some optimizations.
"""
class Solution2b:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = ['0', '1', '8'] if n & 1 else ['']
        
        if n < 2:
            return res

        k = len(res[0])
        
        while k < n:
            new_res = []
            k += 2 # length of new strings

            for s in res:
                if k < n: # don't use '0' on last iteration
                    new_res.extend(['0'+s+'0', 
                        '1'+s+'1', '6'+s+'9', '8'+s+'8', '9'+s+'6'])
                else:
                    new_res.extend(['1'+s+'1', '6'+s+'9', '8'+s+'8', '9'+s+'6'])

            res = new_res

        return res

"""
Solution 2c: same as sol 1c, but using a "for" loop.
"""
class Solution2c:
    def findStrobogrammatic(self, n: int) -> List[str]:
        res = ['0', '1', '8'] if n & 1 else ['']
        
        if n < 2:
            return res

        start = len(res[0]) + 2

        for k in range(start, n+1, 2): # length of new strings
            new_res = []

            for s in res:
                if k < n: # don't use '0' on last iteration
                    new_res.extend(['0'+s+'0', 
                        '1'+s+'1', '6'+s+'9', '8'+s+'8', '9'+s+'6'])
                else:
                    new_res.extend(['1'+s+'1', '6'+s+'9', '8'+s+'8', '9'+s+'6'])

            res = new_res

        return res

###############################################################################
"""
Solution 3: recursion
"""
class Solution3:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def rec(n):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']

            return [ch + s + d[ch] for ch in d for s in rec(n-2)]
        
        if n == 1:
            return ['0', '1', '8']

        d = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}        

        #return [s for s in rec(n) if s[0] != '0'] # alternative
        return [ch + s + d[ch] for ch in ['1','6','8','9'] for s in rec(n-2)]

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"n = {n}")

        res = sol.findStrobogrammatic(n)
        
        print(f"\nres = {res}")
        print(f"\nlen = {len(res)}\n")


    sol = Solution() # iterative
    sol = Solution1b() 
    
    sol = Solution2() # iterative, build from middle of each number
    sol = Solution2b()
    sol = Solution2c()

    #sol = Solution3() # recursive

    comment = 'LC ex; answer = ["11","69","88","96"]'
    n = 2
    test(n, comment)

    comment = ""
    n = 1
    test(n, comment)

    comment = ""
    n = 3
    test(n, comment)

    comment = ""
    n = 4
    test(n, comment)

    comment = ""
    n = 5
    test(n, comment)
