"""
935. Knight Dialer
Medium

A chess knight can move as indicated in the chess diagram below:

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:

Input: 1
Output: 10

Example 2:

Input: 2
Output: 20

Example 3:

Input: 3
Output: 46
 
Note:

1 <= N <= 5000
"""

import collections

###############################################################################
"""
Solution: use vars to track number of dials/sequences that end at each
digit.

Let c_i = number of sequences that end at digit i.

O(n) time
O(1) extra space

Runtime: 288 ms, faster than 93.99% of Python3 online submissions
Memory Usage: 14 MB, less than 23.53% of Python3 online submissions
"""
class Solution:
    def knightDialer(self, n: int) -> int:
        c0 = c1 = c2 = c3 = c4 = c6 = c7 = c8 = c9 = 1

        if n == 1:
            return 10

        for _ in range(1, n):
            c0, c1, c2, c3, c4, c6, c7, c8, c9 = (
                c4 + c6, # 0
                c6 + c8, # 1
                c7 + c9, # 2
                c4 + c8, # 3
                c0 + c3 + c9, # 4
                c0 + c1 + c7, # 6
                c2 + c6, # 7
                c1 + c3, # 8
                c2 + c4 # 9
            )
        
        # print(f"\n0: {c0}")
        # print(f"1: {c1}, 3: {c3}, 7: {c7}, 7: {c9}")
        # print(f"2: {c2}, 8: {c8}")
        # print(f"4: {c4}, 6: {c6}")

        return (c0+c1+c2+c3+c4+c6+c7+c8+c9) % (10**9 + 7)

"""
Solution 1b: same, but make use of symmetry to track fewer vars.

Number of unique dials/sequences ending in 1, 3, 7, 9 are the same.
Number of unique dials/sequences ending in 2, 8 are the same.
Number of unique dials/sequences ending in 4, 6 are the same.

So suffices to keep track of sequences ending in 0, 1, 2, 4.

Runtime: 152 ms, faster than 94.76% of Python3 online submissions
Memory Usage: 13.8 MB, less than 23.53% of Python3 online submissions
"""
class Solution1b:
    def knightDialer(self, n: int) -> int:
        c0 = c1 = c2 = c4 = 1

        if n == 1:
            return 10

        for _ in range(1, n):
            c0, c1, c2, c4 = (
                c4 + c4, # 0
                c2 + c4, # 1
                c1 + c1, # 2
                c0 + c1 + c1, # 4
            )

        return (c0 + 4*c1 + 2*c2 + 2*c4) % (10**9 + 7)

###############################################################################
"""
Solution 2: DP tabulation using 1d dict.

Transitions (20):

2 -> 2 (8): 1->8, 2->7, 2->9, 3->8, 7->2, 8->1, 8->3, 9->2
2 -> 3 (6): 0->4, 0->6, 1->6, 3->4, 7->6, 9->4

3 -> 2 (6): 4->3, 4->9, 4->0, 6->1, 6->7, 6->0
3 -> 3: None

c2 = 8*c2 + 6*c3
c3 = 6*c2

Runtime: 2044 ms, faster than 28.77% of Python3 online submissions
Memory Usage: 13.8 MB, less than 23.53% of Python3 online submissions
"""
class Solution2:
    def knightDialer(self, n: int) -> int:
        moves = {
            0: [4,6], # 3,3
            1: [6,8], # 3,2
            2: [7,9], # 2,2
            3: [4,8], # 3,2
            4: [3,9,0], # 2,2,2
            #5: [],
            6: [1,7,0], # 2,2,2
            7: [2,6], # 2,3
            8: [1,3], # 2,2
            9: [2,4], # 2,3
        }

        if n == 1:
            return 10

        # number of moves (values) ending at each digit (key)
        c = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        
        for _ in range(1, n):
            c2 = collections.Counter()

            for k, v in c.items():
                for endpt in moves[k]:
                    c2[endpt] += v
            
            c = c2

        return sum(c.values()) % (10**9 + 7)

"""
Solution 2b: same, but using arrays instead of dicts for c and c2.

Runtime: 1020 ms, faster than 76.85% of Python3 online submissions for Knight Dialer.
Memory Usage: 13.8 MB, less than 23.53% of Python3 online submissions for Knight Dialer.
"""
class Solution2b:
    def knightDialer(self, n: int) -> int:
        moves = {
            0: [4,6], # 3,3
            1: [6,8], # 3,2
            2: [7,9], # 2,2
            3: [4,8], # 3,2
            4: [3,9,0], # 2,2,2
            5: [],
            6: [1,7,0], # 2,2,2
            7: [2,6], # 2,3
            8: [1,3], # 2,2
            9: [2,4], # 2,3
        }

        #if n == 1:
        #    return 10
        # c = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]

        # number of moves (values) ending at each digit (index)
        c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        
        for _ in range(1, n):
            c2 = [0] * 10

            for k, v in enumerate(c):
                for endpt in moves[k]:
                    c2[endpt] += v
            
            c = c2

        return sum(c) % (10**9 + 7)

###############################################################################
"""
Solution 3: use matrix exponentiation for transition matrix.

O(log n) time
O(1) extra space

Runtime: 108 ms, faster than 96.16% of Python3 online submissions
Memory Usage: 29.7 MB, less than 11.76% of Python3 online submissions
"""
class Solution3:
    def knightDialer(self, n: int) -> int:
        import numpy as np

        m = np.matrix([
            [0,0,0,0,1,0,1,0,0,0], # 0 -> 4, 6
            [0,0,0,0,0,0,1,0,1,0], # 1 -> 6, 8
            [0,0,0,0,0,0,0,1,0,1], # 2 -> 7, 9
            [0,0,0,0,1,0,0,0,1,0], # 3 -> 4, 8
            [1,0,0,1,0,0,0,0,0,1], # 4 -> 0, 3, 9
            [0,0,0,0,0,0,0,0,0,0], # 5 -> N/A
            [1,1,0,0,0,0,0,1,0,0], # 6 -> 0, 1, 7
            [0,0,1,0,0,0,1,0,0,0], # 7 -> 2, 6
            [0,1,0,1,0,0,0,0,0,0], # 8 -> 1, 3
            [0,0,1,0,1,0,0,0,0,0], # 9 -> 2, 4
        ])

        res = [1] * 10
        mod = 10**9 + 7
        n -= 1

        while n:
            if n & 1:
                res = res * m % mod

            m = m * m % mod

            n //= 2

        return np.sum(res) % mod

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")

        res = sol.knightDialer(n)

        print(f"\nres = {res}\n")


    sol = Solution() # vars
    #sol = Solution1b() # vars w/ symmetry
    
    #sol = Solution2() # moves/transition dict
    #sol = Solution2b() # moves/transition array
    
    #sol = Solution3() # matrix exponentiation

    comment = "LC ex1; answer = 10"
    n = 1
    test(n, comment)

    comment = "LC ex1; answer = 20"
    n = 2
    test(n, comment)

    comment = "LC ex1; answer = 46"
    n = 3
    test(n, comment)

    # comment = "max test case; answer = "
    # n = 5000
    # test(n, comment)

    comment = "; answer = "
    n = 11
    test(n, comment)
