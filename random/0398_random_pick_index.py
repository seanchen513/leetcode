"""
398. Random Pick Index
Medium

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""

from typing import List
import collections
import random

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

###############################################################################
"""
Solution: use index map of input array.

This uses more memory than necessary since it stores the indices.

init:
O(n) time: to build index map
O(n) extra memory: for index map

pick:
O(1) time
O(n) extra memory: for list d[target] of indices

"""
class Solution:
    def __init__(self, nums: List[int]):
        self.d = collections.defaultdict(list)
        
        for i, x in enumerate(nums):
            self.d[x].append(i)
        
    def pick(self, target: int) -> int:
        indices = self.d[target]
        
        i = random.randint(0, len(indices) - 1)
        #i = int(random.random() * len(indices)) # this also works
        
        return indices[i]
        
        #return random.choice(self.d[target])


###############################################################################
"""
Solution 2: store input array itself, and choose randomly from list of
indices, where list is built up naively using linear scan.

init:
O(1) time
O(n) extra memory

pick:
O(n) time
O(n) extra memory: to build list of indices for target

"""
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def pick(self, target: int) -> int:
        return random.choice([i for i, x in enumerate(self.nums) if x == target])

###############################################################################
"""
Solution 3: use simple reservoir sampling (Algorithm R) to pick 1 item from n items. 
Here, n is given indirectly: it is the number of duplicates of parameter target.
The items we are picking from are the indices corresponding to the target value.

Pro: O(1) memory for picking. Good for huge input stream.
Con: O(n) time for picking. Not as big a deal for huge input stream, since we
would be dealing with one new number at a time.

Note that the optimal algo for reservoir sampling is Algorithm L,
which computes how many items to skip before the next item to pick (put in the
reservoir, replacing another element). The key is that the number of items to
skip follows a geometric distrib and can be computed in constant time.
Algorithm L is O(k(1+log(n/k))) time. [not implemented here]

###

Proof that each duplicate has an equal chance of being picked:
Suppose target has n duplicates.

1st duplicate:
p = 1 (pick) * 1/2 (no replace) * 2/3 (no replace) * ... * (n-1)/n (no replace) = 1/n

2nd duplicate:
p = 1/2 (pick) * 2/3 (no replace) * ... * (n-1)/n (no replace) = 1/n

3rd duplicate:
p = 1/3 (pick) * 3/4 (no replace) * ... * (n-1)/n (no replace) = 1/n

...

(n-1)th duplicate:
p = 1/(n-1) (pick) * (n-1)/n (no replace) = 1/n

nth duplicate:
p = 1/n (pick) = 1/n

###

init:
O(1) time
O(n) extra memory

pick:
O(n) time
O(1) extra memory

"""
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def pick(self, target: int) -> int:
        count = 0

        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == 1:
                    res = i

        return res
