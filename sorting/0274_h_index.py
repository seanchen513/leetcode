"""
274. H-Index
Medium

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 

Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""

from typing import List

###############################################################################
"""
Solution: use counting sort.

Any citation count > n can be replaced by n and the h-index will still be
the same. This is because we always have h <= n.

After counting sort of citations, we can proceed as in other solution by 
traversing the counts array to find the largest i such that cit[i] > i.
But we can do better.

Define s_k = sum of all counts with cit >= k, ie, number of papers having
>= k citations.  By def, the h-index is the largest k with k <= s_k.

Example:
citations = 1, 3, 2, 3, 100

0 1 2 3 4 5     index
0 1 1 2 0 1     count
5 5 4 3 1 1     s_k
      h

O(n) time
O(n) extra space: for storing the counts
"""
class Solution:
    #def hIndex(self, citations: List[int]) -> int:
    def hIndex(self, cit: List[int]) -> int:
        n = len(cit)
        counts = [0] * (n+1)

        for c in cit:
            counts[min(c, n)] += 1

        k = n
        s = counts[n]

        while k > s:
            k -= 1
            s += counts[k]

        return k

###############################################################################
"""
Solution: sort in reverse order. 

If cit[i] > i, then papers 0 to i (i+1 papers) have at least i+1 citations.
So we search for the largest i such that cit[i] > i. Then the h-index is i+1.
If no such i, then the h-index is 0; this happens when all citations are 0.

Alternatively, the h-index is the first i such that cit[i] <= i. If no such
i, then the h-index is n.

Note: 0 <= h <= n
h = 0 when all citations are 0.
h = n when all citations are >= n.

O(n log n) time: due to sorting.
O(1) extra space: if sort in-place.

Examples:
0 1 2 3 4
6 5 3 1 0
    h

0 1 2 3
4 4 0 0
    h

 0  1
15 11
    h

0 1 2 3 4
1 1 1 1 1 
  h
"""
class Solution2:
    #def hIndex(self, citations: List[int]) -> int:
    def hIndex(self, cit: List[int]) -> int:
        n = len(cit)
        cit.sort(reverse=True)

        i = 0
        while i < n and cit[i] > i:
            i += 1

        return i

"""
Solution 2b: concise version of sol 2.
"""
class Solution2b:
    def hIndex(self, cit: List[int]) -> int:
        cit.sort(reverse=True)

        return sum(i < c for i, c in enumerate(cit))
        #return sum(i < c for i, c in enumerate(sorted(cit, reverse=True)))

###############################################################################
"""
Solution 3: first attempt
"""
class Solution3:
    def hIndex(self, cit: List[int]) -> int:
        n = len(cit)
        if n == 0:
            return 0
        # if n == 1:
        #     return 0 if cit[0] == 0 else 1

        cit.sort(reverse=True)

        if cit[-1] >= n:
            return n

        for i in range(1, n):
            if cit[i-1] >= i >= cit[i]:
                return i

        return 0

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.hIndex(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # use counting sort
    
    sol = Solution2() # sort (in reverse)
    sol = Solution2b() # concise version

    #sol = Solution3() # first attempt

    comment = "LC example; answer = 3"
    arr = [3,0,6,1,5]
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = []
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = [0]
    test(arr, comment)

    comment = "LC test case; answer = 0"
    arr = [0,0]
    test(arr, comment)

    comment = "answer = 1"
    arr = [0,1]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [1,1]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [11,15]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [1]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [100]
    test(arr, comment)

    comment = "LC test case; answer = 2"
    arr = [4,4,0,0]
    test(arr, comment)

    comment = "LC test case; answer = 1"
    arr = [1,1,1,1,1]
    test(arr, comment)
