"""
1375. Bulb Switcher III
Medium

There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.

Example 1:

Input: light = [2,1,3,5,4]
Output: 3
Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.

Example 2:

Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).

Example 3:

Input: light = [4,1,2,3]
Output: 1
Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
Bulb 4th changes to blue at the moment 3.

Example 4:

Input: light = [2,1,4,3,6,5]
Output: 3

Example 5:

Input: light = [1,2,3,4,5,6]
Output: 6
 
Constraints:

n == light.length
1 <= n <= 5 * 10^4
light is a permutation of  [1, 2, ..., n]
"""

from typing import List

###############################################################################
"""
Solution 1: Iterate array and keep track of max.

Note: Only need to keep track of max.  Don't need to keep track of min.
"""
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        mx = 0
        count = 0
        
        for i, val in enumerate(light, 1):
            mx = max(mx, val)
            
            if mx == i:
                count += 1
                
        return count

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.numTimesAllBlue(arr)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = 3"
    arr = [2,1,3,5,4]
    test(arr, comment)
    
    comment = "LC ex2; answer = 2"
    arr = [3,2,4,1,5]
    test(arr, comment)

    comment = "LC ex3; answer = 1"
    arr = [4,1,2,3]
    test(arr, comment)
    
    comment = "LC ex4; answer = 3"
    arr = [2,1,4,3,6,5]
    test(arr, comment)
    
    comment = "LC ex5; answer = 6"
    arr = [1,2,3,4,5,6]
    test(arr, comment)
    