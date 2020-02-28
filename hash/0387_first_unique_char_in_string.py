"""
387. First Unique Character in a String
Easy

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

import collections

###############################################################################
"""
Solution 1: use dict; if same letter seen again, set d[ch] = float('inf')

O(n) time
O(1) extra space: since dict limited to 26 entries
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s == "":
            return -1

        d = {}
        n = float('inf') # or len(s)
        
        for i, ch in enumerate(s):
            if ch in d:
                d[ch] = n
            else:
                d[ch] = i
        
        min_index = min(d.values())
            
        return min_index if min_index < n else -1

###############################################################################
"""
Solution 2: use dict w/ seen set.

O(n) time
O(1) space

Runtime: 92 ms, faster than 83.60% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        seen = set()

        for i, ch in enumerate(s):
            if ch not in seen:
                d[ch] = i
                seen.add(ch)                
            elif ch in d:
                del d[ch]

        return min(d.values()) if d else -1

###############################################################################
"""
Solution 3: use dict mapping chars to list of indices

O(n) time
O(n) extra space: dict limited to 26 entries, but total of n values
"""
class Solution3:
    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(list)
        
        for i, ch in enumerate(s):
            d[ch] += [i]
            
        min_index = len(s)
        
        for indices in d.values():
            if len(indices) == 1 and indices[0] < min_index:
                min_index = indices[0]
                
        return min_index if min_index < len(s) else -1

###############################################################################
"""
Solution 4: use s.index()

https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86351/Python-3-lines-beats-100-(~-60ms)-!

Its only faster because s.index() is a C function that Python is calling. 
So you are changing the Python loop to be the 26 chars, and the C loop is doing
the heavy lifting searching the string. From an algo perspective this is slower
than the others. But good to know for Python users for runtime speedup.

Runtime: 40 ms, faster than 99.15% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution4:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]

        return min(index) if len(index) > 0 else -1

###############################################################################
if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"string = {s}")
        
        res = sol.firstUniqChar(s)

        print(f"\nres = {res}")


    sol = Solution() # use dict; if same letter seen again, set d[ch] = float('inf')
    sol = Solution2() # use dict w/ seen set
    #sol = Solution3() # use dict mapping chars to list of indices
    #sol = Solution4() # use s.index()

    comment = "LC ex1; answer = 0"
    s = "leetcode"
    test(s, comment)

    comment = "LC ex2; answer = 2"
    s = "loveleetcode"
    test(s, comment)

    comment = "trivial case; answer = -1"
    s = ""
    test(s, comment)
