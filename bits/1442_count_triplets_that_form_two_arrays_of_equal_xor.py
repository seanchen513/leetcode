"""
1442. Count Triplets That Can Form Two Arrays of Equal XOR
Medium

Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:

Input: arr = [1,1,1,1,1]
Output: 10

Example 3:

Input: arr = [2,3]
Output: 0

Example 4:

Input: arr = [1,3,5,7,9]
Output: 3

Example 5:

Input: arr = [7,11,12,9,5,2,7,17,22]
Output: 8
 
Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 10^8
"""

from typing import List
import collections

###############################################################################
"""
Solution: precompute xor prefixes. Use dict to count xor values. Use "total"
dict that maps xor value to sum of indices; this makes it easy to subtract
all previous indices with same xor value.

Based on Solution 4 here:
https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/discuss/623747/JavaC%2B%2BPython-One-Pass-O(N4)-to-O(N)

* Expand on examples later.

#############
LC example 1:

2 3 1 6 7
  i j k

xor prefixes:
(0) 2 1 0 6 1

matching xor's:
0, 0: diff in indices = 3, len(subarray) = 3, # partitions = 2
1, 1: diff in indices = 3, len(subarray) = 3, # partitions = 2

#############
LC example 2:
1 1 1 1 1

xor prefixes:
(0) 1 0 1 0 1

matching xor's:
0: diffs = 2, 2, 4
1: diffs = 2, 2, 4

count diffs = 6
sum diffs = 16
answer = 16 - 6 = 10

#############
LC example 5:
7 11 12 9 5 2 7 17 22

xor prefixes:
(0) 7 12 0 9 12 14 9 24 14

matching xor's:
0: diff = 3
12: diff = 3
9: diff = 3
14: diff = 3


O(n) time
O(n) extra space: for "d" and "total" dicts
O(1) extra space if overwrite input list with xor values.

Possible to make it a one-pass solution...

Runtime: 32 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0

        # prefix XOR's of arr
        # dummy value of 0 at index 0
        xor = [0] * (n+1)

        for i in range(n):
            xor[i+1] = xor[i] ^ arr[i]

        d = collections.Counter()
        total = collections.Counter() 

        for i in range(n+1):
            x = xor[i]

            # There are d[x] subarrays ending at current index.
            # Each has (i - 1 - previous index) partitions.
            # Total partitions is d[x] * (i-1) - sum of previous indices.
            count += d[x] * (i-1) - total[x]

            d[x] += 1
            total[x] += i

        return count

"""
LC example 1:

2 3 1 6 7
  i j k

xor prefixes:
(0) 2 1 0 6 1

i = 0
x = 0   d[0] = 0    total[0] = 0
count += 0 * (0-1) - 0, so count += 0, so count = 0

        d[0] = 1    total[0] = 0

i = 1
x = 2   d[2] = 0    total[2] = 0
count += 0 * (1-1) - 0, so count += 0, so count = 0

        d[2] = 1    total[2] = 1

i = 2
x = 1   d[1] = 0    total[1] = 0
count += 0 * (2-1) - 0, so count += 0, so count = 0

        d[1] = 1    total[1] = 2

i = 3
x = 0   d[0] = 1    total[0] = 0
count += 1 * (3-1) - 0, so count += 2, so count = 2

        d[0] = 2    total[0] = 3

i = 4
x = 6   d[6] = 0    total[6] = 0
count += 0 * (4-1) - 0, so count += 0, so count = 2

        d[6] = 1    total[6] = 4

i = 5
x = 1   d[1] = 1    total[1] = 2
count += 1 * (5-1) - 2, so count += 2, so count = 4

"""



###############################################################################
"""
Solution 2: use fact that if a == b iff a ^ b == 0. 
Look at all subarrays of length >= 2 with xor 0. 
Every partition of such a subarray satisfies our condition. 
A subarray with length k can be partitioned into 2 subarrays in k-1 ways.

This version precomputes a xor array.
Note: subarray from i..k has xor 0 iff xor[k] == xor[i-1].
Pro: don't have to do a XOR operation O(n^2) times.
Instead, precalculating the xor array takes O(n) time.
Cons: takes O(n) space instead of O(1). Extra subtraction when incrementing count.

a == b 
a ^ a == a ^ b
0 == a ^ b

LC example 1:

2 3 1 6 7
  i j k

prefix:
(0) 2 1 0 6 1

matching XOR's:
0, 0: diff in indices = 3, len(subarray) = 3, # partitions = 2
1, 1: diff in indices = 3, len(subarray) = 3, # partitions = 2

2 = 3 ^ 1
2 ^ 3 = 1

1 = 6 ^ 7
1 ^ 5 = 7

Subarray [2,3,1] has xor 0. It can be partitioned in len-1 = 2 ways.
Subarray [1,6,7] has xor 0. It can be partitioned in len-1 = 2 ways.

//

a ~ i..j-1 ~ 0..j-1 ^ 0..i-1 = xor[j-1] ^ xor[i-1]
b ~ j..k ~ 0..k ^ 0..j-1 = xor[k] ^ xor[j]

O(n^2) time
O(n) extra space: for xor array

Runtime: 48 ms, faster than 85.71% of Python3 online submissions
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions
"""
class Solution2:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0

        # prefix XOR's of arr
        # dummy value of 0 at index 0
        xor = [0] * (n+1)

        for i in range(n):
            xor[i+1] = xor[i] ^ arr[i]

        for i in range(n-1): # 0 .. n-2
            x = xor[i]

            for j in range(i+2, n+1): # start at i+2, so subarray has length >= 2
                #if xor[j] ^ xor[i] == 0:

                if xor[j] == x: # subarray from i+1..j has xor 0 iff xor[j] == xor[i].
                    # length of subarray is j - (i+1) - 1 = j - i
                    count += j - i - 1

        return count

"""
Solution 2b: same, but don't use prefix XOR's.

O(n^2) time
O(1) extra space

Runtime: 56 ms, faster than 85.71% of Python3 online submissions
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution2b:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0

        for i in range(n):
            a = arr[i]

            for j in range(i+1, n): 
                a ^= arr[j]

                if a == 0:
                    count += j - i

        return count

###############################################################################
"""
Solution 3: brute force

O(n^3) time
O(1) extra space

Runtime: 2348 ms, faster than 71.43% of Python3 online submissions
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions
"""
class Solution3:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0

        for i in range(n):
            a = 0

            for j1 in range(i, n): # j - 1
                a ^= arr[j1]
                b = 0

                for k in range(j1+1, n):
                    b ^= arr[k]

                    if a == b:
                        count += 1

        return count

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr={arr}")

        res = sol.countTriplets(arr)

        print(f"\nres = {res}\n")

    sol = Solution() #

    #sol = Solution2() # look at subarrays of len >= 2 with xor 0
    #sol = Solution2b() # same, but don't use xor prefix array

    #sol = Solution3() # brute force

    comment = "LC ex1; answer = 4"
    arr = [2,3,1,6,7]
    test(arr, comment)

    comment = "LC ex2; answer = 10"
    arr = [1,1,1,1,1]
    test(arr, comment)

    comment = "LC ex3; answer = 0"
    arr = [2,3]
    test(arr, comment)

    comment = "LC ex4; answer = 3"
    arr = [1,3,5,7,9]
    test(arr, comment)
    
    comment = "LC ex5; answer = 8"
    arr = [7,11,12,9,5,2,7,17,22]
    test(arr, comment)
    