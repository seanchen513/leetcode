"""
134. Gas Station
Medium

There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.

Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

from typing import List

###############################################################################
"""
Solution: (greedy) Calculate the differences in gas and cost. 
This is the net gain in gas from each station. 
Calculate the running sum of these differences.

Changing where we start calculating the running sum only shifts all the
values. The minimum will be the same no matter where we start.
Start at the index just after the minimum sum of differences.

It's possible to travel around the route if and only if:
sum_diff for whole array = sum(gas) - sum(cost) >= 0

LC example:

 1  2  3  4  5  gas
 3  4  5  1  2  cost
-2 -2 -2  3  3  diff

-2 -4 -6 -3  0  sum_diff
      min

O(n) time
O(1) extra space
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        sum_diff = 0
        min_sum_diff = float('inf')

        for i in range(n):
            sum_diff += gas[i] - cost[i]

            if sum_diff < min_sum_diff:
                min_sum_diff = sum_diff
                min_i = i

        if sum_diff < 0:
            return -1

        # Take mod in case min_i is the last index, n-1.
        return (min_i + 1) % n

"""
Proof:
Let s(i, j) be sum of diffs from index i to j, inclusive.
Suppose s(0, i) is the min among all s(0, j) for j = 0, ..., n-1.

We want to show that if we start traveling at i+1, we cane make a 
circular route. This is the same as showing
(1) s(i+1, j) >= 0 for all j = i+1, ..., n-1 and
(2) s(i+1, n-1) + s(0, k) >= 0 for all k = 0, ..., i.

Since s(0, i) is the min, we have
s(0, i) <= s(0, j) = s(0, i) + s(i+1, j) for j = i+1, ..., n-1

Thus,
s(i+1, j) >= 0 for all j = i+1, ..., n-1.
This proves (1).

For (2), rewrite the expression in terms of the full sum s(0, n-1):

s(i+1, n-1) + s(0, k)
= s(0, n-1) - s(k+1, i)

Assume the term s(0, n-1) >= 0. The full expression is >= 0 if s(k+1, i) <= 0.

s(k+1, i) = s(0, i) - s(0, k) <= 0 since the min s(0, i) <= s(0, k).

This proves (2) for k = 0, .., i-1, where we assumed the case k = i (the full sum).

"""

###############################################################################
"""
Solution 2:

Suppose we start at A and B is the first station we can't reach.
Then we also wouldn't be able to reach B from any station that was on
the way from A to B. So the next possible start station is B.

O(n) time
O(1) extra space
"""
class Solution2:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start = 0

        net = 0 # net balance of gas
        sum_diff = 0 # same as "net" except that we never reset it

        for i in range(n):
            net += gas[i] - cost[i]
            sum_diff += gas[i] - cost[i]

            if net < 0: # start at station i+1 with 0 gas instead
                start = i + 1
                net = 0

        if sum_diff < 0:
            return -1

        # Take mod in case we restarted at start = n, which should be 0 instead.
        return start % n

###############################################################################

if __name__ == "__main__":
    def test(gas, cost, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\n{gas}")
        print(f"{cost}")
        
        res = sol.canCompleteCircuit(gas, cost)

        print(f"\nresult = {res}\n")


    sol = Solution() # 
    #sol = Solution2() # 
    
    comment = "LC example; answer = 3"
    gas  = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    test(gas, cost, comment)

    comment = "LC TC; answer = -1"
    gas = [3,3,4]
    cost = [3,4,4]
    test(gas, cost, comment)

    # This test case is good for checking wrap-around.
    comment = "rotated LC example so min sum diff at end; answer = 0"
    gas  = [4,5,1,2,3]
    cost = [1,2,3,4,5]
    test(gas, cost, comment)
