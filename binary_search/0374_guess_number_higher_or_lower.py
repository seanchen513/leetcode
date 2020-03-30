"""
374. Guess Number Higher or Lower
Easy

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :

Input: n = 10, pick = 6
Output: 6
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

###############################################################################
"""
Solution: use binary search with "lo <= hi".
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            x = guess(mid)
            if x == -1:
                hi = mid - 1
            elif x == 1:
                lo = mid + 1
            else:
                return mid
    
        # this point never reached
        return -1
    
###############################################################################
"""
Solution 2: use binary search with "lo < hi". Just be careful to set
hi = mid if x == 0.
"""
class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            x = guess(mid)
            if x == 1:
                lo = mid + 1
            else:
                hi = mid

        return lo
