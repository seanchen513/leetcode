"""
186. Reverse Words in a String II
Medium

Given an input string , reverse the string word by word. 

Example:

Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?
"""

from typing import List

###############################################################################
"""
Solution: reverse list of letters, and reverse each word.

O(n) time
O(1) extra space: in-place, no extra space used.
"""
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        n = len(s)
        i = 0

        while i < n:
            start = i
            while i < n and s[i] != ' ':
                i += 1

            rev(start, i-1)

            i += 1 # Skip over space

        rev(0, n-1)

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\narray of letters = {arr}")

        sol.reverseWords(arr)

        print(f"\nAfter: = {arr}\n")


    sol = Solution()

    comment = "LC example"
    arr = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    test(arr, comment)
