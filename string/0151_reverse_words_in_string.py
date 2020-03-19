"""
151. Reverse Words in a String
Medium

Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Follow up:
For C programmers, try to solve it in-place in O(1) extra space.
"""

import collections

###############################################################################
"""
Solution: find all words and put in list.  Reverse list, then join.

O(n) time: for looping through string, copying words, and joining words.

O(n) extra space: for copying words from string, and joining words to form
new string to return.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        #s = s.strip() # remove leading and trailing spaces

        n = len(s)
        i = 0
        words = []

        # Skip leading spaces, and find index of first letter of first word.
        while i < n and s[i] == " ":
            i += 1
        start = i

        while i < n:
            # Skip non-spaces and find next space (first space after word).
            while i < n and s[i] != " ":
                i += 1

            words.append(s[start:i])

            # Skip spaces after the word.
            while i < n and s[i] == " ":
                i += 1

            # Index for first letter of new word.
            start = i

        #print(words)
        words.reverse()

        return ' '.join(words)

"""
Solution 1b: same as sol 1, but use built-in string split().

O(n) time
O(n) extra space: for results of split() and join()
"""
class Solution1b:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

###############################################################################
"""
Solution 2: trim spaces, reverse each word while adding letters of string
to list, then reverse list and join.

Avoid using built-in string functions except for join().

O(n) time
O(n) extra space
"""
class Solution2:
    def reverseWords(self, s: str) -> str:
        def rev(start, end):
            while start < end:
                letters[start], letters[end] = letters[end], letters[start]
                start += 1
                end -= 1

        n = len(s)
        i = 0 # index for string s
        letters = []

        while i < n:
            # Skip spaces and find first letter of next word.
            while i < n and s[i] == ' ':
                i += 1

            if i == n:
                break

            start = i

            # Skip non-spaces and find next space (first space after word).
            while i < n and s[i] != ' ':
                i += 1

            end = i - 1 # index for last letter of word

            # Add letters of word in reverse to "letters" list.
            while start <= end:
                letters.append(s[end])
                end -= 1

            # Alternatively, could have added letters in order, then
            # call rev() for word.  But note indices for "letters" different
            # than for "s".

            letters.append(' ')


        if letters:
            letters.pop() # Remove extraneous space at end.
        
        rev(0, len(letters) - 1) # letters.reverse()

        return ''.join(letters)

###############################################################################
"""
Solution 3: trim spaces, push words in front of deque, then join.

O(n) time
O(n) extra space
"""
class Solution3:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        i = 0 # index for string s
        d = collections.deque([])

        while i < n:
            # Skip spaces and find first letter of next word.
            while i < n and s[i] == ' ':
                i += 1

            if i == n:
                break

            # Skip non-spaces and find next space (first space after word).
            word = []
            while i < n and s[i] != ' ':
                word.append(s[i])
                i += 1

            d.appendleft(''.join(word))

        return ' '.join(d)

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\nstring = {s}")

        res = sol.reverseWords(s)

        print(f"\nres = {res}\n")


    sol = Solution() # split string into list of words, reverse list, join list
    sol = Solution1b() # use split() and join()
    
    sol = Solution2() # reverse word while adding letters to list, then reverse list and join
    
    sol = Solution3() # push words in front of deque, then join

    comment = "LC ex1"
    s = "the sky is blue"
    test(s, comment)

    comment = "LC ex2"
    s = "  hello world!  "
    test(s, comment)
    
    comment = "LC ex3"
    s = "a good   example"
    test(s, comment)

    comment = "LC test case; empty string"
    s = ""
    test(s, comment)

    comment = "LC test case; single space"
    s = " "
    test(s, comment)
