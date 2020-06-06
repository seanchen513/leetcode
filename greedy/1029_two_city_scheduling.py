"""
1029. Two City Scheduling
Easy

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110

Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""

from typing import List
import random

###############################################################################
"""
Solution: greedy. Pick city A for the n people with the greatest difference
cost_B - cost_A. This maximizes the savings from choosing city A over city B
for n people.

O(n log n) time: for sorting
O(n) extra space: for sorted array; O(1) if sort in-place.
"""
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
            
        s = sorted(costs, key=lambda x: x[1] - x[0])

        return sum(x[1] for x in s[:n]) + sum(x[0] for x in s[n:])

"""
Solution 1b: rewrite
"""
class Solution1b:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        res = 0
            
        s = sorted(costs, key=lambda x: x[1] - x[0])

        for i in range(n):
            res += s[i][1] + s[i+n][0]

        return res

###############################################################################
"""
Solution 2: use quick select to find the nth smallest element, where
n = len(costs) // 2.

Note: the partition() function is modified so that the pivot is calculated
as the difference in costs between going to city A and city B for the same
person. Also, a similar calculation is made for each array element before
comparing to the pivot.

C++:
nth_element(begin(cs), begin(cs) + cs.size() / 2, end(cs), 
    [](vector<int> &a, vector<int> &b) {
        return (a[0] - a[1] < b[0] - b[1]);
});

###

This beats the sorting solution in the average case, ties or beats it in
virtually all cases, and is only worse in pathological cases.

O(n^2) time worst case, but O(n) avg case, and O(n log n) with "high probability".
Worst case can be improved to O(n) using median-of-medians or introselect (not done here).

O(1) extra space
"""
class Solution2:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 2-way partition, putting pivot in proper place with elts to its left
        # < pivot, elts to its right > pivot. Assumes pivot value starts at a[right].
        def partition(a, left, right):
            #pv = a[right]
            pv = a[right][1] - a[right][0]
            i = left # index of next position to swap a smaller-than-pivot element to

            # Move all elts smaller than pivot to the left (of pivot).
            for j in range(left, right):
                #if a[j] < pv:
                if a[j][1] - a[j][0] < pv:
                    a[i], a[j] = a[j], a[i]
                    i += 1

            a[i], a[right] = a[right], a[i] # swap pivot to its proper position
            return i # pivot index

        def select(a, k):
            left = 0
            right = len(a) - 1

            while left <= right:
                # Pick random initial pivot to feed into partition().
                # Swap it to position at "right" index.
                p = random.randint(left, right) # inclusive
                a[p], a[right] = a[right], a[p]
                p = partition(a, left, right)

                if p == k:
                    return a[k]
                elif p > k:
                    right = p - 1
                else: # p < k
                    left = p + 1

        n = len(costs) // 2
        select(costs, n-1) # 2nd arg can be n-1 or n
        res = 0
        
        for i in range(n):
            res += costs[i][1] + costs[i+n][0]

        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ncosts = {arr}")

        res = sol.twoCitySchedCost(arr)

        print(f"\nresult = {res}")


    sol = Solution() # sort
    sol = Solution1b() # rewrite

    sol = Solution2() # quick select

    comment = "LC example; answer = 110"
    arr = [[10,20],[30,200],[400,50],[30,20]]
    test(arr, comment)
    