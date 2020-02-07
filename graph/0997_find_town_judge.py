"""
997. Find the Town Judge
Easy

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
"""

from typing import List
import collections

###############################################################################
"""
Solution 1: brute force

O(N + len(trust)) time
O(N^2) extra space for dict; O(N) for set
"""
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust and N == 1:
            return 1
        
        # d is O(N^2) space
        d = collections.defaultdict(list) # trusted -> list of trusters
        trusters = set() # O(N) space

        for truster, trusted in trust: # O(len(trust))
            d[trusted].append(truster)
            trusters.add(truster)
            
        # O(N) since d might have an entry for each person (trusted)
        cand = [trusted for trusted, trusters in d.items() if len(trusters)==N-1]
            
        if len(cand) == 1 and cand[0] not in trusters:
            return cand[0]

        return -1

###############################################################################
"""
Solution 2:

Consider trust as a directed graph from truster to trusted.  
The node with degree in - out = N - 1 is the judge.

If N = 1 and trust = [], then in - out = N - 1 = 1 - 1 = 0 for the judge.

O(len(trust) + N) time
O(N) extra space for "degree" array
"""
class Solution2:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        degree = [0]*(N+1) # ignore index 0

        for truster, trusted in trust:
            degree[trusted] += 1 # in
            degree[truster] -= 1 # out

        for i in range(1, N+1):
            if degree[i] == N - 1:
                return i

        return -1 

###############################################################################
"""
Solution 3: count how many people trust each person (votes; in-degree)
and check for the one with N-1 votes.  But if a person is a truster,
use a sentinel float('inf') to invalidate the person.

If N = 1 and trust = [], then in - out = N - 1 = 0 for the judge.

O(N + len(trust)) time
O(N) extra space for "votes" array
"""
class Solution3:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        votes = [-1] + [0]*N # [-1] to skip this index in final loop

        for truster, trusted in trust:
            votes[trusted] += 1
            votes[truster] = float('inf') # cannot be the judge

        for i, v in enumerate(votes):
            if v == N-1:
                return i
        
        return -1

###############################################################################

if __name__ == "__main__":
    def test(N, trust, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        res = s.findJudge(N, trust)

        print(f"\nN = {N}")
        print(f"\n{trust}")
        print(f"\nresult = {res}")


    s = Solution() 
    s = Solution2() 
    s = Solution3() 

    comment = "LC ex1; answer = 2"
    N = 2
    trust = [[1,2]]
    test(N, trust, comment)

    comment = "LC ex2; answer = 3"
    N = 3
    trust = [[1,3],[2,3]]
    test(N, trust, comment)

    comment = "LC ex3; answer = -1"
    N = 3
    trust = [[1,3],[2,3],[3,1]]
    test(N, trust, comment)

    comment = "LC ex4; answer = -1"
    N = 3
    trust = [[1,2],[2,3]]
    test(N, trust, comment)

    comment = "LC ex5; answer = 3"
    N = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    test(N, trust, comment)

    comment = "LC test case; answer = 1"
    N = 1
    trust =  []
    test(N, trust, comment)
