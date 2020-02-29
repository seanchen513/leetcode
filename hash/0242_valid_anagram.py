"""
242. Valid Anagram
Easy

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

import collections

###############################################################################
"""
Solution 1: use dict to count chars.

Hash table can adapt to any range of chars (eg, if use Unicode), and would
be more efficient than using a fixed-size array for counting.

O(n) time
O(1) extra space since fixed number of chars
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d = collections.defaultdict(int)

        for ch in s:
            d[ch] += 1

        for ch in t:
            d[ch] -= 1

        return all(d[ch] == 0 for ch in d)

"""
Solution 1b: use collections.Counter(), which subclasses dict.
"""
class Solution1b:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return collections.Counter(s) == collections.Counter(t)

###############################################################################
"""
Solution 2: use sorting.

O(n log n) time
O(1) extra space if sort in-place, else O(n)
"""
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

###############################################################################

if __name__ == "__main__":
    def test(s, t, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        print(f"t = {t}")
        
        res = sol.isAnagram(s, t)

        print(f"\nres = {res}\n")
        

    sol = Solution() # use dict
    sol = Solution1b() # use collections.Counter()
    #sol = Solution2() # use sorting

    comment = "LC ex1; answer = True"
    s = "anagram"
    t = "nagaram"
    test(s, t, comment)

    comment = "LC ex2; answer = False"
    s = "rat"
    t = "car"
    test(s, t, comment)
