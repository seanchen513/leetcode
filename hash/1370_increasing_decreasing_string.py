"""
1370. Increasing Decreasing String
Easy

Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Example 2:

Input: s = "rat"
Output: "art"
Explanation: The word "rat" becomes "art" after re-ordering it with the mentioned algorithm.

Example 3:

Input: s = "leetcode"
Output: "cdelotee"

Example 4:

Input: s = "ggggggg"
Output: "ggggggg"

Example 5:

Input: s = "spo"
Output: "ops"
 
Constraints:

1 <= s.length <= 500
s contains only lower-case English letters.
"""

import collections
###############################################################################
"""
Solution: use dict to count chars. Loop through alphabet forward and reverse.

O(n) time
O(n) extra space
"""
class Solution:
    def sortString(self, s: str) -> str:
        d = collections.Counter(s)
        res = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while d:
            for ch in alphabet:
                if ch in d:
                    res.append(ch)
                    if d[ch] == 1:
                        del d[ch]
                    else:
                        d[ch] -= 1

            for ch in reversed(alphabet):
                if ch in d:
                    res.append(ch)
                    if d[ch] == 1:
                        del d[ch]
                    else:
                        d[ch] -= 1

        return ''.join(res)

"""
Solution 1b: don't delete from dict, but check count d[ch]. For loop condition,
check len(res) < len(s) instead of dict.
"""
class Solution1b:
    def sortString(self, s: str) -> str:
        d = collections.Counter(s)
        res = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        while len(res) < len(s):
            for ch in alphabet:
                if d[ch] > 0:
                    res.append(ch)
                    d[ch] -= 1

            for ch in reversed(alphabet):
                if d[ch] > 0:
                    res.append(ch)
                    d[ch] -= 1

        return ''.join(res)

###############################################################################
"""
Solution 2: use dict to count chars. Loop through sorted keys forward and
in reverse.
"""
class Solution2:
    def sortString(self, s: str) -> str:
        d = collections.Counter(s)
        res = []
        
        while d:
            keys = sorted(d)
            res.extend(keys)
            
            for k in keys:
                if d[k] == 1:
                    del d[k]
                else:
                    d[k] -= 1
            
            keys = sorted(d, reverse=True)
            res.extend(keys)

            for k in keys:
                if d[k] == 1:
                    del d[k]
                else:
                    d[k] -= 1
                
        return ''.join(res)

"""
Solution 1b: don't delete from dict, but check count d[ch]. For loop condition,
check len(res) < len(s) instead of dict.
"""
class Solution2b:
    def sortString(self, s: str) -> str:
        d = collections.Counter(s)
        res = []
        
        keys = sorted(d)

        while len(res) < len(s):
            for k in keys:
                if d[k] > 0:
                    res.append(k)
                    d[k] -= 1
            
            for k in reversed(keys):
                if d[k] > 0:
                    res.append(k)
                    d[k] -= 1
                
        return ''.join(res)
