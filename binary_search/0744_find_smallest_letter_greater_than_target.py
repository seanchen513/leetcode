"""
744. Find Smallest Letter Greater Than Target
Easy

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""

from typing import List

###############################################################################
"""
Solution: do bsearch_right with "lo < hi". After loop, if lo == len(arr),
then return arr[0], else return arr[lo].
"""
class Solution:
    #def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    def nextGreatestLetter(self, arr: List[str], target: str) -> str:
        lo = 0
        hi = len(arr)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if arr[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
                
        if lo == len(arr):
            return arr[0]
  
        return arr[lo]
