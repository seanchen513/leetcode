"""
678. Valid Parenthesis String
Medium

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.

An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""

###############################################################################
"""
NOTES:

* can only serve as matching ) for ('s that come before it.
* can only serve as matching ( for )'s that come after it.
Any "()" can be removed.

If len(s) = n, how many *'s do we need to ensure s can always be valid? Half?

Automatic disqualifiers:
( at end
) at start

Any * at end must cancel any immediately preceding (
Any * at start must cancel any immediately following )

Left with string like this if valid:

***( ... )***

"""

###############################################################################
"""
Solution: greedy, forward and reverse traversals.

Traverse L to R: count '*' and '(' as +1. If count reaches negative, return 
False because there is a ')' that cannot be matched (from the left side).

Traverse R to L: count '*' and ')' as -1. If count reaches positive, return 
False because there is a '(' that cannot be matched (from the right side).

O(n) time
O(1) extra space

Runtime: 24 ms, faster than 90.48% of Python3 online submissions
Memory Usage: 14 MB, less than 14.29% of Python3 online submissions
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0

        # This also gives a high count of '('. If count becomes < 0, then
        # current prefix cannot be made valid because of an unmatched ')'.
        for c in s:
            if c == ')':
                count -= 1
            else: # '(' or '*'
                count += 1

            if count < 0:
                return False

        count = 0

        # If count becomes > 0, then current suffix cannot be made valid
        # because of an unmatched '('.
        for c in reversed(s):
            if c == '(':
                count += 1
            else: # ')' or '*'
                count -= 1

            if count > 0:
                return False

        return True

"""
Solution: greedy.

Track possible net balance as we traverse the string.
Going from one char to the next, the net balance can change by -1, 0, or 1.
The range of possible net balance values forms an interval of integers.
We only need to track the min and max (lo and hi) of this interval.

The min balance comes from choosing every '*' to be ')'. This gives the
min number of possible '('.

The max balance comes from choosing every '*' to be '('. This gives the
max number of possible '('. If this max becomes < 0, then there is a ')'
that cannot be matched (from the left).

O(n) time
O(1) extra space

Runtime: 20 ms, faster than 98.16% of Python3 online submissions
Memory Usage: 13.8 MB, less than 14.29% of Python3 online submissions
"""
class Solution1b:
    def checkValidString(self, s: str) -> bool:
        hi = lo = 0

        for c in s:
            if c == ')':
                hi -= 1

                if hi < 0: # found a ')' that cannot be matched (to the left)
                    return False

            else: # '(' or '*'
                hi += 1

            if c == '(':
                lo += 1
            else: # ')' or '*'
                lo -= 1

                if lo < 0: # ??? '(' shouldn't be used to match any '(' appearing after it
                    lo = 0

            #print(f"lo, hi = {lo:2}, {hi:2}")

        return lo == 0

###############################################################################
"""
Solution 2: greedy stack-based validation. Build left parens stack and star 
stack, while matching all ')' first with a previous '(' or '*'. Then, going in
reverse on stacks, match each remaining '(' with a '*' to the right of it.

1. Reduce step is optional.
2. Build stack of indices for left parentheses and stack of indices for stars.
3. Match left parentheses with stars to the right.

O(n) time
O(n) extra space: for stacks

Runtime: 20 ms, faster than 98.16% of Python3 online submissions
Memory Usage: 14 MB, less than 14.29% of Python3 online submissions
"""
class Solution2:
    def checkValidString(self, s: str) -> bool:
        def reduce(s):
            stack = []

            for c in s:
                if c == ')':
                    if not stack:
                        return False
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)

            return stack

        s = reduce(s)
        #if s: print(''.join(s))

        if s is False: # distinguish from []
           return False

        # Build stack of left parentheses and stack of stars.
        parens = []
        stars = []

        for i, c in enumerate(s):
            if c == '*':
                stars.append(i)
            elif c == '(':
                parens.append(i)
            else: # c == ')'
                if parens:
                    parens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

        # Drain each remaining left parenthesis by matching it with a star
        # to the right of it.
        if len(parens) > len(stars):
            return False

        # for i in range(-1, -1-len(parens), -1):
        #     if parens[i] > stars[i]: # use right-most star first
        #         return False

        for i, j in zip(reversed(parens), reversed(stars)):
            if i > j:
                return False

        return True

###############################################################################
"""
Solution 3: DP, recursion w/ memo

dp[pos][net count]

O(n^2) time
O(n^2) extra space: for memo; there's also overhead for recursion

* Note sure how to turn this into tabulation since net count is calculated
going forward, but base case is at the end and depends on net count.
Also, there's an early return if net count ever becomes negative.

Runtime: 36 ms, faster than 13.69% of Python3 online submissions
Memory Usage: 14.5 MB, less than 14.29% of Python3 online submissions
"""
import functools
class Solution3:
    def checkValidString(self, s: str) -> bool:
        @functools.lru_cache(None)
        def solve(i, count):
            if count < 0:
                return False
            
            if i == n:
                return count == 0

            if s[i] == '(':
                return solve(i+1, count+1)
            if s[i] == ')':
                return solve(i+1, count-1)

            # s[i] == '*'
            return max(solve(i+1, count), solve(i+1, count-1), solve(i+1, count+1))

        n = len(s)

        return solve(0, 0)

"""
*** NOT DONE

Solution 3b: DP tabulation

dp[pos][net count]

O(n^2) time
O(n^2) extra space: for dp table
"""
class Solution3b:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)
        dp = [[0] * (2*n) for _ in range(n)]

        pass

###############################################################################
"""
Solution 4: DP tabulation

dp[i][j] := True if interval s[i], ..., s[j] can be made valid.
ie,

s[i] is '*' and s[i+1], ..., s[j] can be made valid

or

s[i] is '*' or '(', and there is some k in [i+1, j] such that:
    - s[k] is ')' or '*'
    - the two subintervals cut by s[k] can be made valid
        - s[i+1:k] and s[k+1:j+1]


O(n^3) time
O(n^2) time: for dp table

Runtime: 268 ms, faster than 5.01% of Python3 online submissions
Memory Usage: 14 MB, less than 14.29% of Python3 online submissions
"""
class Solution4:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True

        LEFTY = '(*'
        RIGHTY = ')*'
        n = len(s)

        dp = [[False] * n for _ in s]

        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True

            if i < n - 1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        """
        Check intervals [0,2], [1,3], ..., [n-3, n-1],
        [0,3], [1,4], ..., [n-4, n-1], etc.
        """
        for sz in range(2, n):
            for i in range(n - sz):
                j = i + sz

                if s[i] == '*' and dp[i+1][j]:
                    dp[i][j] = True
                elif s[i] in LEFTY:
                    for k in range(i+1, j+1):
                        if (s[k] in RIGHTY and
                        (k == i+1 or dp[i+1][k-1]) and
                        (k == j or dp[k+1][j])
                        ):
                            dp[i][j] = True

        return dp[0][-1]
        
###############################################################################
"""
Solution 5: brute force using backtracking.

O(n * 3^n) time: check 3 possibilities for each '*', with at most n number of stars.
O(n) extra space: for array holding chars of string.

TLE
"""
class Solution5:
    def checkValidString(self, s: str) -> bool:
        def solve(i):
            nonlocal res
            if i == n:
                res |= valid()
            elif a[i] == '*':
                for c in '() ': # try 3 possibilities; note the space
                    a[i] = c
                    solve(i+1)
                    if res:
                        return
                a[i] = '*' # backtrack
            else:
                solve(i+1)

        def valid():
            net = 0
            for c in a:
                if c == '(': 
                    net += 1
                elif c == ')': 
                    net -= 1
                    if net < 0:
                        return False

            return net == 0
                
        n = len(s)
        a = list(s)
        res = False
        
        solve(0)

        return res       

###############################################################################
"""
Solution 6: brute force using backtracking after doing these checks:

1. Reduce string. Returns false if ')' is encountered and stack is empty.
2. Check left and right ends of string.
3. Check net balance vs number of stars.

TLE
"""
class Solution6:
    def checkValidString(self, s: str) -> bool:
        def solve(i):
            nonlocal res
            if i == n:
                res |= valid()
            elif a[i] == '*':
                for c in '() ': # try 3 possibilities; note the space
                    a[i] = c
                    solve(i+1)
                    if res:
                        return
                a[i] = '*' # backtrack
            else:
                solve(i+1)

        def valid():
            net = 0
            for c in a:
                if c == '(': 
                    net += 1
                elif c == ')': 
                    net -= 1
                    if net < 0:
                        return False

            return net == 0
                
        n = len(s)
        a = list(s)
        res = False

        def reduce(s):
            stack = []

            for c in s:
                if c == ')':
                    if not stack:
                        return False
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)

            return stack


        s = reduce(s)
        
        if s is False: # distinguish from []
            return False

        print('\n### PASSED reduce check')

        # Check left end
        star_count = 0
        for c in s:
            if c == '*':
                star_count += 1
            elif c == '(':
                break
            else:
                star_count -= 1
                if star_count < 0:
                    print('\n### FAILED check on left end')
                    return False
            
        # Check right end
        star_count = 0
        for c in reversed(s):
            if c == '*':
                star_count += 1
            elif c == ')':
                break
            else:
                star_count -= 1
                if star_count < 0:
                    print('\n### FAILED check on right end')
                    return False
        
        print("\n### PASSED check on ends")

        # possible balance check

        net = 0
        star = 0

        for c in s:
            if c == '(':
                net += 1
            elif c == ')':
                net -= 1
            else:
                star += 1

        print(f"\nnet = {net}")
        print(f"star = {star}")

        if star < abs(net):
            print('\n### FAILED net/star check')
            return False

        print('\n### PASSED net/star check')
        
        solve(0)

        return res

"""
Instead of simple backtracking, what if we tried only the possibilities for
the stars such that the net balance is 0?

Example:
15 star
13 net

want:
13 -1
2 left sum to 0
both 0, or () or )(

C(13,2) * 3 possibilities

But what if net close to 0, and star >> net ?

net = 1
star = 20

1 is -1
19 left sum to 0
k each of ( and ), where k = 0..9, with rest blank

20 * (sum_k C(19,k) * C(19-k, k))
or 20 * C(19, k, k)

"""

###############################################################################
"""
Solution 7: NOT a solution.

Simple checks:
1. Reduce string. Returns false if ')' is encountered and stack is empty.
2. Check left and right ends of string.
3. Check net balance vs number of stars.

"""
class Solution7:
    def checkValidString(self, s: str) -> bool:
        def reduce(s):
            stack = []

            for c in s:
                if c == ')':
                    if not stack:
                        return False
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)

            return stack


        s = reduce(s)
        #if s: print(''.join(s))

        if s is False: # distinguish from []
            return False

        print('### PASSED reduce check')

        # Check left end
        star_count = 0
        for c in s:
            if c == '*':
                star_count += 1
            elif c == '(':
                break
            else:
                star_count -= 1
                if star_count < 0:
                    print('\n### FAILED check on left end')
                    return False
            
        # Check right end
        star_count = 0
        for c in reversed(s):
            if c == '*':
                star_count += 1
            elif c == ')':
                break
            else:
                star_count -= 1
                if star_count < 0:
                    print('\n### FAILED check on right end')
                    return False

        print('\n### PASSED check on ends')

        # possible balance check

        net = 0
        star = 0

        for c in s:
            if c == '(':
                net += 1
            elif c == ')':
                net -= 1
            else:
                star += 1

        print(f"\nnet = {net}")
        print(f"star = {star}")

        if star < abs(net):
            print('\n### FAILED net/star check')
            return False

        print('\n### PASSED net/star check')
        
        # Need to check more...
        
        return True

###############################################################################

if __name__ == "__main__":
    def reduce(s):
        stack = []

        for c in s:
            if c == ')':
                #if not stack:
                #    return False
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return stack

    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")
        r = ''.join(reduce(s))
        print(f"\nreduce(s) = {r}")

        res = sol.checkValidString(s)

        print(f"\nres = {res}\n")


    sol = Solution() # greedy; forward and reverse traversals
    sol = Solution1b() # greedy; forward traversal, tracking lo and hi
    
    sol = Solution2() # greedy stack-based validation
    
    #sol = Solution3() # DP memo using dp[pos][net count]
    #sol = Solution3b() # DP tabulation ... NOT DONE

    #sol = Solution4() # DP using dp[i][j] for interval s[i]...s[j] (official sol)

    #sol = Solution5() # brute force using backtracking

    #sol = Solution6() # brute force using backtracking after reduce, check ends, and check balance/stars
    
    #sol = Solution7() # NOT a sol; just simple checks

    comment = 'LC ex1; answer = True'
    s = "()"
    test(s, comment)

    comment = 'LC ex2; answer = True'
    s = "(*)"
    test(s, comment)

    comment = 'LC ex3; answer = True'
    s = "(*))"
    test(s, comment)

    comment = 'trivial case; answer = True'
    s = ""
    test(s, comment)

    comment = 'LC TC; answer = True'
    s = "(*()"
    test(s, comment)

    comment = 'LC TC; answer = False'
    s = ")"
    test(s, comment)

    comment = 'LC TC; answer = False'
    s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
    test(s, comment)

    comment = 'remove () from above; answer = False'
    s = "((*)(*))((*"
    test(s, comment)

    comment = 'not enough to check ends; answer = False'
    s = "*()(())*()(()()((()(()()*)(*(())((((((((()*)(()(*)"
    # reduced = **((((*)(*((((((((*)((*)
    # net = 12; star 6 => string not valid
    test(s, comment)

    comment = 'not enough to check ends, and to check net count with stars; answer = False'
    # reduced = (*)(*)(((*)))((((((*))
    # net = 4, star = 4
    s = "(()*)(()((())()))(*)((((())*())))()(((()((()(*()))"
    test(s, comment)

    comment = "LC TC; TLE's backtracking but fails simple reduce check; answer = False"
    # FAILS reduce check
    s = "(((()))())))*))())()(**(((())(()(*()((((())))*())(())*(*(()(*)))()*())**((()(()))())(*(*))*))())"
    test(s, comment)

    comment = "LC TC; TLE's backtracking w/ reduce; answer = False"
    # passes reduce check
    # FAILS check on ends
    # reduce = *))))*)*(**))))((*)((*))**)))*))))))))*)(*((((**
    s = "(()())*)))())*)*(*()*()))())())((*)((((((())))())*))**)))()*))()))))()()))*)()(*(())((()((()**()()"
    test(s, comment)

    comment = "LC TC; TLE's backtracking w/ reduce and checks on ends; answer = False"
    # passes reduce check
    # passes check on ends
    # net = 13, star = 15 ; passes net/star check
    # reduce = (((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((((**(**)
    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    test(s, comment)
