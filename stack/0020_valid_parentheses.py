"""
20. Valid Parentheses
Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
"""

###############################################################################
"""
Solution: use stack.

Be careful to check if stack is empty before popping from it.
Be careful to check if stack is nonempty at end.

O(n) time
O(n) extra space
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"(": ")", "[": "]", "{": "}"}

        for ch in s:
            if ch in ("(", "[", "{"):
                stack.append(ch)
            
            elif ch in (")", "]", "}"):
                if not stack:
                    return False

                ch2 = stack.pop()
                if ch != match[ch2]:
                    return False

        if stack:
            return False

        return True

###############################################################################
"""
Example of how simple recursion does NOT work.
Counterexamples: "()[]" or "()[]{}".
"""
class SolutionNOT:
    def isValid(self, s: str) -> bool:
        def rec(start, end):
            if start > end:
                return True

            if s[start] in match and match[s[start]] == s[end]:
                return rec(start + 1, end - 1)

            return False

        if len(s) % 2 == 1:
            return False
        
        match = {"(": ")", "[": "]", "{": "}"}
        
        return rec(0, len(s)-1)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment, "\n")

        print(s)

        res = sol.isValid(s)
        print(f"\nSolution: {res}\n")


    sol = Solution() # use stack
    #sol = SolutionNOT() # simple recursion does NOT work

    comment = "LC ex1: answer = True"
    s = "()"
    test(s, comment)

    comment = "LC ex2: answer = True"
    s = "()[]{}"
    test(s, comment)

    comment = "LC ex3; answer = False"
    s = "(]"
    test(s, comment)

    comment = "LC ex4; answer = False"
    s = "([)]"
    test(s, comment)
    
    comment = "LC ex5; answer = True"
    s = "{[]}"
    test(s, comment)
    
    comment = "LC test case; answer = False"
    s = "]"
    test(s, comment)

    comment = "Empty string; answer = True"
    s = ""
    test(s, comment)
