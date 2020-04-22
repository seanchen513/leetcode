"""
686. Repeated String Match
Easy

Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

###############################################################################
"""
Solution: same as sol 2, but also use idea of min number of repeats.

len(k * A) >= len(B)
k * len(A) >= len(B)
k >= len(B) / len(A)
k >= ceil(len(B) / len(A))

k >= (len(B) - 1) // len(A) + 1

So the min number of repeats the right expression, which happens to be
one less than the max number of repeats.

min repeats: length of repeat big enough to hold B, with B starting at
first index.

max repeats: length of repeat big enough to hold B, with B starting at
last index of first repeat.

"""
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        min_repeats = (len(B) - 1) // len(A) + 1
        #max_repeats = min_repeats + 1
        #max_repeats = (len(A) + len(B) - 1) // len(A) + 1

        s = A * min_repeats

        if B in s:
            return min_repeats

        if B in s + A:
            return 1 + min_repeats # max_repeats

        return -1

###############################################################################
"""
Solution 2: 

If B is a substring of some repeat of A, then every char in B must be a char
in A. In particular, the first char of B must be in A, and the greatest index
it can be at is len(A)-1. If we look at B in A repeated enough times, then the
corresponding index that the last char of B is at is 
(len(A)-1) + (len(B)-1) = len(A) + len(B) - 2.

So we want to check if B is in repeats of A, up until the length of the repeat
is at least len(A) + len(B) - 1.

The max number of repeats is
(len(A) + len(B) - 1) // len(A) + 1

Example:
len(A) = 4
len(B) = 8

First char of B appears in A at greatest index len(A)-1 = 3.
Corresponding index of last char of B is 3 + len(B) - 1 = 3+8-1 = 10.
This requires the repeat to have length >= 11.
The max number of repeats is 11 // 4 + 1 = 3.

0123 4567 8901  index
abcd abcd abcd  A
1234 5678       B ordinals
 123 4567 8
  12 3456 78
   1 2345 678

"""
class Solution2:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        n_repeat = 1
        s = A # repeat of A

        max_repeats = (len(A) + len(B) - 1) // len(A) + 1

        while n_repeat <= max_repeats:
            if B in s:
                return n_repeat
            
            s += A
            n_repeat += 1
            
        return -1

###############################################################################

if __name__ == "__main__":
    def test(arr, w, comment=None):       
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        print(f"t = {t}")
        
        res = sol.repeatedStringMatch(s, t)

        print(f"\nresult = {res}\n")


    sol = Solution() # make use of min repeats and max repeats
    #sol = Solution2() # make use of max repeats
 
    comment = "LC ex1; answer = 3"
    s = "abcd"
    t = "cdabcdab"
    test(s, t, comment)
    
    comment = "LC TC; answer = 4"
    s = "abc"
    t = "cabcabca"
    test(s, t, comment)

    comment = "LC TC; answer = -1"
    s = "babbbaabb"
    t = "babbbaabbbabbbbaabbbabbbbaabbbabbbbaabbbabbbbaabbbabbbbaabbbabbbbaabbbabbbbaabbbabbbbaabbbabbbbaabb"
    test(s, t, comment)
    
    comment = "LC TC; answer = 1"
    s = "aa"
    t = "a"
    test(s, t, comment)

    comment = "LC TC; answer = 2"
    s = "aaaaaaaaaaaaaaaaaaaaaab"
    t = "ba"
    test(s, t, comment)

    comment = "LC TC; answer = -1"
    s = "abcabcabcabc"
    t = "abac"
    test(s, t, comment)
    