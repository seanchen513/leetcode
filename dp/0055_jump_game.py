"""
55. Jump Game
Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""

from typing import List

###############################################################################
"""
Solution: use greedy tactic of making the maximum possible jump, and
backing up as needed.

O(n) time...
O(1) extra space
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #n = len(nums)
        #if n <= 1:
        #    return True

        start = 0
        end = len(nums) - 1
        
        while start < end:
            x = nums[start]

            if start + x >= end: # x is big enough for us to jump to the end
                return True

            ### Checking cases x == 0 and x == 1 aren't necessary but
            ### might be useful.
            #if x == 0: # we were forced here and it's not the last element
            #    return False
            #if x == 1: # only one possible move
            #    start += 1
            #    continue

            start += x # try maximum possible jump

            # If we land at a 0 value, keep backing up one position at a
            # time until we're sure we we're not forced to end up at that
            # same zero again in however many steps.  
            # If this is not possible (start ends up < 0), then return False.

            zero_shifted = 0

            while start >= 0 and nums[start] <= zero_shifted:
                start -= 1
                zero_shifted += 1

            # algo won't work if this was "if start <= start_orig:"
            # where start_orig is value of start before "start += x"
            if start <= 0:
                return False

        return True
###############################################################################
"""
Solution 2: greedy algo.  This is related to the solution using tabulation,
where we also chose to check jumps starting from the furthest one.
Now, instead of just storing the result in the "good" set, we use the
first good index found.

O(n) time
O(1) extra space

https://leetcode.com/problems/jump-game/solution/
"""
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
            
        end = len(nums) - 1
        last_good_pos = end # "good" index

        for i in range(end-1, -1, -1):
            if i + nums[i] >= last_good_pos:
                last_good_pos = i # update "good" index

        return last_good_pos == 0

###############################################################################
"""
Solution 3: Recursion.  Try every possible jump.

O(2^n) time - proof: https://leetcode.com/problems/jump-game/solution/
O(n) space for recursion stack
"""
class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        def can_jump(pos): # can jump from this position to end
            if pos >= end:
                return True

            furthest = min(pos + nums[pos], end)

            #for i in range(pos + 1, furthest + 1): # check left to right
            for i in range(furthest, pos, -1): # check right to left
                if can_jump(i):
                    return True

            return False

        end = len(nums) - 1
        return can_jump(0)

###############################################################################
"""
Solution 4: Recursion w/ memoization.

O(n^2) time
O(n) extra space - for recursion and "good" memo cache.

LC TLE for [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
"""
class Solution4:
    def canJump(self, nums: List[int]) -> bool:
        def can_jump(pos): # can jump from this position to end
            if (pos in good) or (pos >= end):
                return True

            furthest = min(pos + nums[pos], end)

            #for i in range(pos + 1, furthest + 1): # check left to right
            for i in range(furthest, pos, -1): # check right to left
                if can_jump(i):
                    good.add(i)
                    return True

            return False

        end = len(nums) - 1

        # Cache for memoization.
        # Elements in set are array indices for which it's possible to jump
        # from to eventually reach the last index.
        good = set([end])
        
        return can_jump(0)

###############################################################################
"""
Solution 5: tabulation

O(n^2) time
O(n) extra space for "good" set

LC overall TLE
"""
class Solution5:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        
        end = len(nums) - 1
        good = set([end])

        for i in range(end-1, -1, -1):
            furthest = min(i + nums[i], end)

            #for j in range(i+1, furthest+1): # check left to right
            for j in range(furthest, i, -1): # check right to left
                if j in good:
                    good.add(i)
                    break
    
        return 0 in good

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        #solutions = [Solution(), Solution2(), Solution3(), Solution4(), 
        #    Solution5()]
        solutions = [Solution(), Solution2()] # just the greedy solutions

        res = [s.canJump(arr) for s in solutions]

        print("="*80)
        if comment:
            print(comment, "\n")
        print(arr)

        print(f"\nSolutions: {res}\n")


    comment = "LC ex1; answer = True"
    arr = [2,3,1,1,4]
    test(arr, comment)

    comment = "LC ex2; answer = False"
    arr = [3,2,1,0,4]
    test(arr, comment)

    comment = "LC test case; answer = True"
    arr = [2,0]
    test(arr, comment)

    comment = "LC test case; answer = True"
    arr = [2,0,0]
    test(arr, comment)

    comment = "LC test case; answer = True"
    arr = [1,1,2,2,0,1,1]
    test(arr, comment)

    comment = "LC test case; answer = True"
    arr = [1,1,1,0]
    test(arr, comment)

    comment = "LC test case; answer = True"
    arr = [5,9,3,2,1,0,2,3,3,1,0,0]
    test(arr, comment)

    comment = "LC test case; answer = True"
    arr = [2,5,0,0]
    test(arr, comment)

    comment = "LC test case; answer = False"
    arr = [2,0,0,0,2,0,0,0]
    test(arr, comment)
    
    comment = "LC test case; answer = True"
    arr = [3,0,8,2,0,0,1]
    test(arr, comment)

    comment = "LC test case; memoization TLE; answer = False"
    arr = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    test(arr, comment)

    comment = "Trivial case"
    arr = []
    test(arr, comment)

    comment = "Trivial case; answer = True"
    arr = [0]
    test(arr, comment)

    comment = "Trivial case; answer = True"
    arr = [1]
    test(arr, comment)
