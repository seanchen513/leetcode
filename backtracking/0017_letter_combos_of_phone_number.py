"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

from typing import List

###############################################################################
"""
Solution: iterative.

Runtime: 28 ms, faster than 67.82% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": " ",
        }

        if not digits: # eg, ""
            return []

        res = [""]
        
        for digit in digits:
            next_res = []

            for s in res:
                for ch in d[digit]:
                    next_res.append(s + ch)

            res = next_res

        return res
        
###############################################################################
"""
Solution 1b: same as sol #1, but rewritten to be more concise.
"""
class Solution1b:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
            "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "}

        res = [""] if digits else []

        for digit in digits:
            res = [s + ch for s in res for ch in d[digit]]

        return res

###############################################################################
"""
Solution: recursive.
"""
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        def rec(s="", index=0):
            if len(s) == n:
                res.append(s)
                return
            
            for ch in d[digits[index]]:
                rec(s + ch, index + 1)

        if not digits:
            return []

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", 
            "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "}

        n = len(digits)
        res = []

        rec()

        return res

###############################################################################

if __name__ == "__main__":
    def test(n_str, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(f"n = {n_str}")

        res = sol.letterCombinations(n_str)
        print(f"\nSolution: {res}\n")


    sol = Solution() # iterative
    sol = Solution1b() # more concise
    sol = Solution2() # recursive

    comment = "LC example"
    n_str = "23"
    test(n_str, comment)

    comment = "LC test case; answer = []"
    n_str = ""
    test(n_str, comment)
