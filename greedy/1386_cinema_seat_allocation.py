"""
1386. Cinema Seat Allocation
Medium

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i]=[3,8] means the seat located in row 3 and labelled with 8 is already reserved. 

Return the maximum number of four-person families you can allocate on the cinema seats. A four-person family occupies fours seats in one row, that are next to each other. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be next to each other, however, It is permissible for the four-person family to be separated by an aisle, but in that case, exactly two people have to sit on each side of the aisle.

Example 1:

Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four families, where seats mark with blue are already reserved and contiguous seats mark with orange are for one family. 

Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2

Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4

Constraints:

1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
All reservedSeats[i] are distinct.
"""

from typing import List
import collections

###############################################################################
"""
Solution: process reservedSeats into dict of sets, then iterate over dict,
using set.isdisjoint().

At most 2 families per row. Greedily check if we can allocate seats for
2, 1, or 0 families. Process only rows that appear in the input. For the
other rows, we can always allocate 2 families.

O(k) time, where k = len(reservedSeats)
O(k) extra space

Runtime: 644 ms, faster than 80.00% of Python3 online submissions
Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    #def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    def maxNumberOfFamilies(self, n: int, res: List[List[int]]) -> int:
        d = collections.defaultdict(set)
        for row, c in res: # reserved seats
            d[row].add(c)

        count = 2 * n
        t1 = set([2,3,4,5])
        t2 = set([4,5,6,7])
        t3 = set([6,7,8,9])

        for s in d.values():
            remove = 0

            if not s.isdisjoint(t1):
                remove += 1

            if not s.isdisjoint(t3):
                remove += 1

            if remove == 2 and s.isdisjoint(t2):
                remove = 1

            count -= remove

            #print(s, count)

        return count

###############################################################################
"""
Solution 2: same as sol 1, but don't use set.isdisjoint().

Runtime: 656 ms, faster than 80.00% of Python3 online submissions
Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def maxNumberOfFamilies(self, n: int, res: List[List[int]]) -> int:
        d = collections.defaultdict(set)
        for row, c in res: # reserved seats
            d[row].add(c)

        count = 2 * n

        for s in d.values():
            remove = 0
            
            if (2 in s) or (3 in s) or (4 in s) or (5 in s):
                remove += 1

            if (6 in s) or (7 in s) or (8 in s) or (9 in s):
                remove += 1

            if remove == 2 and (4 not in s) and (5 not in s) and (6 not in s) and (7 not in s):
                remove = 1

            count -= remove

            #print(s, count)

        return count

###############################################################################
"""
Solution 3: use sorting instead of processing input into dict of sets.

O(k log k) time
O(1) extra space: use in-place sort.

Runtime: 740 ms, faster than 40.00% of Python3 online submissions
Memory Usage: 16.3 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def maxNumberOfFamilies(self, n: int, res: List[List[int]]) -> int:
        def process_row(s):
            remove = 0

            if not s.isdisjoint(t1):
                remove += 1

            if not s.isdisjoint(t3):
                remove += 1

            if remove == 2 and s.isdisjoint(t2):
                remove = 1

            return remove


        if not res:
            return 2*n

        res.sort()
        count = 2 * n
        
        t1 = set([2,3,4,5])
        t2 = set([4,5,6,7])
        t3 = set([6,7,8,9])

        s = set()
        prev_row = res[0][0]

        for row, seat in res:
            if row == prev_row:
                prev_row = row
                s.add(seat)
                continue

            count -= process_row(s)

            s = set([seat])
            prev_row = row

        count -= process_row(s)

        return count

###############################################################################

if __name__ == "__main__":   
    def test(n, arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.maxNumberOfFamilies(n, arr)

        print(f"\nres = {res}\n")


    sol = Solution() # use set.isdisjoint()
    sol = Solution2()
    sol = Solution3() # use sorting
    
    comment = "LC ex1; answer = 4"
    n = 3
    arr = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    test(n, arr, comment)

    comment = "LC ex2; answer = 2"
    n = 2
    arr = [[2,1],[1,8],[2,6]]
    test(n, arr, comment)

    comment = "LC ex3; answer = 4"
    n = 4
    arr = [[4,3],[1,4],[4,6],[1,7]]
    test(n, arr, comment)

    comment = "LC test; answer = 5"
    n = 3
    arr = [[2,3]]
    test(n, arr, comment)
