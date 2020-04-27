"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""

from typing import List

###############################################################################
"""
Solution: go position by position (index i), comparing ith char of each string 
to ith char of 1st string. Return on 1st string that ends or on 1st mismatch.

O(n * min_len) time, where n = number of strings, and min_len = min length 
among all strings

O(min_len) extra space: for string copy s[:i]
"""
class Solution:
    #def longestCommonPrefix(self, strs: List[str]) -> str:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if not arr:
            return ""

        n = len(arr)
        s = arr[0]
        m = len(s)

        for i in range(m): # loop through positions; ith char
            ch = s[i]

            for j in range(1, n): # loop through strings in array; jth string
                
                # Case 1: found another string with length <= first string,
                # and that string has ended.
                # Case 2: found a character mismatch
                if i == len(arr[j]) or arr[j][i] != ch:
                    return s[:i]

        # s is the shortest string and no mismatch was found
        return s
  
"""
Solution 1b: same as sol 1, but find min length among all strings first.

O(nm), where n = number of strings, and m = min string length
O(m) extra space: for string copies s[:i] and s[:m]
"""        
class Solution1b:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if not arr:
            return ""

        s = arr[0]
        m = min(len(s) for s in arr) # min length among all strings

        for i in range(m): # loop through positions
            ch = s[i]
            if any(t[i] != ch for t in arr):
                return s[:i]

        return s[:m]

"""
Solution 1c: same as sol 1, but find string of min length first.
"""
class Solution1c:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if not arr:
            return ""

        s = min(arr, key=len) # shortest string

        for i, ch in enumerate(s):
            if any(t[i] != ch for t in arr):
                return s[:i]

        return s

###############################################################################
"""
Solution 2: use zip() and set().
"""
class Solution2:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        if not arr:
            return ""

        for i, letters_in_pos in enumerate(zip(*arr)):
            if len(set(letters_in_pos)) != 1:
                return arr[0][:i]

        return min(arr)

###############################################################################
"""
Solution 3: use os.path.commonprefix()
"""
import os
class Solution3:
    def longestCommonPrefix(self, arr: List[str]) -> str:
        return os.path.commonprefix(arr)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        
        res = sol.longestCommonPrefix(arr)

        print(f"\nres = {res}\n")
        

    sol = Solution() # brute force
    sol = Solution1b() # find min length among all strings first
    sol = Solution1c() # find string of min length first

    sol = Solution2() # use zip() and set()
    #sol = Solution3() # use os.path.commonprefix()

    comment = "LC ex1; answer = fl"
    arr = ["flower","flow","flight"]
    test(arr, comment)

    comment = "LC ex1; answer = (empty string)"
    arr = ["dog","racecar","car"]
    test(arr, comment)

    comment = "LC TC; answer = (empty string)"
    arr = []
    test(arr, comment)

    comment = "LC TC; answer = (empty string)"
    arr = [""]
    test(arr, comment)
    
    comment = "LC TC; answer = a"
    arr = ["a"]
    test(arr, comment)

    comment = "LC TC; answer = a"
    arr = ["aa", "a"]
    test(arr, comment)

    comment = "LC TC; answer = aa"
    arr = ["aacc","aa","aa","aa","aaca"]
    test(arr, comment)
