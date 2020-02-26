"""
33. Search in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

from typing import List

"""
The worst case cannot be better than O(n) because all values might be
duplicates.  A simple linear scan can achieve this worst case time complexity,
but would be less efficient when there are not many duplicates, ie, is still
O(n) when there are no duplicates.  Modified binary search is O(log n) when 
there are no duplicates.
"""

###############################################################################
"""
Solution: same as for LC33, but update lo or high with mid only if we are
sure one side is sorted (by checking strict inequalities).  If we're not sure,
check target vs the ends, and update lo or high accordingly.

Even with duplicates, at least one side (left or right) must be sorted.
Because of duplicates, we cannot check if a side is sorted using non-strict
inequalities; eg, if arr[lo] <= arr[mid], it be something like 1 3 1 1 1.

However, we can check using a strict inequality:
arr[lo] < arr[mid] implies the left side is sorted;
arr[mid] < arr[hi] implies the right side is sorted.

If both strict inequalities do not hold, then we can't tell which side is
sorted.
arr[lo] >= arr[mid] >= arr[hi].

Example:
1 3 1 1 1 search left
1 1 1 3 1 search right
lo <= mid <= hi
"""
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if target == arr[mid]:
                return True
            
            #if arr[mid] > arr[hi]: 
            if arr[lo] < arr[mid]: # left side is sorted; must be strict >
                if arr[lo] <= target < arr[mid]: # target on left side
                    hi = mid - 1
                else:
                    lo = mid + 1

            #elif arr[mid] < arr[lo]: 
            elif arr[mid] < arr[hi]: # right side is sorted; must be strict <
                if arr[mid] < target <= arr[hi]: # target on right side
                    lo = mid + 1
                else:
                    hi = mid - 1

            else:
                # There are duplicates from lo to mid, or from mid to hi.
                # Can't tell which side target is on.
                if target != arr[lo]:
                    lo += 1
                
                if target != arr[hi]:
                    hi -= 1

                # At least one of lo or hi was updated.  Suppose neither
                # were updated.  Then arr[lo] == arr[hi] == target != arr[mid].
                # So arr[lo] and arr[hi] are both < arr[mid] or both > arr[mid].
                # In the former case, arr[lo] < arr[mid], and in the latter
                # case, arr[mid] < arr[hi].  In either case, this "else"
                # wouldn't have been entered.

        return False

"""
Solution 1b: same as sol 1, but move the checks of target vs the ends to
go with checking vs mid.
"""
class Solution1b:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if target in (arr[lo], arr[mid], arr[hi]):
                return True
            
            if arr[lo] < arr[mid]: # left side is sorted; must be strict >
                if arr[lo] <= target < arr[mid]: # target on left side
                    lo += 1
                    hi = mid - 1
                else: # target on right side
                    lo = mid + 1
                    hi -= 1

            elif arr[mid] < arr[hi]: # right side is sorted; must be strict <
                if arr[mid] < target <= arr[hi]: # target on right side
                    lo = mid + 1
                    hi -= 1
                else: # target on left side
                    lo += 1
                    hi = mid - 1

            else:
                # There are duplicates from lo to mid, or from mid to hi.
                # Can't tell which side target is on, but know it's not at
                # lo, mid, or hi.
                lo += 1
                hi -= 1

        return False

###############################################################################
"""
Solution 2: same as for LC33, but at start of loop, skip all duplicates of 
arr[lo] on left side, and skip all duplicates of arr[hi] on right side.
Do skips only while lo < hi.

After checking if arr[mid] == target, be careful of case lo == mid.
Want lo = mid + 1 because we want to exclude mid.

O(n) time: in case of all or nearly all duplicates
O(1) extra space
"""
class Solution2:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            # skip duplicates of arr[lo] on left side, while lo < hi
            while lo < hi and arr[lo] == arr[lo + 1]:
                lo += 1

            # skip duplicates of arr[hi] on right side, while lo < hi
            while lo < hi and arr[hi] == arr[hi - 1]:
                hi -= 1

            # rest of loop is like for LC33
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return True

            # must be inclusive <= here: if lo == mid, want lo = mid + 1
            if arr[lo] <= arr[mid]: # subarray from lo to mid is sorted
                if arr[lo] <= target < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            else: # arr[mid] <= arr[hi], subarray from mid to hi is sorted
                if arr[mid] < target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        # target not found
        return False # return -1

###############################################################################
"""
Solution 3: same as for LC33, but skip all duplicates of arr[mid] on both sides
when arr[mid] != target.

If arr[lo] == arr[mid] != target, then we don't know if the left or right
part of the array is filled with duplicates of arr[lo] == arr[high].
We can reduce the search space by skipping all the duplicates of arr[mid]
on both sides.

O(n) time: in case of all or nearly all duplicates
O(1) extra space
"""
class Solution3:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return True

            # Skip duplicates on both sides up to mid.
            # If needed, more of the same duplicates will be skipped in
            # succeeding iterations.
            while lo < mid and arr[lo] == arr[mid]:
                lo += 1

            while hi > mid and arr[hi] == arr[mid]:
                hi -= 1

            if lo == mid: # might be more duplicates on left
                lo = mid + 1
                continue
            
            if hi == mid: # might be more duplicates on right
                hi = mid - 1
                continue

            if arr[lo] < arr[mid]: # subarray from lo to mid is sorted
                if arr[lo] <= target < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            else: # arr[mid] <= arr[hi], subarray from mid to hi is sorted
                if arr[mid] < target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        # target not found
        return False # return -1

###############################################################################
"""
Solution 3b: same as for LC33, but skip all duplicates of arr[mid] on *left* 
side when arr[mid] != target.

If arr[lo] == arr[mid] != target, then we don't know if the left or right
part of the array is filled with duplicates of arr[lo] == arr[high].
We can reduce the search space by skipping all the duplicates on the *left*
side.

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/28195/Python-easy-to-understand-solution-(with-comments).

O(n) time: in case of all or nearly all duplicates
O(1) extra space
"""
class Solution3b:
    def search(self, arr: List[int], target: int) -> int:

        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return True

            # Skip duplicates on left side up to mid.
            # If needed, more of the same duplicates will be skipped in
            # succeeding iterations.
            while lo < mid and arr[lo] == arr[mid]:
                lo += 1

            # If lo == mid, then there might be more of the same duplicates,
            # and since we know arr[mid] != target, we want lo = mid + 1.

            if arr[lo] <= arr[mid]: # subarray from lo to mid is sorted
                if arr[lo] <= target < arr[mid]: # fails if more of same duplicates
                    hi = mid - 1
                else:
                    lo = mid + 1 # in particular, if more of same duplicates still on left
            
            else: # arr[mid] <= arr[hi], subarray from mid to hi is sorted
                if arr[mid] < target <= arr[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        
        # target not found
        return False # return -1

###############################################################################
"""
Solution 3c: same as for LC33, but skip all duplicates of arr[mid] on *right*
side when arr[mid] != target.

This is the *right* side version of sol 2.

If arr[lo] == arr[mid] != target, then we don't know if the left or right
part of the array is filled with duplicates of arr[lo] == arr[high].
We can reduce the search space by skipping all the duplicates on the *right*
side.
"""
class Solution3c:
    def search(self, arr: List[int], target: int) -> int:
        lo = 0
        hi = len(arr) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return True

            # Skip duplicates on right side up to mid.
            while hi > mid and arr[hi] == arr[mid]:
                hi -= 1

            # If hi == mid, then there might be more of the same duplicates
            # and since we know arr[mid] != target, we want hi = mid - 1.

            if arr[mid] <= arr[hi]: # subarray from mid to hi is sorted
                if arr[mid] < target <= arr[hi]: # fails if more of same duplicates
                    lo = mid + 1
                else:
                    hi = mid - 1 # in particular, if more of same duplicates still on right
            
            else: # arr[mid] > arr[hi], subarray from lo to mid is sorted
                if arr[lo] <= target < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        
        # target not found
        return False # return -1


###############################################################################
"""
Solution 4: find rotation index using linear scan of value drop.  Then do
usual binary search using (mid + rot) % n.
"""
class Solution4:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # First, find rotation index using linear scan for value drop.
        # If there is no value drop, then rot = 0.
        rot = 0
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                rot = i
        
        # Usual binary search on sorted array.
        lo = 0
        hi = n - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            # index of where actual middle value is
            real_mid = (mid + rot) % n

            if arr[real_mid] == target:
                return True
            elif arr[real_mid] < target:
                lo = mid + 1
            else: # arr[real_mid] > target
                hi = mid - 1

        # target not found
        return False

"""
Solution 4b: find rotation index using linear scan of value drop.  Then use
rotation index to determine which side to do usual binary search on
(sides split by rot, not mid).
"""
class Solution4b:
    def search(self, arr: List[int], target: int) -> int:
        if not arr:
            return False

        n = len(arr)

        # First, find rotation index using linear scan for value drop.
        # If there is no value drop, then rot = 0.
        rot = 0
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                rot = i
        
        # Use rotation index to adjust indices for sorted subarray.
        # The subarray from rot to hi is sorted, and the subarray from
        # lo to rot-1 (if rot-1 >= lo) is sorted.  Subarrays split by
        # rot, not mid.
        lo = 0
        hi = n - 1
        if arr[rot] <= target <= arr[hi]: # search in right subarray
            lo = rot
        else: # search in left subarray
            hi = rot - 1

        # Do usual binary search on sorted subarray.
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                lo = mid + 1
            else: # arr[real_mid] > target
                hi = mid - 1

        # target not found
        return False

###############################################################################
"""
Solution 5: iterative.  Use set to remove duplicates, then do modified binary
search in any of the ways done for LC33.  

This solution is simple, and still O(n) like the others (can't be better),
but uses O(n) space instead of O(1) space.

O(n) time: for removing duplicates, which dominates O(log n) of bsearch.
O(n) extra space: for using set to remove duplicates.
"""
class Solution5:
    def search(self, arr: List[int], target: int) -> int:
        arr = list(set(arr))

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return True # return mid
            
            if arr[left] <= arr[mid]: # subarray from left to mid is sorted
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else: # arr[mid] <= arr[right], subarray from mid to right is sorted
                #if arr[mid + 1] <= target <= arr[right]:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # target not found
        return False # return -1

###############################################################################

if __name__ == "__main__":
    def test(arr, target, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)
        print(f"\ntarget = {target}")

        res = sol.search(arr, target)

        print(f"\nres = {res}")

    # Only update lo or hi with mid if sure a side is sorted;
    # otherwise, check target vs both ends.
    sol = Solution() 
    sol = Solution1b() # same, but check target vs lo, mid, and hi at start of loop

    #sol = Solution2() # skip all duplicates of arr[lo] on left, of arr[hi] on right
    
    #sol = Solution3() # skip all duplicates of arr[mid] on both sides
    #sol = Solution3b() # skip all duplicates of arr[mid] on left side
    #sol = Solution3c() # skip all duplicates of arr[mid] on right side
    
    # To find rotation index in case of duplicates, do a linear scan for
    # value drop (rather than binary search).
    sol = Solution4() # find rotation index, then do bsearch with (mid + rot) % n
    sol = Solution4b() # use rotation index to find which side to do bsearch on

    #sol = Solution5() # iterative; use set to remove all duplicates first

    comment = "LC ex1; answer = True"
    arr = [2,5,6,0,0,1,2]
    target = 0
    test(arr, target, comment)

    comment = "LC ex2; answer = False"
    arr = [2,5,6,0,0,1,2]
    target = 3
    test(arr, target, comment)

    comment = "LC test case; answer = True"
    arr = [1,3,1,1,1]
    target = 3
    test(arr, target, comment)

    comment = "; answer = True"
    arr = [1,1,1,3,1]
    target = 3
    test(arr, target, comment)

    comment = "LC test case; answer = True"
    arr = [3,1]
    target = 1
    test(arr, target, comment)

    comment = "LC test case; answer = False"
    arr = [2,5,6,0,0,1,2]
    target = 3
    test(arr, target, comment)

    comment = "sorted array with duplicates, not rotated; answer = True"
    arr = [2,2,3,3,5,5,5,5,8,13,13,21,21,21,21]
    target = 13 # also check 1, 2, 4, 21, 22
    test(arr, target, comment)

    comment = "answer = True"
    arr = [5,5]
    target = 5
    test(arr, target, comment)

    comment = "answer = False"
    arr = [5]
    target = 4
    test(arr, target, comment)

    comment = "trivial case; answer = False"
    arr = []
    target = 5
    test(arr, target, comment)
