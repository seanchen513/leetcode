"""
1046. Last Stone Weight
Easy

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:

Input: [2,7,4,1,8,1]
Output: 1

Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 
Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

from typing import List
import heapq
import bisect
        
###############################################################################
"""
Solution: use max heap to store stones

O(n log n) time
O(1) extra space: if turn input array into heap in-place using heapify.
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use negative values so we can have a max heap
        for i, x in enumerate(stones):
            stones[i] = -x

        heapq.heapify(stones) # O(n)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y > x:
                heapq.heappush(stones, x - y)

        return -stones[0] if stones else 0

###############################################################################
"""
Solution2: sort array at start, then insert new elts in sorted order.

O(n^2) time
O(1) extra space: sort in-place
"""
class Solution2:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            
            if y > x:
                bisect.insort(stones, y - x)
                
        return stones[0] if stones else 0
            
###############################################################################
"""
Solution 3: sort array every iteration.

O(sum(i log i) for i=2..n) = O(n^2 log n) time
O(1) extra space: sort in-place
"""
class Solution3:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()

            y = stones.pop()
            x = stones.pop()
            
            if y > x:
                stones.append(y - x)
                
        return stones[0] if stones else 0
                 
###############################################################################
"""
Solution 4: use list.index() to find max. To avoid having to shift array when
removing an element, swap the max with the last element and then pop.

O(n^2) time
O(1) extra space: sort in-place
"""
class Solution4:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def remove_max():
            i_max = stones.index(max(stones))

            # swap stone to be removed with the one at the end
            stones[i_max], stones[-1] = stones[-1], stones[i_max]

            return stones.pop()
        
        while len(stones) > 1:
            y = remove_max()
            x = remove_max()
            
            if y > x:
                stones.append(y - x)
                
        return stones[0] if stones else 0
