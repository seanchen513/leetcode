"""
1441. Build an Array With Stack Operations
Easy

Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]

Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.

Example 4:

Input: target = [2,3,4], n = 4
Output: ["Push","Pop","Push","Push","Push"]

Constraints:

1 <= target.length <= 100
1 <= target[i] <= 100
1 <= n <= 100
target is strictly increasing.
"""

from typing import List

###############################################################################
"""
Solution: iterate x from 1 to n, and use index j to track next value in 
target. "Push" each value x. If x not in target (using target[j] to compare), 
then "pop". Otherwise, it is in target, so just increment j.

O(n) time
O(1) extra space
"""            
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        end = target[-1] + 1
        j = 0
        
        for x in range(1, end):
            res.append("Push")
            
            #if x not in target:
            #    res.append("Pop")
            
            if x != target[j]:
                res.append("Pop")
            else:
                j += 1
            
        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, n, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\narr = {arr}")
        print(f"n = {n}")

        res = sol.buildArray(arr, n)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = 'LC ex1; answer = ["Push","Push","Pop","Push"]'
    arr = [1,3]
    n =3
    test(arr, n, comment)
    
    comment = 'LC ex2; answer = ["Push","Push","Push"]'
    arr = [1,2,3]
    n = 3
    test(arr, n, comment)
    
    comment = 'LC ex3; answer = ["Push","Push"]'
    arr = [1,2] 
    n = 4
    test(arr, n, comment)
    
    comment = 'LC ex4; answer = ["Push","Pop","Push","Push","Push"]'
    arr = [2,3,4]
    n = 4
    test(arr, n, comment)
    
