"""
775. Global and Local Inversions
Medium

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
Example 2:

Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
"""
###############################################################################

from typing import List

"""
Example: sorted array has no inversions (local or global).  So return True.

Example:
n = 5, reverse sorted
[4,3,2,1,0]
local inversions = n - 1 = 4
global inversions = n(n-1)/2 = 4 + 3 + 2 + 1 = 10
In general, these are equal if n = 2.

Note that 0 is 3 positions away from its sorted position.
1 - 2
2 - 0
3 - 2
4 - 3
(Total is 10, the same as the number of global inversions is a coincidence).
Note that the values 2 and 3 are > 1.

Example: [1,0,2]
local inversions = 1
global inversions = 1

Number of positions away from sorted position:
0 - 1
1 - 1
2 - 0

Note that the values 0 and 1 are <= 1.
"""

###############################################################################
"""
Solution 1: there are no global inversions if every value is at most 1
position away from its position in an ideal permutation, ie, if
abs(arr[i] - i) <= 1 for all i in range(n).

Consider 0.  If 0 occurs at i >= 2, then arr[0] > arr[i] is a global inversion.
So 0 must occur at index 0 or 1.  If arr[1] = 0, then arr[0] = 1, otherwise
arr[0] > arr[j] = 1 for j >= 2 is a global inversion.

So the two possibilities are:
arr = [0] + (ideal permutation of 1, ..., n-1)
arr = [1, 0] + (ideal permutation of 2, ..., n-1)

Repeating the argument...

O(n) time
O(1) extra space
"""
class Solution:
    def isIdealPermutation(self, arr: List[int]) -> bool:
        n = len(arr)

        # n_local = sum(arr[i] > arr[i+1] for i in range(n-1))
        # n_global = sum(abs(arr[i] - i) for i in range(n))

        # return n_local == n_global

        return all(abs(arr[i] - i) <= 1 for i in range(n))


###############################################################################
"""
Solution 2: Linear scan forward, tracking max.

arr[j] < arr[i] for any i=0,...,j-2 then return False
arr[j] < max(arr[i] for i=0,...,j-2)

O(n) time
O(1) extra space
"""
class Solution2:
    def isIdealPermutation(self, arr: List[int]) -> bool:
        n = len(arr)
        mx = 0

        for j in range(n-2):
            mx = max(mx, arr[j])

            if arr[j+2] < mx:
                return False

        return True

"""
Solution 2b: Linear scan in reverse, tracking min.

arr[j] < arr[i] for any j=i+2,...,n-1 then return False
arr[i] > min(arr[j] for j=i+2,...,n-1)

See approach 2 here:
https://leetcode.com/problems/global-and-local-inversions/solution/
"""
class Solution2b:
    def isIdealPermutation(self, arr: List[int]) -> bool:
        n = len(arr)
        min_val = n-1

        for i in range(n-1, 1, -1):
            min_val = min(min_val, arr[i])

            if arr[i-2] > min_val:
                return False

        return True

###############################################################################
"""
Solution 3:

Every local inversion is a global inversion.  So they are equal if there
are no global inversions that are local inversions.

O(n^2) time
O(1) extra space

See approach 3 here:
https://leetcode.com/problems/global-and-local-inversions/solution/

TLE
"""
class Solution3:
    def isIdealPermutation(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n-1):
            for j in range(i+2, n):
                if arr[i] > arr[j]:
                    return False

        return True

###############################################################################
"""
Solution 4: brute force

O(n^2) time
O(1) extra space

TLE
"""
class Solution4:
    def isIdealPermutation(self, arr: List[int]) -> bool:
        n = len(arr)
        n_local = 0
        n_global = 0

        for i in range(n-1):
            if arr[i+1] < arr[i]:
                n_local += 1

            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    n_global += 1

        print(f"local = {n_local}")
        print(f"global = {n_global}")
        return n_local == n_global

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.isIdealPermutation(arr)

        print(f"\nres = {res}")


    sol = Solution() # check abs(arr[i] - i) <= 1 for all i
    #sol = Solution2() # linear scan, tracking max
    #sol = Solution2() # linear scan in reverse, tracking min
    #sol = Solution3() # brute force, return False ASAP
    #sol = Solution4() # brute force

    comment = "LC ex1; answer = True"
    arr = [1,0,2]
    test(arr, comment)
    
    comment = "LC ex2; answer = False"
    arr = [1,2,0]
    test(arr, comment)

    comment = "LC test case; answer = True"
    arr = [0,1]
    test(arr, comment)

    comment = "reverse sorted, n = 5; answer = False"    
    arr = [4,3,2,1,0]
    test(arr, comment)

    comment = "sorted, n = 5; answer = True"
    arr = [0,1,2,3,4]
    test(arr, comment)

#arr = [2,4,3,5,1]
