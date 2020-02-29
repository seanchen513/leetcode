"""
131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

from typing import List

###############################################################################
"""
Solution 1: backtracking.  Pass substrings and partition copies.
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def rec(p, t):
            """
            p = partition so far (list of substrings)
            t = remaining substring to check
            """
            if not t:
                res.append(p) # partition done, so add to results
                return

            # Next char t[0] is always a palindrome.
            # This can be made part of loop, but this way saves some work.
            rec(p + [t[0]], t[1:])
            
            # Look at substrings t2 of t with same starting index.
            for end in range(1, len(t)):
                if t[0] == t[end]:
                    t2 = t[:end+1]
                    
                    if t2 == t2[::-1]: # substring is palindrome
                        # Add substring to partition and check rest of string.
                        rec(p + [t2], t[end+1:]) 

        res = [] # list of partitions
        rec([], s)

        return res

"""
Solution 1b: same as sol 1, but only make copy of partition when adding it
to results list.  This makes the backtracking more obvious.  We are always
working on the same object "p", so no need to have it as a fn parameter.
"""
class Solution1b:
    def partition(self, s: str) -> List[List[str]]:
        def rec(t):
            """
            p = partition so far (list of substrings)
            t = remaining substring to check
            """
            if not t:
                res.append(p[:]) # partition done, so add to results
                return

            # Next char t[0] is always a palindrome.
            # This can be made part of loop, but this way saves some work.
            p.append(t[0])
            rec(t[1:])
            p.pop()

            # Look at substrings t2 of t with same starting index.
            for end in range(1, len(t)):
                if t[0] == t[end]:
                    t2 = t[:end+1]
                    
                    if t2 == t2[::-1]: # substring is palindrome
                        # Add substring to partition and check rest of string.
                        p.append(t2)
                        rec(t[end+1:]) 
                        p.pop()

        p = [] # partition; list of substrings that partition given string s
        res = [] # list of partitions
        rec(s)

        return res

###############################################################################
"""
Solution 2: same as sol 1, but pass string indices instead of substrings.
Also, make copy of partition only when adding it to results list
(this makes the backtracking more obvious).

Runtime: 56 ms, faster than 98.10% of Python3 online submissions
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        def rec(start=0):
            """
            p = partition so far (list of substrings)
            start = start index of remaining substring to check
            """
            if start == n:
                res.append(p[:]) # partition finished, so add to results
                return

            # Next char t[0] is always a palindrome.
            # This can be made part of loop, but this way saves some work.
            p.append(s[start])
            rec(start + 1)
            p.pop()

            # Look at substrings t2 with same starting index
            for end in range(start+1, n):
                if s[start] == s[end]:
                    t2 = s[start:end+1]
                    
                    if t2 == t2[::-1]: # substring is palindrome
                        # Add substring to partition and check rest of string.
                        p.append(t2)
                        rec(end + 1)
                        p.pop()

        p = [] # partition; list of substrings that partition given string s
        res = [] # list of partitions
        n = len(s)
        rec()

        return res

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        
        res = sol.partition(s)

        print(f"\nres = {res}\n")
        

    sol = Solution() # backtracking, pass partitons and substrings
    sol = Solution1b() # same, but make copy of partition only when adding to results list
    
    #sol = Solution2() # pass string indices

    comment = "LC ex1"
    s = "aab"
    test(s, comment)

    comment = "LC test case"
    s = "bb"
    test(s, comment)
