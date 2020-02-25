"""
268. Missing Number
Easy

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

from typing import List

###############################################################################
"""
Solution 1: use math.

O(n) time
O(1) extra space
"""
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        return n*(n+1)//2 - sum(arr)


###############################################################################
"""
Solution 2: use bit manipulation.

Start with n, and XOR it with every index and value.

If n itself is missing, then arr[i] = i for all i, so all indices and
values cancel out via XOR.

If some other number is missing, say arr[i] = n, then all other numbers
cancel out except n ^ (i ^ n) = i.

O(n) time
O(1) extra space
"""
class Solution2:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        for i, x in enumerate(arr):
            n ^= i ^ x

        return n

###############################################################################
"""
Solution 3: attempt cyclic sort.

Only swap values if current value isn't n.
Don't increment if swap happens.
Afterwards, if every index matches its value, then missing number is n.
Otherwise, the first index that doesn't match its value (which will be n) 
is the missing number.

https://leetcode.com/problems/missing-number/discuss/450090/Cyclic-Sort

O(n) time
O(1) extra space
"""
class Solution3:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)

        i = 0
        while i < n:
            x = arr[i]

            if x != i and x != n:
                arr[x], arr[i] = arr[i], arr[x] # swap so arr[x] == x
            else:
                i += 1

        for i, x in enumerate(arr):
            if i != x:
               return i

        return n

"""
LC example 1:
0 1 2
3 0 1

i = 0: don't do anythhing, n found

i = 1
0 1 2
0 3 1

i = 2
0 1 2*
0 1 3

n=3 in array, but 2 isn't.
"""

"""
LC example 2:
0 1 2 3 4 5 6 7 8
9 6 4 2 3 5 7 0 1

i = 0: don't do anything, n=9 found

i = 1
0 1 2 3 4 5 6 7 8
9 7 4 2 3 5 6 0 1
9 0 4 2 3 5 6 7 1
0 9 4 2 3 5 6 7 1

i = 2
0 1 2 3 4 5 6 7 8
0 9 3 2 4 5 6 7 1
0 9 2 3 4 5 6 7 1

i = 3,4,5,6,7: do nothing
0 1 2 3 4 5 6 7 8*
0 1 2 3 4 5 6 7 9

n=9 in array, but 8 isn't.
"""

"""
n = 5
2 is missing

0 1 2 3 4
3 5 4 0 1

i = 0
0 1 2 3 4
0 5 4 3 1

i = 1: do nothing, n=5 found

i = 2
0 1 2 3 4
0 5 1 3 4
0 1 5 3 4

i = 3, 4: do nothing

sorted:
0 1 2* 3 4
0 1 3  4 5
"""

"""
n = 4
0 is missing

0 1 2 3
1 3 2 4

i = 0
0 1 2 3
3 1 2 4
4 1 2 3

i = 1, 2, 3: do nothing

sorted:
0 1 2 3
1 2 3 4
"""
###############################################################################
"""
Solution 4: use set.

O(n) time
O(n) extra space
"""
class Solution4:
    def missingNumber(self, arr: List[int]) -> int:
        s = set( range(len(arr) + 1) )

        for x in arr:
            s.remove(x)

        return s.pop()

###############################################################################
"""
Solution 5: use set subtraction.

O(n) time
O(n) extra space
"""
class Solution5:
    def missingNumber(self, arr: List[int]) -> int:
        return (set( range(len(arr) + 1) ) - set(arr)).pop()

###############################################################################
"""
Solution 5: use sorting.

If n is missing, then in sorted array, every index matches its value.

If n is not missing, then arr[-1] == n.  Some other number i is missing.  
In sorted array, it is the first index that doesn't match its value.

O(n log n) time
O(1) extra space: if use in-place sorting.
"""
class Solution6:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)

        if arr[-1] != n: # or arr[-1] == n - 1
            return n

        for i in range(n):
            if arr[i] != i:
                return i

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.missingNumber(arr)

        print(f"\nres = {res}")


    sol = Solution() # use math
    sol = Solution2() # bit manipulation
    sol = Solution3() # try cyclic sort
    #sol = Solution4() # use set
    #sol = Solution5() # use set subtraction
    #sol = Solution() # use sorting

    comment = "LC ex1; answer = 2"
    arr = [3,0,1]
    test(arr, comment)

    comment = "LC ex2; answer = 8"
    arr = [9,6,4,2,3,5,7,0,1]
    test(arr, comment)
