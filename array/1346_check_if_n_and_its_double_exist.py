"""
1346. Check If N and Its Double Exist
Easy

Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

Example 2:

Input: arr = [7,1,14,11]
Output: true
Explanation: N = 14 is the double of M = 7,that is, 14 = 2 * 7.

Example 3:

Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.

Constraints:
2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3
"""

from typing import List
import collections

###############################################################################

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()

        for x in arr:
            if x in s:
                return True
            
            s.add(2 * x)
            if x % 2 == 0:
                s.add(x // 2)

        return False

###############################################################################

class Solution2:
  def checkIfExist(self, arr: List[int]) -> bool:
    s = collections.Counter(arr)
    
    if s[0] > 1: 
        return True
    
    for x in arr:
        if s[2 * x] and x != 0:
            return True
    
    return False

###############################################################################

if __name__ == "__main__":
    def test(arr, comment):
        print("="*80)
        if comment:
            print(comment)

        res = s.checkIfExist(arr)

        print(f"\n{arr[:20]}")
        print(f"\nlen(arr) = {len(arr)}")
        if len(arr) > 20:
            print(" (only show at most 20 elements)")

        print(f"\nresult = {res}")

    #s = Solution() # use set
    s = Solution2() # use Counter()

    comment = "LC ex1; answer = True"
    arr = [10,2,5,3]
    test(arr, comment)

    comment = "LC ex2; answer = True"
    arr = [7,1,14,11]
    test(arr, comment)

    comment = "LC ex3; answer = False"
    arr = [3,1,7,11]
    test(arr, comment)
    