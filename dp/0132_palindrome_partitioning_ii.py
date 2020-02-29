"""
132. Palindrome Partitioning II
Hard

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

###############################################################################
"""
Solution 1: recursion w/ memoization via @functools.lru_cache().

TLE's without memoization.
Passing start index instead of substring wasn't faster.

Runtime: 1080 ms, faster than 8.87% of Python3 online submissions
Memory Usage: 29.3 MB, less than 90.00% of Python3 online submissions
"""
import functools
class Solution:
    def minCut(self, s: str) -> int:
        @functools.lru_cache(None)
        def rec(t, n_cuts):
            nonlocal min_cuts
            
            if t == t[::-1]:
                if n_cuts < min_cuts:
                    min_cuts = n_cuts
                return

            if n_cuts >= min_cuts:
                return

            for end in range(len(t) - 1, -1, -1):
                if t[0] == t[end]: # to avoid some copying
                    t2 = t[:end+1]

                    if t2 == t2[::-1]:
                        rec(t[end+1:], n_cuts + 1)

        min_cuts = len(s) - 1

        rec(s, 0)

        return min_cuts

###############################################################################
"""
Solution 2: naive tabulation.  Nested loops for start and end indices of
substrings to check for palindromes.  Cutting around palindromes give 
relation:

new_cuts = cuts[start] + 1

DP table is "cuts".  
cuts[k] = minimum number of cuts for substring up to index k-1.

DP relation is:
cuts[end] = min( cuts[end], cuts[start] + 1 )

O(n^3) time
O(n) extra space

Without initial checks for cases 0 and 1:
Runtime: 736 ms, faster than 33.24% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions

With initial checks for cases 0 and 1:
Runtime: 100 ms, faster than 94.04% of Python3 online submissions
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0

        # Initial check for case of one cut partitioning the string into
        # two palindromes.
        n = len(s)
        for i in range(1, n-1):
            if s[0] == s[i] and s[i+1] == s[-1]:
                t = s[:i]
                u = s[i:]
                if t == t[::-1] and u == u[::-1]:
                    return 1
                
        # Number of cuts for the first k chars.  This is our dp table.
        # Same as number of cuts up for substring from index 0 to k-1.
        # Dummy value cuts[0] = -1 to avoid using an "if" statement
        # when calculating new_cuts.
        cuts = list(range(-1, n)) # [-1, 0, 1, ..., n-1]

        for start in range(n):

            #for end in range(start + 1, n + 1): # one past last char of substring
            for end in range(start, n): # last char of substring
                t = s[start:end+1]
                if t == t[::-1]:
                    new_cuts = cuts[start] + 1

                    if new_cuts < cuts[end + 1]:
                        cuts[end + 1] = new_cuts 

        return cuts[-1]

###############################################################################
"""
Solution 3: tabulation.  Look at each char as midpoint of palindrome, and
expand on both sides to check for palindrome to determine cuts.

https://leetcode.com/problems/palindrome-partitioning-ii/discuss/42198/My-solution-does-not-need-a-table-for-palindrome-is-it-right-It-uses-only-O(n)-space.

O(n^2) time
O(n) extra space

Without initial checks for cases 0 and 1:
Runtime: 152 ms, faster than 90.44% of Python3 online submissions
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions

With initial checks for cases 0 and 1:
Runtime: 24 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def minCut(self, s: str) -> int:        
        if s == s[::-1]:
            return 0

        # Initial check for case of one cut partitioning the string into
        # two palindromes.
        n = len(s)
        for i in range(1, n-1):
            if s[0] == s[i] and s[i+1] == s[-1]:
                t = s[:i]
                u = s[i:]
                if t == t[::-1] and u == u[::-1]:
                    return 1

        # Number of cuts for the first k chars.  This is our dp table.
        # Same as number of cuts up for substring from index 0 to k-1.
        # Dummy value cuts[0] = -1 to avoid using an "if" statement
        # when calculating new_cut_at_end.
        cuts = list(range(-1, n)) # [-1, 0, 1, ..., n-1]

        # Iterate through all chars as midpoint of palindrome.
        for mid in range(n): # range(1, n) also works?
            # (Case 1) odd length strings: center is at index mid.
            # Expand on both sides.  
            # While we have a palindrome, cut around the palindrome.
            # Number of cuts including the palindrome = 1 + number of cuts
            # before the palindrome.
            start = end = mid
            while start >= 0 and end < n and s[start] == s[end]:
                new_cut_at_end = cuts[start] + 1
                
                if new_cut_at_end < cuts[end + 1]:
                    cuts[end + 1] = new_cut_at_end

                start -= 1
                end += 1
            
            # (Case 2) even length strings: center is b/w [mid-1, mid].
            # Expand on both sides.
            start, end = mid-1, mid
            while start >= 0 and end < n and s[start] == s[end]:
                new_cut_at_end = cuts[start] + 1
                
                if new_cut_at_end < cuts[end + 1]:
                    cuts[end + 1] = new_cut_at_end

                start -= 1
                end += 1

        return cuts[n]

"""
Solution 3b: concise version of sol 3 w/o initial checks.
"""
class Solution3b:
    def minCut(self, s: str) -> int:
        n = len(s)
        cuts = list(range(-1, n))

        for mid in range(n):
            for (start, end) in (mid, mid), (mid-1, mid):
                while start >= 0 and end < n and s[start] == s[end]:
                    cuts[end + 1] = min(cuts[end + 1], cuts[start] + 1)
                    start -= 1
                    end += 1
        
        return cuts[n]

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        
        res = sol.minCut(s)

        print(f"\nres = {res}\n")
        

    sol = Solution() # memoization
    
    sol = Solution2() # naive tabulation

    sol = Solution3() # tabulation; chars as midpoints of palindromes
    #sol = Solution3b() # concise version

    comment = "LC ex1; answer = 1"
    s = "aab"
    test(s, comment)

    comment = "LC test case; answer = 0"
    s = "bb"
    test(s, comment)

    comment = "trivial case; answer = 0"
    s = "a"
    test(s, comment)

    comment = "don't be greedy at first; answer = 1"
    s = "aaabba"
    test(s, comment)

    comment = "LC test case; TLE danger; answer = 75"
    s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
    test(s, comment)
