"""
1363. Largest Multiple of Three
Hard

Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

Example 1:

Input: digits = [8,1,9]
Output: "981"

Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"

Example 3:

Input: digits = [1]
Output: ""

Example 4:

Input: digits = [0,0,0,0,0,0]
Output: "0"
 
Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros.
"""

from typing import List
import collections

###############################################################################
"""
Solution: math.

There are 5 cases.  Let s = sum(digits).
(1) s % 3 == 0.  No digits need to be removed.

(2,3) s % 3 == 1.  If there is a 1, 4, or 7, remove it.
Otherwise, there must be two digits from 2, 5, and 8 to remove (remove them
in this order, possibly duplicate digits).

(4,5) s % 3 == 2  If there is a 2, 5, or 8, remove it.
Otherwise, there must be two digits from 1, 4, and 7 to remove (remove them
in this order, possibly duplicate digits).

Note order of "if" statements, and order of function arguments within
return statements.

O(n) time: if use counting sort, otherwise O(n log n).
O(1) extra space

https://leetcode.com/problems/largest-multiple-of-three/discuss/517628/Python-Basic-Math

Runtime: 88 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # Try to remove digit i from digits.
        # Check for base cases (no digits left, or all 0s).
        # Check if we have answer.
        def f(i):
            nonlocal s

            if count[i]:
                digits.remove(i) # O(n)
                count[i] -= 1
                s -= i

            if not digits:
                return ""
            
            #if not any(digits):
            if digits[0] == 0:
                return "0"

            #if sum(digits) % 3 == 0:
            if s % 3 == 0:
                return "".join(map(str, digits)) # O(n)

        s = sum(digits) # O(n)
        if s == 0:
            return "0"

        #digits.sort(reverse=True)

        ### Use counting sort in reverse.
        count = collections.Counter(digits) # O(n)

        start = 0
        for d in range(9, -1, -1):
            cnt = count[d]
            if cnt != 0:
                digits[start:start+cnt] = [d]*cnt
                #for i in range(start, start+cnt):
                #    digits[i] = d
                
                start += cnt

        #print(f"count = {count}")
        #print(f"digits = {digits}")

        ###
        if s % 3 == 0:
            return f(-1) # -1 to not remove any digits

        # Try to remove one digit from 1, 4, 7
        #if s % 3 == 1 and count[1] + count[4] + count[7]:
        if s % 3 == 1 and (count[1] or count[4] or count[7]):
            return f(1) or f(4) or f(7)
        
        # Try to remove one digit from 2, 5, 8
        #if s % 3 == 2 and count[2] + count[5] + count[8]:
        if s % 3 == 2 and (count[2] or count[5] or count[8]):
            return f(2) or f(5) or f(8)

        # Try to remove two digits from 1, 4, 7
        if s % 3 == 2:
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)

        # Only remaining possibility is s % 3 == 1 and to
        # remove two digits from 2, 5, 8
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)

"""
Solution 1b: same as sol 1, but rewritten.
"""
class Solution1b:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        # Try to remove digit i from digits.
        # Check for base cases (no digits left, or all 0s).
        # Check if we have answer.
        def f(i):
            nonlocal s

            if count[i]:
                digits.remove(i)
                count[i] -= 1
                s -= i

            if not digits:
                return ""
            
            if digits[0] == 0:
                return "0"

            if s % 3 == 0:
                return "".join(map(str, digits))

        s = sum(digits)
        if s == 0:
            return "0"

        digits.sort(reverse=True)
        count = collections.Counter(digits)
        #print(f"### {digits}")

        if s % 3 == 0:
            return f(-1) # -1 to not remove any digits

        # Try to remove one digit from 1, 4, 7
        if s % 3 == 1:
            if count[1]: return f(1)
            if count[4]: return f(4)
            if count[7]: return f(7)

        # Try to remove one digit from 2, 5, 8
        if s % 3 == 2:
            if count[2]: return f(2)
            if count[5]: return f(5)
            if count[8]: return f(8)

            # Try to remove two digits from 1, 4, 7
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)

        # Only remaining possibility is s % 3 == 1 and to
        # remove two digits from 2, 5, 8
        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)

###############################################################################
"""
Solution 2: math, same idea as solution 1, but slower due to list processing.

Based on:
https://leetcode.com/problems/largest-multiple-of-three/discuss/517745/Elegant-Python-Solution

Runtime: 104 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        s = sum(digits)
        if s == 0:
            return "0"

        if s % 3 == 0:
            res = digits
        else:
            d1 = sorted([i for i in digits if i % 3 == 1]) # 1, 5, 8
            d2 = sorted([i for i in digits if i % 3 == 2]) # 2, 4, 7            
            res = [i for i in digits if i % 3 == 0] # 0, 3, 6, 9

            if s % 3 == 1:
                if len(d1) == 0: # need to remove two digits from 2, 4, 7
                    res += d2[2:]
                else: # need to remove one digit from 1, 5, 8
                    res += d1[1:] + d2

            else: # s % 3 == 2
                if len(d2) == 0: # need to remove two digits from 1, 5, 8
                    res += d1[2:]
                else: # need to remove one digit from 2, 4, 7
                    res += d1 + d2[1:]

        if not res:
            return ""

        res.sort(reverse=True)

        ### Alternative to checking s == 0.
        #return str(int("".join([str(i) for i in res])))

        return "".join(map(str, res))

###############################################################################
"""
Solution 3: use counting sort to help build up solution.

Based on:
https://leetcode.com/problems/largest-multiple-of-three/discuss/517704/Java-Basic-Multiple-of-3-Clean-code-O(N)-~-2ms
"""
import itertools
class Solution3:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        count = collections.Counter(digits) # O(n)

        count_r1 = count[1] + count[4] + count[7] # num elts w/ remainder 1
        count_r2 = count[2] + count[5] + count[8] # num elts w/ remainder 2

        rem = (count_r1 + 2 * count_r2) % 3 # same as sum(digits) % 3

        if rem == 1:
            if count_r1 >= 1: # delete smallest digit w/ remainder 1
                count_r1 -= 1
            else: # delete 2 smallest digits with remainder 2
                count_r2 -= 2

        elif rem == 2:
            if count_r2 >= 1: # delete smallest digit w/ remainder 2
                count_r2 -= 1
            else: # delete 2 smallest digits with remainder 1
                count_r1 -= 2
        
        start = 0
        for d in range(9, -1, -1):
            cnt = count[d]
            if d % 3 == 1:
                cnt = min(cnt, count_r1)    
                count_r1 -= cnt
            elif d % 3 == 2:
                cnt = min(cnt, count_r2)
                count_r2 -= cnt

            digits[start:start+cnt] = [d]*cnt
            start += cnt

        if digits[0] == 0:
            return "0"

        #return "".join(map(str, digits[:start]))
        return "".join(map(str, itertools.islice(digits, start)))

###############################################################################
"""
Solution 4: BFS.

LC: Memory Limit Exceeded
"""
class Solution4:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        s1 = sum(digits)
        if s1 == 0:
            return "0"

        digits = sorted(digits, reverse=True)
        #print(f"### {digits}")

        q = collections.deque( [(digits, s1)] )

        while q:            
            for i in range(len(q)):
                dig, s1 = q[i]

                if s1 % 3 == 0:
                    return ''.join(map(str, dig))

            n = len(q)
            for _ in range(n):
                dig, s1 = q.popleft()

                for i in range(len(dig)-1,-1,-1):

                    dig2 = dig[:i] + dig[i+1:]
                
                    #print(f"dig = {dig}")
                    q.append( [dig2, s1 - dig[i]] )

        return ""

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.largestMultipleOfThree(arr)

        print(f"\nres = {res}")


    sol = Solution() # math
    #sol = Solution1b() # same as sol 1, rewritten
    #sol = Solution2() # same idea, but use more list processing
    sol = Solution3() # use counting sort...
    #sol = Solution4() # BFS; LC: memory limit exceeded 

    comment = "LC ex1; answer = 981"
    arr = [8,1,9]
    test(arr, comment)

    comment = "LC ex2; answer = 8760"
    arr = [8,6,7,1,0]
    test(arr, comment)

    comment = "LC ex3; answer = (empty string)"
    arr = [1]
    test(arr, comment)

    comment = "LC ex4; answer = 0"
    arr = [0,0,0,0,0,0]
    test(arr, comment)
    
    comment = "LC test case; answer = 966"
    arr = [9,8,6,8,6]
    test(arr, comment)

    comment = "LC max digits length; answer = "
    #arr = [1]*10000 # LC max digits length
    #test(arr, comment)
    
    comment = "answer = 3"
    arr = [3]
    test(arr, comment)

    comment = "answer = 0"
    arr = [0]
    test(arr, comment)

    comment = "answer = (empty string)"
    arr = [2]
    test(arr, comment)

    comment = "all digits, each exactly once; answer = 9876543210"
    #arr = [0,1,2,3,4,5,6,7,8,9]
    arr = [8,6,7,1,0,9,2,3,4,5]
    test(arr, comment)
