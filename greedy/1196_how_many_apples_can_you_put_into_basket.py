"""
1196. How Many Apples Can You Put into the Basket
Easy

You have some apples, where arr[i] is the weight of the i-th apple.  You also have a basket that can carry up to 5000 units of weight.

Return the maximum number of apples you can put in the basket.

Example 1:

Input: arr = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.

Example 2:

Input: arr = [900,950,800,1000,700,800]
Output: 5
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.
 
Constraints:

1 <= arr.length <= 10^3
1 <= arr[i] <= 10^3
"""

from typing import List

###############################################################################

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        s = 0

        for i, wt in enumerate(sorted(arr)):
            s += wt

            if s > 5000:
                return i
        
        # We took all the applies, so now i = len(arr) - 1 (last index).
        return i + 1
            
###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        res = sol.maxNumberOfApples(arr)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = 4"
    arr = [100,200,150,1000]
    test(arr, comment)

    comment = "LC ex2; answer = 5"
    arr = [900,950,800,1000,700,800]
    test(arr, comment)
