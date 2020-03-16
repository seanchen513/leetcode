"""
384. Shuffle an Array
Medium

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

from typing import List
import random

###############################################################################
"""
Solution: use random.shuffle().

When shuffling, create copy of array stored in Solution, shuffle the copy, 
then return it.

Runtime: 268 ms, faster than 96.76% of Python3 online submissions
Memory Usage: 18.2 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.orig = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.orig[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        arr = self.nums[:]
        random.shuffle(arr)

        return arr


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

###############################################################################
"""
Solution 2: create a copy of stored array to do random draws from.
Use random.randrange() to pick from remaining items left.

O(n^2) time: draw n items; popping each item from list takes O(n) time.

O(n) extra space: to store array copy in __init__(), to make array copy
in reset(), and to make array copy for random draws in shuffle().
"""
class Solution2:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.orig = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.orig[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        aux = self.nums[:]

        for i in range(len(self.nums)):
            remove_index = random.randrange(len(aux))
            self.nums[i] = aux.pop(remove_index)

        return self.nums


###############################################################################
"""
Solution 3: Fisher-Yates algo.

On each iteration of algo, generate random int b/w current index and last
index of array.  Swap elements at these indices.  This simulates drawing
and removing elements from a hat (copied array), as t he next range from 
which we select a random index will not include the most recently processed
element.  

Note that in this process, it is possible to swap an element with itself.
We want to permit this, since in a random shuffle, an element might not
move from its original position.

O(n) time: since generating a random index and swapping two values are O(1).

O(n) extra space: for storing array copy in __init__() and making array
copy in reset().  However, we avoid making array copy in shuffle().
"""
class Solution3:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.orig = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.orig[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.nums)

        for i in range(n):
            j = random.randrange(i, n)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

        return self.nums

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print()
        print(arr)
        
        #sol = Solution(arr) # use random.shuffle()
        #sol = Solution2(arr) # do random draws using randrange()
        sol = Solution3(arr) # Fisher-Yates algo

        print("\nShuffle:")
        res = sol.shuffle()
        print(f"res = {res}\n")
        
        print("Reset:")
        res = sol.reset()
        print(f"res = {res}\n")
        
        print("Shuffle:")
        res = sol.shuffle()
        print(f"res = {res}\n")


    comment = "LC example"
    arr = [1,2,3]
    test(arr, comment)
    