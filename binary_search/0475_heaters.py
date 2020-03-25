"""
475. Heaters
Easy

Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same. 

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""

from typing import List
import bisect

###############################################################################
"""
Solution: sort heaters, then for each use, use binary search of house
location on sorted heaters array.

Each house is heated by a heater before or after it. The min distance
of the house between the two heaters is the radius required by that house.
The answer is the max radius across all houses. Special cases for houses
that only have heaters on one side.

O( (#houses + #heaters) * log #heaters ) time

O(1) extra space: if heaters sorted in-place.

Runtime: 288 ms, faster than 88.11% of Python3 online submissions
Memory Usage: 16.2 MB, less than 16.67% of Python3 online submissions

Replacing min() and max() with "if" statements, and using "inf" var:
Runtime: 280 ms, faster than 95.15% of Python3 online submissions
Memory Usage: 16.1 MB, less than 16.67% of Python3 online submissions
"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(heaters)
        heaters.sort()
        
        r = 0
        
        for h in houses:
            i = bisect.bisect(heaters, h)
            ### heaters[i-1] <= h < heaters[i]

            if i == 0:
                r = max(r, heaters[i] - h)

            elif i == n:
                r = max(r, h - heaters[i-1])

            else:
                r = max(r, min(heaters[i] - h, h - heaters[i-1]))

            #print(f"\nh, i, r = {h}, {i}, {r}")
            
        return r

"""
Solution 1b: same as sol 1, but add two fake heaters at positive and
negative infinity. This avoids branching.
"""
class Solution1b:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
        r = 0
        
        for h in houses:
            i = bisect.bisect(heaters, h)
            r = max(r, min(heaters[i] - h, h - heaters[i-1]))

        return r

"""
Solution 1c: same as sol 1b, but sort houses and use pointer for heaters
as start index to do next binary search.

This may be useful if #houses << #heaters.
"""
class Solution1c:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
        r = 0
        i = 0 # index for heaters
        
        for h in sorted(houses):
            i = bisect.bisect(heaters, h, i)
            r = max(r, min(heaters[i] - h, h - heaters[i-1]))

        return r

###############################################################################
"""
Solution 2: sort both houses and heater. Traverse houses and track pointer for
heaters. For each house, find the closest heater by comparing the house
location to the average location of adjacent heaters.

This is a good solution if #houses ~< #heaters..

O(m log m + n log n) time

"""
class Solution2:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters = sorted(heaters) + [float('inf')]
        
        i = 0 # index of current closest heater
        r = 0

        for h in sorted(houses):
            while h >= sum(heaters[i:i+2]) / 2:
                i += 1
            
            r = max(r, abs(heaters[i] - h))

        return r

###############################################################################
"""
Solution 3: brute force

TLE
"""
class Solution3:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        return max(min(abs(h - ht) for ht in heaters) for h in houses)

###############################################################################

if __name__ == "__main__":
    def test(houses, heaters, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"houses = {houses}")
        print(f"heaters = {heaters}")

        res = sol.findRadius(houses, heaters)

        print(f"\nres = {res}\n")


    sol = Solution() # sort heaters, and use bsearch on heaters for each house
    sol = Solution1b() # same, but add two fake heaters at +/- infinity
    sol = Solution1c() # same, but sort houses and use ptr for heaters...

    #sol = Solution2() # sort houses and heaters; ptr for heaters
    
    #sol = Solution3() # brute force

    comment = "LC ex1; answer = 1"
    houses = [1,2,3]
    heaters = [2]
    test(houses, heaters, comment)

    comment = "LC ex2; answer = 1"
    houses = [1,2,3,4]
    heaters = [1,4]
    test(houses, heaters, comment)

    comment = "LC test case; answer = 3"
    houses = [1,5]
    heaters = [2]
    test(houses, heaters, comment)
