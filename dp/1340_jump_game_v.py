"""
1340. Jump Game V
Hard

Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.

Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.

Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies. 

Example 4:

Input: arr = [7,1,7,1,7,1], d = 2
Output: 2

Example 5:

Input: arr = [66], d = 1
Output: 1
 
Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length
"""

from typing import List

###############################################################################
"""
Solution 1: tabulation using max_visits array.

Build up a solution by finding max_visits for indices with the
smallest values first.
"""
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # "visits" records the max number of other indices that can be visited
        # from each index.
        n = len(arr)
        visits = [1]*n
        
        # Create sorted list of tuples (val, index) from array.
        # This way, we will be able to loop through indices with smaller values
        # first.
        values = [(val, i) for i, val in enumerate(arr)]
        values.sort()
        
        min_val = values[0][0]
         
        for val, index in values:
            if val == min_val:
                continue

            # bounds for how far the current index can visit
            left = max(0, index - d)
            right = min(n - 1, index + d)

            max_so_far = 1

            i = index + 1
            while i <= right and val > arr[i]:
                max_so_far = max(max_so_far, 1 + visits[i])
                i += 1

            i = index - 1
            while i >= left and val > arr[i]:
                max_so_far = max(max_so_far, 1 + visits[i])
                i -= 1

            visits[index] = max_so_far

        return max(visits)

###############################################################################
"""
Solution 2: recursion

LC TLE
"""
class Solution2:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def visits(index):
            if index < 0 or index > end:
                return 0

            max_so_far = 1

            val = arr[index]
            left = max(0, index - d)
            right = min(end, index + d)

            i = index + 1
            while i <= right and arr[i] < val:
                max_so_far = max(max_so_far, 1 + visits(i))
                i += 1

            i = index - 1
            while i >= left and arr[i] < val:
                max_so_far = max(max_so_far, 1 + visits(i))
                i -= 1

            return max_so_far
            
        max_overall = 1
        end = len(arr) - 1

        for i in range(end+1):
            max_overall = max(max_overall, visits(i))

        return max_overall
        
###############################################################################
"""
Solution 3: memoization
"""
class Solution3:
    def maxJumps(self, arr: List[int], d: int) -> int:
        def num_visits(index):
            nonlocal max_visits

            if max_visits[index] != 0:
                return max_visits[index]

            if index < 0 or index >= n:
                return 0

            max_so_far = 1

            val = arr[index]
            left = max(0, index - d)
            right = min(n - 1, index + d)

            i = index + 1
            while i <= right and arr[i] < val:
                max_so_far = max(max_so_far, 1 + num_visits(i))
                i += 1

            i = index - 1
            while i >= left and arr[i] < val:
                max_so_far = max(max_so_far, 1 + num_visits(i))
                i -= 1

            max_visits[index] = max_so_far

            return max_so_far
            
        n = len(arr)
        max_visits = [0]*n # memoization; 0 signifies not calculated yet
        
        #max_overall = 1
        # for i in range(n):
        #     max_overall = max(max_overall, num_visits(i))

        # return max_overall

        return max(map(num_visits, range(n)))

###############################################################################

if __name__ == "__main__":
    def test(arr, d, comment=None):
        max_jumps = s.maxJumps(arr, d)
        
        print("="*80)
        if comment:
            print(comment)
            
        print(f"\n{arr}")
        print(f"d = {d}")
        print(f"\nmax jumps = {max_jumps}")


    #s = Solution() # tabulation
    #s = Solution2() # recursion
    s = Solution3() # memoization

    # comment = "LC ex1; answer = 4"
    # arr = [6,4,14,6,8,13,9,7,10,6,12]
    # d = 2
    # test(arr, d, comment)

    # comment = "LC ex2; answer = 1"
    # arr = [3,3,3,3,3]
    # d = 3 
    # test(arr, d, comment)

    # comment = "LC ex3; answer = 7"
    # arr = [7,6,5,4,3,2,1]
    # d = 1
    # test(arr, d, comment)

    # comment = "LC ex4; answer = 2"
    # arr = [7,1,7,1,7,1]
    # d = 2
    # test(arr, d, comment)

    # comment = "LC ex5; answer = 1"
    # arr = [66]
    # d = 1
    # test(arr, d, comment)

    comment = "LC test case; TLE's basic recursion; answer = 13"
    arr = [82,40,59,75,78,69,38,50,12,86,70,57,61,89,39,18,29,64,92,57,2,93,69,63,50,77,93,19,74,21,40,83,54,91,97,32,45,64,22,47,71,26,60,3,92,81,44,71,71,83,100,10,49,69,53,30,42,6,1,69,5,6,57,39,66,51,6,61,48,96,42,94,61,35,88,89,95,23,16,6,96,93,6,16,84,94,16,13,79,60,37,8,30,29,93,53,59,56,92,53,50,29,66,91,85,61,25,69,25,27,93,64,85,25,72,49,97,28,50,59,47,33,2,11,21,63,85,41,97,57,7,61,18,41,63,83,48,3,29,68,23,39,96,53,98,20,29,73,47,54,52,65,48,17,60,80,49,25,90,53,71,73,92,68,36,29,16,78,21,52,76,86,3,64,86,10,22,33,63,87,1,25,80,53,75,69,45,94,14,33,21,94,67,39,63,28,23,95,74,95,57,41,41,12,2,28,80,59,99,99,4,85,88,73,46,37,98,48,53,22,37,29,24,14,86,89,59,68,98,98,33,41,97,99,91,65,97,39,42,48,46,70,15,71,77,95,36,54,74,22,32,34,12,48,41,7,18,70,17,36,62,35,19,32,43,11,85,39,37,30,78,93,86,22,44,56,28,56,9,31,96,74,87,40,48,74,74,63,67,42,41,54,59,87,78,8,71,27,68,1,26,33,37,69,18,96,45,55,77,25,16,95,10,44,19,61,38,46,91,63,45,4,18,4,90,54,48,14,11,46,94,69,75,74,78,22,31,56,10,29,92,84,55,1,55,77,47,25,59,93,96,30,41,27,19,59,30,88,43,79,71,16,96,87,26,96,89,6,48,59,26,52,17,73,96,99,33,84,56,7,72,25,95,24,5,42,97,18,70,43,14,26,78,46,54,59,66,29,10,11,92,15,42,28,36,78,49,99,79,26,56,66,100,52,65,74,46,29,70,19,72,83,37,11,100,27,14,21,27,63,23,67,50,45,4,95,43,83,86,57,45,60,90,84,64,51,3,45,23,67,63,40,94,95,59,73,24,30,35,51,40,95]
    d = 122
    test(arr, d, comment)
