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
Solution: Greedy algo using two pointers.

The pointers are for the current and previous farthest reachable index.
The jump counter is only incremented if the current index is equal to
the previous farthest reachable index, which implies a jump is required
to reach any more indices.

https://leetcode.com/problems/jump-game-ii/discuss/18035/Easy-Python-Greedy-solution-with-explanation

O(n) time
O(1) extra space
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curr_max_reach = 0
        prev_max_reach = 0

        end = len(nums) - 1

        for i in range(end):
            curr_max_reach = max(curr_max_reach, i + nums[i])

            if i == prev_max_reach: # jump is required to go further
                jumps += 1
                prev_max_reach = curr_max_reach

        return jumps


"""
Solution: Greedy ago using two pointers or an inclusive range.

The pointers are the left and right indices of the current reachable
range of indices.  Alternatively, we can think of this just as an
inclusive range of current reachable indices.

Initially, with no jumps made, the only reachable index is 0,
corresponding to an inclusive range [0, 0].

Inclusive range [l, r] contains the current reachable indices from the
previous jump.  If we jump again, the furthest reachable index is the 
max of i + nums[i] for i in inclusive range [l, r].

https://leetcode.com/problems/jump-game-ii/discuss/170518/8-Lines-in-Python!-Easiest-Solution!

O(n) time
O(1) extra space
"""
class Solution2:
    def jump(self, nums: List[int]) -> int:
        end = len(nums) - 1
        if end <= 0:
            return 0

        jumps = 0
        l = 0
        r = 0

        while r < end:
            jumps += 1
            next_r = max(i + nums[i] for i in range(l, r+1))
            l = r + 1 # since we can reach old "r" in one fewer jump
            r = next_r

        return jumps

###############################################################################
"""
Solution 3: recursion.  Try all possible paths.

LC TLE on [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
"""
class Solution3:
    def jump(self, nums: List[int]) -> int:
        def rec(i, count):
            nonlocal min_count
            
            if i == end:
                min_count = min(min_count, count)
                return

            end_index = min(i + nums[i], end)

            # Try all possible jumps from i to j = i+1, ..., end_index
            for j in range(i+1, end_index + 1):
                rec(j, count + 1)

        if not nums:
            return 0

        end = len(nums) - 1
        min_count = float('inf')
        
        rec(0, 0)
        return min_count


###############################################################################
"""
Solution 4: recursion w/ memoization.

LC TLE on [25000,24999,24998,24997,24996,...]
"""
class Solution4:
    def jump(self, nums: List[int]) -> int:
        def rec(i, count, min_count): # if is current start index
            nonlocal min_jumps_from

            if i in min_jumps_from:
                return count + min_jumps_from[i]

            if i == end:
                min_count = min(min_count, count)
                return min_count

            end_index = min(i + nums[i], end)
            
            # Try all possible jumps from i to j = i+1, ..., end_index
            for j in range(i+1, end_index + 1):
                min_count = min(min_count, rec(j, 1 + count, min_count))

            min_jumps_from[i] = min_count - count # min jumps *from i* to end

            return min_count

        if not nums:
            return 0

        end = len(nums) - 1
        min_jumps_from = {} # for memoization

        return rec(0, 0, float('inf'))

###############################################################################
"""
Solution 5: tabulation, building up jumps_to_end array.

TLE on [25000,24999,24998,24997,24996,...]
"""
class Solution5:
    def jump(self, nums: List[int]) -> bool:
        if not nums:
            return 0
        
        end = len(nums) - 1

        jumps_to_end = [float('inf')]*(end+1)
        jumps_to_end[end] = 0

        for i in range(end-1, -1, -1):
            if nums[i] == 0:
                #jumps_to_end[i] = float('inf')
                continue

            furthest = min(i + nums[i], end)
            if furthest == end:
                jumps_to_end[i] = 1
                continue

            #min_jumps = float('inf') 
            #for j in range(i+1, furthest+1): # check left to right
            #for j in range(furthest, i, -1): # check right to left
            #    if jumps_to_end[j] < min_jumps:
            #        min_jumps = jumps_to_end[j]

            min_jumps = min(jumps_to_end[j] for j in range(furthest, i, -1))

            jumps_to_end[i] = 1 + min_jumps

        return jumps_to_end[0]

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        #solutions = [Solution(), Solution2(), Solution3(), Solution4(), 
        #    Solution5()]
        solutions = [Solution(), Solution2()] # just the greedy also

        res = [s.jump(arr) for s in solutions]

        print("="*80)
        if comment:
            print(comment, "\n")
        print(arr)

        print(f"\nSolutions: {res}\n")


    comment = "LC ex1; answer = 2"
    arr = [2,3,1,1,4]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [2,0]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [2,0,0]
    test(arr, comment)

    comment = "LC test case; answer = 5"
    arr = [1,1,2,2,0,1,1]
    test(arr, comment)

    comment = "LC test case; answer = 3"
    arr = [1,1,1,0]
    test(arr, comment)

    comment = "LC test case; answer = 3"
    arr = [5,9, 3,2, 1,0, 2,3, 3,1, 0,0]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [2,5,0,0]
    test(arr, comment)
    
    comment = "LC test case; answer = 2"
    arr = [3,0,8,2,0,0,1]
    test(arr, comment)

    comment = "LC test case; TLE for simple recusion; answer = 5"
    arr = [5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5]
    test(arr, comment)
    
    comment = "Trivial case; answer = 0"
    arr = []
    test(arr, comment)

    comment = "Trivial case; answer = 0"
    arr = [0]
    test(arr, comment)

    comment = "Trivial case; answer = 0"
    arr = [1]
    test(arr, comment)
