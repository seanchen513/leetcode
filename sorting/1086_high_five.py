"""
1086. High Five
Easy

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]

Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 
Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
"""

from typing import List
import collections
import heapq

###############################################################################
"""
Solution: sort by id, then by negative of score. Then process.

O(n log n) time
O(num students) extra space: for output; assume sorting is in-place
"""
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key=lambda x: (x[0], -x[1]))
        res = []
        prev_i = -1
        k = 0
        
        while k < len(items):
            i = items[k][0]
            
            if i != prev_i:
                total = 0
                for j in range(k, k+5):
                    total += items[j][1]
                res.append([i, total // 5])
            
            prev_i = i
            k += 1
        
        return res

###############################################################################
"""
Solution 2: use dict of min heaps, each of size 5. Sorted dict also used.

O(n log n) time: due to using sorted(d)
O(num students) extra space: for dict and sorted(dict).
"""
class Solution2:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        for i, score in items:
            heapq.heappush(d[i], score)

            if len(d[i]) > 5:
                heapq.heappop(d[i])

        return [[i, sum(d[i]) // 5] for i in sorted(d)]

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.highFive(arr)

        print(f"\nres = {res}\n")


    sol = Solution() # sort
    sol = Solution2() # use min heap

    comment = "LC example; answer = [[1,87],[2,88]]"
    arr = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    test(arr, comment)
    