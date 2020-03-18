"""
189. Rotate Array
Easy

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

from typing import List

###############################################################################
"""
Solution: look at partitions of array into cycles, and do rotate within
each cycle.

Example:
1 2 3 4 5 6 7 8
n = 8, k = 3
(1 4 7 2 5 8 3 6)

Example:
n = 8, k = 2
(1 3 5 7)
(2 4 6 8)

Example:
1 2 3 4 5 6 7 8 9 10 11 12
n = 12, k = 8
(1 9 5)
(2 10 6)
(3 11 7)
(4 12 8)

gcd = 4 = number of cycles
n / gcd = 3 = length of each cycle

O(n) time
O(1) extra space

Runtime: 56 ms, faster than 93.60% of Python3 online submissions
Memory Usage: 14.3 MB, less than 5.09% of Python3 online submissions
"""
class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # O(h), where h = number of digits in smaller number
        # ie, O(log(min(a,b)))
        def gcd(a, b):
            while b:
                a, b = b, a % b            
            return a

        n = len(arr)
        k = k % n
        
        if k == 0 or n == 1:
            return

        n_cycles = gcd(n, k)
        len_cycle = n // n_cycles

        for i in range(n_cycles):
            temp = arr[i]
            j = i

            for _ in range(len_cycle-1):
                j_dec = (j - k) % n
                arr[j] = arr[j_dec]
                j = j_dec

            arr[j] = temp

###############################################################################
"""
Solution 2: reverse list, then reverse two sublists (first k elements, and
then last n-k elements).

Alternatively, can reverse the sublists first, then reverse the entire list.

Example:
n = 7, k = 3
1 2 3 - 4 5 6 7
7 6 5 - 4 3 2 1
5 6 7 - 1 2 3 4

O(n) time
O(1) extra space
"""
class Solution2:
    def rotate(self, arr: List[int], k: int) -> None:
        def rev(start, end): # inclusive
            # mid = (end - start + 1) // 2
            # for i in range(mid):
            #     arr[start + i], arr[end - i] = arr[end - i], arr[start + i]

            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(arr)
        k %= n

        rev(0, n-1) # or arr.reverse()
        rev(0, k-1)
        rev(k, n-1)

###############################################################################
"""
Solution 3: use array slicing

n = 7
k = 3
n-k = 4
0 1 2 - 3 4 5 6     indices
1 2 3 - 4 5 6 7     orig array
5 6 7 - 1 2 3 4     rotated array

O(n) time
O(n) extra space
"""
class Solution3:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        arr[:k], arr[k:] = arr[n-k:], arr[:n-k]

class Solution3b:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        arr[:] = arr[n-k:] + arr[:n-k]

class Solution3c:
    def rotate(self, arr: List[int], k: int) -> None:
        k %= len(arr)
        arr[:] = arr[-k:] + arr[:-k]

###############################################################################
"""
Solution 4: make copy of array, and copy values from it into given array
in their rotated positions.

O(n) time
O(n) extra space
"""
class Solution4:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)
        k %= n

        orig = arr[:]

        for i in range(k, n):
            arr[i] = orig[i - k]

        m = n - k
        for i in range(k):
            arr[i] = orig[m + i]

###############################################################################
"""
Solution 5: rotate array to right by one position, and repeat this k times.

O(nk) time
O(1) extra space

TLE
"""
class Solution5:
    def rotate(self, arr: List[int], k: int) -> None:
        n = len(arr)

        for _ in range(k):
            temp = arr[-1]

            for i in range(n-1, 0, -1):
                arr[i] = arr[i-1]

            arr[0] = temp

###############################################################################

if __name__ == "__main__":
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)
        print(f"k = {k}")

        sol.rotate(arr, k)

        # print(f"\nres = {res}\n")
        print()
        print(arr)


    sol = Solution() # partition array into cycles, and rotate within each cycle
    
    #sol = Solution2() # reverse list, then reverse two sublists
    
    #sol = Solution3() # use array slicing
    #sol = Solution3b()
    #sol = Solution3c()

    #sol = Solution4() # make copy of array; copy from it to rotated positions
    #sol = Solution5() # rotate by 1 position, and repeat k times
    
    comment = "LC ex1; answer = [5,6,7,1,2,3,4]"
    arr = [1,2,3,4,5,6,7]
    k = 3
    test(arr, k, comment)

    comment = "LC ex2; answer = [3,99,-1,-100]"
    arr = [-1,-100,3,99]
    k = 2
    test(arr, k, comment)

    comment = "answer = [5,6,7,8,9,10,11,12,1,2,3,4]"
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    k = 8
    test(arr, k, comment)

    comment = "LC test case; answer = [1]"
    arr = [1]
    k = 0
    test(arr, k, comment)

    comment = "LC test case; answer = [1]"
    arr = [1]
    k = 1
    test(arr, k, comment)

    comment = "LC test case; answer = [1,2]"
    arr = [1,2]
    k = 2
    test(arr, k, comment)
