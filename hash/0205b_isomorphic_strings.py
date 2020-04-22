"""
Follow-up to LC205 Isomorphic Strings

https://leetcode.com/problems/isomorphic-strings/discuss/57941/Python-different-solutions-(dictionary-etc)./267905

Group all isomorphic strings.

Obvious sol using sol to LC205 is O(n * m^2), where n is length of each string
and m is num of strings.

O(mn) sol by encoding each string
"""

import collections

###############################################################################
"""
Solution: use dict to map each unique letter to the order (among alphabet) it 
appears in the string. Use this to encode the string. The code represents the 
group of all isomorphic sequences that the sequence belongs to.

O(mn) time, where n is length of each string, and m is number of strings
O(mn) extra space

Example:
aab [0, 0, 1]   "001"
xxy [0, 0, 1]   "001"
xyz [0, 1, 2]   "012"
abc [0, 1, 2]   "012"
def [0, 1, 2]   "012"
xyx [0, 1, 0]   "010"
"""
def group_iso(strs):
    # Each letter is encoded as the order it appears in "s".
    # Eg, first unique letter is encoded as 0, second unique letter as 1, etc.
    # encode() is O(n) time
    def encode(s):
        d = {}
        code = []

        for ch in s:
            if ch not in d:
                d[ch] = len(d)

            code.append(d[ch])

        return str(code) # makes it hashable

    groups = collections.defaultdict(list)

    for s in strs:
        encoded = encode(s)
        print(s, encoded)

        groups[encoded].append(s)
        
    return list(groups.values())

###############################################################################

if __name__ == "__main__":
    strings = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']

    print(f"\nstrings = {strings}\n")

    res = group_iso(strings)

    print(f"\nres = {res}\n")
