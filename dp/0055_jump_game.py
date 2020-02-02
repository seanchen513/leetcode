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
Possible solution: Check backwards from last index.

TLE on LC test case [25000,24999,24998,24997,...]
"""
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        possible = [False]*n

        # it's always possible to reach the last index from the last index
        possible[n-1] = True 

        for i in range(n-2, -1, -1):
            x = nums[i] # current value, which is also max jump length

            end = min(i+x, n-1)
            possible[i] = any(possible[j] for j in range(i+1, end+1))

            # j = min(i+x, n-1)
            # while j >= i+1:
            #     if possible[j]:
            #         possible[i] = True
            #         break
            #     j -= 1

        return possible[0]          

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        solutions = [Solution(), Solution2()]

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

    comment = "Trivial case"
    arr = []
    test(arr, comment)

    comment = "Trivial case; answer = True"
    arr = [0]
    test(arr, comment)

    comment = "Trivial case; answer = True"
    arr = [1]
    test(arr, comment)
