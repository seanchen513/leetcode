"""
444. Sequence Reconstruction
Medium

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].

Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
"""

from typing import List
        
###############################################################################
"""
The sequence "org" is the unique sequence that can be reconstructed from "seqs"
if and only if these conditions holds:

1. The set of all elements in "org" is the same as the set of all elements from
all sequences in "seq".
2. Every 2 consecutive elements in "org" are consecutive elements in some
sequence in "seqs".
3. Every sequence in "seqs" is a subsequence in "org".

Check (1) first to get rid of cases with outlier numbers in "seqs".
Checking (2) before (3) seems to be faster on LC.

Based on idea from:
https://leetcode.com/problems/sequence-reconstruction/discuss/92574/Very-short-solution-with-explanation

LeetCode Feb 10, 2020:
Runtime: 436 ms, faster than 94.42% of Python3 online submissions
Memory Usage: 17 MB, less than 100.00% of Python3 online submissions
"""
#import functools
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        ### Used this or parts of it to get a couple of LC test cases:
        #if org == [1] and (seqs == [] or seqs == [[], []]):
        #    return False
        
        ### Check condition 1.  Check this first to get rid of cases with
        ### outlier numbers in seqs.

        #sets = [set(seq) for seq in seqs]
        #seqs_set = functools.reduce(lambda x, y: x | y, sets, set())
        #if set(org) != seqs_set: # SLOW

        if set(org) != set(x for seq in seqs for x in seq): # much faster
            #print("Failed at condition 1.")
            return False

        ### Check condition 2.

        s = set()
        for seq in seqs:
            for i in range(1, len(seq)):
                s.add((seq[i-1], seq[i]))

        for i in range(1, len(org)):
            if (org[i-1], org[i]) not in s:
                #print("Failed at condition 2.")
                return False

        ### Check condition 3.

        inv = {}
        for i, x in enumerate(org):
            inv[x] = i

        for seq in seqs:
            for i in range(1, len(seq)):
                # equality will disquality sequences like [1, 1]
                if inv[seq[i]] <= inv[seq[i-1]]:
                    #print("Failed at condition 3.")
                    return False

        return True
          
###############################################################################

if __name__ == "__main__":
    def test(org, seqs, comment=None):
        print("="*80)
        if comment:
            print(comment)

        res = s.sequenceReconstruction(org, seqs)

        print(f"\norg = {org}")
        print(f"\nseqs = {seqs}")
        
        print(f"\nresult = {res}")


    s = Solution()

    comment = "LC ex1; answer = False"
    org = [1,2,3]
    seqs = [[1,2],[1,3]]
    test(org, seqs, comment)

    comment = "LC ex2; answer = False"
    org = [1,2,3]
    seqs = [[1,2]]
    test(org, seqs, comment)

    comment = "LC ex3; answer = True"
    org = [1,2,3]
    seqs = [[1,2],[1,3],[2,3]]
    test(org, seqs, comment)

    comment = "LC ex4; answer = True"
    org = [4,1,5,2,6,3]
    seqs = [[5,2,6,3],[4,1,5,2]]
    test(org, seqs, comment)

    comment = "LC test case; answer = False"
    org = [1]
    seqs = []
    test(org, seqs, comment)

    comment = "LC test case; answer = False"
    org = [1]
    seqs = [[], []]
    test(org, seqs, comment)

    comment = "LC test case; answer = False"
    org = [1]
    seqs = [[1,1]]
    test(org, seqs, comment)

    comment = "LC test case; answer = False"
    org = [5,3,2,4,1]
    seqs = [[5,3,2,4],[4,1],[1],[3],[2,4], [1000000000]]
    test(org, seqs, comment)
