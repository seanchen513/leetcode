"""
187. Repeated DNA Sequences
Medium

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

from typing import List
import collections

###############################################################################
"""
Solution: brute force counting with dict and string slicing.

O(n) time
O(n) extra space: for dict and output
"""
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        d = collections.Counter()
        
        for i in range(n-9):
            d[s[i:i+10]] += 1
                
        res = []
        
        for k, cnt in d.items():
            if cnt > 1:
                res.append(k)
                
        return res

"""
Solution: same, but with sets instead of dict. Saves time from iterating
through dict.
"""
class Solution1b:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        seen = set()
        res = set()
        
        for i in range(n-9):
            t = s[i:i+10]
            if t in seen:
                res.add(t)
            else:
                seen.add(t)
        
        return list(res)
            
###############################################################################
"""
Solution 2: string hashing, where each letter is represented by these
integers:

A 0
C 1
G 2
T 3

10-char string x0, x1, ..., x9

hash0 = x0 * 4^9 + x1 * 4^8 + ... + x8 * 4 + x9

hash1 = x1 * 4^9 + x2 * 4^8 + ... + x9 * 4 + x10
= hash0 * 4 + x10 - (x0 * 4^10) ### use this one
= (hash0 - x0 * 4^9) * 4 + x10

//

hash0 = x0 + x1 * 4 + x2 * 4^2 + ... + x8 * 4^8 + x9 * 4^9

hash1 = x1 + x2 * 4 + x3 * 4^2 + ... + x9 * 4^8 + x10 * 4^9
= (hash0 - x0) // 4 + x10 * 4^9

"""
class Solution2:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        hash = 0
        
        # Calculate initial hash.
        for i in range(10):
            hash = hash * 4 + d[s[i]]

        indices = collections.defaultdict(list)
        indices[hash] = [0]
        c = 4**10

        for i in range(10, n): # ending index for substring
            hash = hash * 4 + d[s[i]] - d[s[i-10]] * c
            indices[hash].append(i-9)

        res = []
        
        for ind in indices.values():
            if len(ind) > 1:
                i = ind[0]
                res.append(s[i:i+10])
                
        return res

"""
Solution 2b: same, but convert string to list of integers first.
"""
class Solution2b:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        t = [d[ch] for ch in s]
        hash = 0

        # Calculate initial hash.
        for i in range(10):
            hash = hash * 4 + t[i]

        indices = collections.defaultdict(list)
        indices[hash] = [0]
        c = 4**10

        for i in range(10, n): # ending index for substring
            hash = hash * 4 + t[i] - t[i-10] * c
            indices[hash].append(i-9)

        res = []
        
        for ind in indices.values():
            if len(ind) > 1:
                i = ind[0]
                res.append(s[i:i+10])
                
        return res                

"""
Solution 2c: same as sol 2b, but use 2 sets instead of "indices" dict.
"""
class Solution2c:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        t = [d[ch] for ch in s]
        hash = 0

        # Calculate initial hash.
        for i in range(10):
            hash = hash * 4 + t[i]

        seen = {hash}
        res = set()
        c = 4**10

        for i in range(10, n): # ending index for substring
            hash = hash * 4 + t[i] - t[i-10] * c

            if hash in seen:
                res.add(s[i-9:i+1])
            else:
                seen.add(hash)
                
        return list(res)

###############################################################################
"""
Solution 3: represent each nucleotide by bits. Count with dict where keys
are numbers represented by the bit representation of 10-char strings.

A 00
C 01
G 10
T 11

Ten-char string is represented by 20 bits.

00 x1 x2 ... x19 x20
<< 2
x1 x2 x3 ... x20 00
+ x21
x1 x2 x3 ... x20 x21
& ((1 << 20) - 1)
x2 x3 ... x21


"""
class Solution3:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        key = 0

        # Calculate initial key.
        for i in range(10):
            key = (key << 2) + d[s[i]]

        indices = collections.defaultdict(list)
        indices[key] = [0]
        mask = (1 << 20) - 1

        for i in range(10, n): # ending index for substring
            key = ( (key << 2) | d[s[i]] ) & mask
            indices[key].append(i-9)

        res = []
        
        for ind in indices.values():
            if len(ind) > 1:
                i = ind[0]
                res.append(s[i:i+10])
                
        return res                

"""
Solution 3b: same, but convert string to list of integers first.
"""
class Solution3b:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        t = [d[ch] for ch in s]
        key = 0

        # Calculate initial key.
        for i in range(10):
            key = (key << 2) | t[i]

        indices = collections.defaultdict(list)
        indices[key] = [0]
        mask = (1 << 20) - 1

        for i in range(10, n): # ending index for substring
            key = ( (key << 2) | t[i] ) & mask
            indices[key].append(i-9)

        res = []
        
        for ind in indices.values():
            if len(ind) > 1:
                i = ind[0]
                res.append(s[i:i+10])
                
        return res  

"""
Solution 3c: same, but use 2 sets instead of "indices" dict.
"""
class Solution3c:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        d = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        t = [d[ch] for ch in s]
        key = 0

        # Calculate initial key.
        for i in range(10):
            key = (key << 2) | t[i]

        seen = {key}
        res = set()
        mask = (1 << 20) - 1

        for i in range(10, n): # ending index for substring
            key = ( (key << 2) | t[i] ) & mask
            
            if key in seen:
                res.add(s[i-9:i+1])
            else:
                seen.add(key)

        return list(res)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        
        res = sol.findRepeatedDnaSequences(s)

        print(f"\nresult = {res}\n")


    sol = Solution() # brute force counting with dict and string slicing
    sol = Solution1b() # same, but use 2 sets instead of dict

    sol = Solution2() # string hashing
    sol = Solution2b() # same, but convert string to list of integers first
    sol = Solution2c() # use 2 sets instead of "indices" dict

    sol = Solution3() # bits
    sol = Solution3b() # same, but convert string to list of integers first
    sol = Solution3c() # use 2 sets instead of "indices" dict

    comment = 'LC example; answer = ["AAAAACCCCC", "CCCCCAAAAA"]'
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    test(s, comment)

    comment = 'LC TC; answer = ["AAAAAAAAAA"]'
    s = "AAAAAAAAAAA" ## 11 A's
    test(s, comment)

    comment = 'LC TC; answer = []'
    s = ""
    test(s, comment)
