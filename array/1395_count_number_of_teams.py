"""
1395. Count Number of Teams
Medium

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 

Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:

Input: rating = [1,2,3,4]
Output: 4
 
Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5
"""

from typing import List
import collections
import itertools

###############################################################################
"""
Solution: brute force using itertools.combinations().

O(n^3) time
O(1) extra space
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0

        for i, j, k in itertools.combinations(rating, 3):
            if i < j < k or i > j > k:
                count += 1

        return count


###############################################################################
"""
Solution 2: brute force.

O(n^3) time
O(1) extra space
"""
class Solution2:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        if n < 3:
            return 0

        count = 0

        for i in range(n-2):
            ri = rating[i]
            
            for j in range(i+1, n-1):
                rj = rating[j]

                if ri < rj:
                    for k in range(j+1, n):
                        if rj < rating[k]:
                            count += 1
                elif ri > rj:
                    for k in range(j+1, n):
                        if rj > rating[k]:
                            count += 1

        return count

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.numTeams(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # brute force using itertools.combinations()
    sol = Solution2() # brute force

    comment = "LC ex1; answer = 3"
    arr = [2,5,3,4,1]
    test(arr, comment)

    comment = "LC ex2; answer = 0"
    arr = [2,1,3]
    test(arr, comment)

    comment = "LC ex3; answer = 4"
    arr = [1,2,3,4]
    test(arr, comment)
