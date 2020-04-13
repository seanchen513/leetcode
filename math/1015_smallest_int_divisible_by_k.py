"""
1015. Smallest Integer Divisible by K
Medium

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.

Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.

Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
 
Note:

1 <= K <= 10^5
"""

###############################################################################
"""
Solution: brute force, generating trial n's with n = 10 * n + 1.

n is always odd, ie, n can never be a multiple of 2.
n can never be a multiple of 5, since those end in 0 or 5.

ie, to have an answer, the last digit of k must be 1, 3, 7, or 9.

Runtime: 1972 ms, faster than 26.74% of Python3 online submissions
Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions
"""
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        n = 1
        
        while n % k != 0:
            n = n * 10 + 1
        
        return len(str(n))
            

"""
Solution: same, but avoid large ints (int overflow in other languages) 
by working with mods.

Not needed for code:

Look at the first k expressions:

1 % k, 11 % k, 111 % k, ..., 11..1 % k (k number of 1's).

The first one equal to 0 corresponds to the answer.
If none are 0, then we have k values in [1, ..., k-1].
By pigeonhole principle, there are two equal values.
In this case, we get a cycle (with the pattern of expressions continuing).
This only happens if k is divisible by 2 or 5.

Runtime: 32 ms, faster than 97.09% of Python3 online submissions
Memory Usage: 13.8 MB, less than 20.00% of Python3 online submissions
"""            
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        mod = 0
        length = 1
        
        while 1:
            mod = (mod * 10 + 1) % k
            if mod == 0:
                return length

            length += 1
        
        return length
            