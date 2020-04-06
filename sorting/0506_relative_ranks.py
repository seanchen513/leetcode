"""
506. Relative Ranks
Easy

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""

from typing import List

###############################################################################
"""
Solution: use dict(zip(s, rank)) that maps reverse-sorted values to ranks.

O(n log n) time: for sorting
O(n) extra space: for rank list, dict, and for not sorting in-place

Example:
nums = [8, 9, 2, 7, 6]
s    = [9, 8, 7, 6, 2]

list(zip(s, rank)) = [(9, 'Gold Medal), (8, 'Silver Medal), ...]
dict(zip(s, rank)) = {9: 'Gold Medal', 8: 'Silver Medal', ...}

"""
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        s = sorted(nums, reverse=True)

        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            [str(i) for i in range(4, len(nums) + 1)]
        
        d = dict(zip(s, rank))
        
        #return [d[i] for i in nums]
        return map(d.get, nums)

###############################################################################
"""
Solution 2:

Example:
0 1 2 3 4
8 9 2 7 6

sorted in reverse:
0 1 2 3 4 new index
1 0 3 4 2 old index
9 8 7 6 2

sort in reverse: (val, old index)

res[old index] = new index + 1

"""
class Solution2:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        s = [(val, i) for i, val in enumerate(nums)]
        s.sort(reverse=True)

        n = len(s)
        res = [""] * n

        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            [str(i) for i in range(4, n+1)]
        #     list(map(str, range(4, n+1)))

        for i in range(n):
            _, old_i = s[i]
            res[old_i] = rank[i]

        return res

###############################################################################
"""
Solution 3: use list that maps new indices to old indices. Create this list
by sorting old indices (0, 1, 2, ..., n-1) by key=lambda i: -nums[i].

Example:
0 1 2 3 4
8 9 2 7 6

sorted in reverse:
0 1 2 3 4 new index
1 0 3 4 2 old index
9 8 7 6 2

index = [0, 1, 2, 3, 4]

after sorting by lambda:
index = [1, 0, 3, 4, 2]

"""
class Solution3:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        n = len(nums)
        index = list(range(n))
        index.sort(key=lambda i: -nums[i])
        
        res = [""] * n

        rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + \
            [str(i) for i in range(4, n+1)]
        #     list(map(str, range(4, n+1)))

        for i in range(n):
            res[index[i]] = rank[i]

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")

        res = sol.findRelativeRanks(arr)
        
        print(f"\nres = {res}\n")


    sol = Solution() # use dict(zip(s, rank))
    sol = Solution2() # track old indices
    sol = Solution3() # use list that maps new indices to old indices

    comment = 'LC ex; answer = ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]'
    arr = [5, 4, 3, 2, 1]
    test(arr, comment)

    comment = "answer = ['Silver Medal', 'Gold Medal', '5', 'Bronze Medal', '4']"
    arr = [8,9,2,7,6]
    test(arr, comment)
