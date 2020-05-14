"""
402. Remove K Digits
Medium

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""

###############################################################################
"""
Solution: greedy; use increasing stack of digits.

Idea: remove larger digits that are more significant (towards the left).
If k=1, scanning left to right, remove first "peak" digit, ie, digit that is
greater than the next digit.

O(n) time
O(n) extra space: for stack
"""
class Solution:
    def removeKdigits(self, n: str, k: int) -> str:
        ### Don't need this if check for empty stack at end.
        if k >= len(n):
            return "0"

        stack = []
        count = 0

        for ch in n:
            while count < k and stack and ch < stack[-1]:
                stack.pop()
                count += 1

            stack.append(ch)

        # Haven't removed enough digits yet, so remove digits from end.
        while count < k and stack:
            stack.pop()
            count += 1

        ### Don't need this if check k >= len(n) at start
        # if not stack:
        #     return "0"

        return str(int(''.join(stack)))

"""
Solution 1b: same, but break early from loop if count == k.
"""
class Solution1b:
    def removeKdigits(self, n: str, k: int) -> str:
        ### Don't need this if check for empty stack at end.
        if k >= len(n):
            return "0"

        stack = []
        count = 0

        for i, ch in enumerate(n):
            while count < k and stack and ch < stack[-1]:
                stack.pop()
                count += 1

            if count == k:
                stack.extend(n[i:])
                break

            stack.append(ch)

        # Haven't removed enough digits yet, so remove digits from end.
        while count < k and stack:
            stack.pop()
            count += 1

        ### Don't need this if check k >= len(n) at start
        # if not stack:
        #     return "0"

        return str(int(''.join(stack)))

###############################################################################

if __name__ == "__main__":
    def test(n, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        print(f"k = {k}")

        res = sol.removeKdigits(n, k)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution1b() # same, but early break from loop

    comment = "LC ex1; answer = 1219"
    n = "1432219"
    k = 3
    test(n, k, comment)

    comment = "LC ex2; answer = 200"
    n = "10200"
    k = 1
    test(n, k, comment)

    comment = "LC ex3; answer = 0"
    n = "10"
    k = 2
    test(n, k, comment)

    comment = "LC TC; answer = 0"
    n = "9"
    k = 1
    test(n, k, comment)

    comment = "LC TC; answer = 11"
    n = "112"
    k = 1
    test(n, k, comment)
