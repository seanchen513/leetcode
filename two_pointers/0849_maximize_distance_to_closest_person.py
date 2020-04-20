"""
849. Maximize Distance to Closest Person
Easy

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2

Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: [1,0,0,0]
Output: 3

Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""

from typing import List
import bisect

###############################################################################
"""
Solution: 2 pointers: "last" and i. Take average index between 1's, rounded 
down. If there are 0's at end, calculate distance from index of first/last 1.

Single pass.

O(n) time
O(1) extra space
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)

        # Find the first 1
        for i in range(n):
            if seats[i] == 1:
                break
        
        res = i # Assume a 1 was found
        last = i # index where last 1 was found
        
        for j in range(i+1, n):
            if seats[j] == 1:
                d = (j - last) // 2
                if d > res:
                    res = d
                
                last = j

        d = n - last - 1
        if d > res:
            res = d

        return res

"""
Solution1b: same, just rewrite using "max" and get rid of "d" variable.
"""
class Solution1b:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)

        # Find the first 1
        for i in range(n):
            if seats[i]:
                break
        
        res = i # Assume a 1 was found
        last = i # index where last 1 was found
        
        for j in range(i+1, n):
            if seats[j]:
                res = max(res, (j - last) // 2)                
                last = j

        res = max(res, n - last - 1)

        return res
  
###############################################################################
"""
Solution 2: do forward and reverse pass, finding distance since previous 1.
For each position, take min between the two passes. Take max among all these
mins.

O(n) time
O(n) extra space: for distance array; don't modify input array.
"""
class Solution2:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)

        # Set d = inf initially as sentinel, and so we can take min in second
        # pass. Settign d = None would also work, but be more involved.
        inf = float('inf')
        d = inf # distance to previous 1 in seats array
        
        dist = [inf] * n # can also use [n] * n
        res = 0

        for i in range(n):
            if seats[i] == 1:
                d = 0
            elif d < inf:
                d += 1
                dist[i] = d

        d = inf
        
        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                d = 0
            elif d < inf:
                d += 1
                
            dist[i] = min(dist[i], d)
            if dist[i] > res:
                res = dist[i]

        return res

"""
Solution 2b: same, but use positions in seats array with 0 values to store 
distance info as negative values.

O(n) time
O(1) extra space
"""
class Solution2b:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)        
        d = None
        res = 0
        
        for i in range(n):
            if seats[i] == 1:
                d = 0
            elif d != None: # seats[i] == 0, and 1 has been encountered
                d -= 1
                seats[i] = d # distance from previous 1 as negative value

        d = None

        for i in range(n-1, -1, -1):
            if seats[i] == 1:
                d = 0
            elif d != None: # seats[i] <= 0, and 1 has been encountered
                d -= 1
                
                if seats[i] == 0:
                    seats[i] = d
                else:
                    seats[i] = max(seats[i], d)

            if -seats[i] > res: # take max of both passes
                res = -seats[i]

        return res        
