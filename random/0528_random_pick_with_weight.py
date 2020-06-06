"""
528. Random Pick with Weight
Medium

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

from typing import List
import random
import bisect

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

###############################################################################
"""
Solution: initialize by calculating and storing prefix sums from given
weights. To pick index, generate random int from 0 to total sum - 1, inclusive,
and bisect_right() the sums array, searching for the generated random int.

Alternatively, generate random int from 1 to total sum, inclusive,
and bisect_left() the sums array, searching for the generated random int.

Example:
w = 3, 14, 1, 7
sums = 3, 17, 18, 25 # prefix (cumulative) sums
Let s = 25 be the total sum.

Generate random int from 0 to 24 = s - 1.

i   randint     cs value
0   0..2        3
1   3..16       17
2   17          18
3   18..24      25

so we want to use bisect.bisect(), aka, bisect.bisect_right().

Alternatively, generate random int from 1 to 25 = s
and use bisect.bisect_left().

Alternatively, generate a random floating number from 0 to s.
This works for both bisect_left() and bisect_right().
This is because there is a negligible chance that the random float will be
exactly any of the prefix sums, so both bisect_left() and bisect_right()
will "never" find the random float within the prefix sums array; in such
cases, both bisect functions return the index of the first prefix sum
greater than the target.

###

Initialize: O(n) time, O(n) space.
pickIndex(): O(log n) time for binary search, O(1) space.

"""
class Solution:
    def __init__(self, w: List[int]):
        self.sums = []
        s = 0
        
        for wt in w:
            s += wt
            self.sums.append(s)

    def pickIndex(self) -> int:
        r = random.random() * self.sums[-1] # for either...
        r = random.randint(0, self.sums[-1] - 1) # for bisect_right()
        # r = random.randint(1, self.sums[-1]) # for bisect_left()
        
        return bisect.bisect(self.sums, r) # aka, bisect_right()
        # return bisect.bisect_left(self.sums, r)
               
###############################################################################       
"""
Solution 2: same, but write the binary search routine manually.
"""
class Solution2:
    def __init__(self, w: List[int]):
        self.sums = []
        s = 0
        
        for wt in w:
            s += wt
            self.sums.append(s)
            
    def pickIndex(self) -> int:
        r = random.random() * self.sums[-1] # for either...
        #r = random.randint(0, self.sums[-1] - 1) # for bisect_right()
        #r = random.randint(1, self.sums[-1]) # for bisect_left()
        
        lo = 0
        hi = len(self.sums) 
        # Not subtracting 1 from hi is standard, but in this problem,
        # we can subtract 1 without issue. This is because the target "r"
        # is always found with the bounds of the sums array.
        # ie, we never have r > max of sums array.
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            #if self.sums[mid] <= r: # for bisect_right() w/ r in [0, s-1]
            if self.sums[mid] < r: # for bisect_left() w/ r in [1, s]
                lo = mid + 1
            else:
                hi = mid

        return lo 
