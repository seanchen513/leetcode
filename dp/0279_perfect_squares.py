"""
279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
###############################################################################
"""
Solution: simple recursion.

LC TLE
"""
class Solution:
    def numSquares(self, n: int) -> int:
        def num_squares(m, min_count=float('inf')):
            if m == 0:
                return 0

            i = 1
            while i*i <= m:
                count = 1 + num_squares(m - i*i, min_count)
                min_count = min(min_count, count)

                i += 1

            return min_count

        return num_squares(n)

###############################################################################
"""
Solution: Recursion w/ memoization.

Very slow if "cache" is a variable inside numSquares() that is accessed
as a nonlocal within the helper function.  TLE's on LC.  If "cache" is made
"static" by making it a class var, then solution takes ~280ms on LC.
"""
class Solution2:
    cache = {0: 0}

    def numSquares(self, n: int) -> int:
        def num_squares(m, min_count=float('inf')):
            if min_count == 1:
                return 1

            if m in self.cache:
                return self.cache[m]

            i = 1
            while i*i <= m:
                count = 1 + num_squares(m - i*i, min_count)
                min_count = min(min_count, count)

                i += 1

            self.cache[m] = min_count

            return min_count

        return num_squares(n)

###############################################################################
"""
Solution 3: tabulation (very fast).

First check if given integer n is a square.  Then form a list of all 
squares < n.  Add squares to the list of squares up to until n is reached
or surpassed.  If one of the new sums equals n, return the count.
Otherwise, we now have a list of sums of two squares up to n.  Repeat.

This can be thought of as a BFS of a graph with nodes 0, 1, 2, ..., n.  
Two nodes are connected by an edge if they differ by a positive square.  
Starting from node 0, do a BFS.  If we reach node n at step k, then the least 
number of squares that sum to n is k.  By Lagrange's 4-square theorem, 
k is at most 4.

Note: we don't have to keep track of the minimum count of squares for
each integer (node) because we only care about "n", and we return
the answer the first time a sum of squares is found for "n".

O(n) time overall (at most)
O(sqrt(n)) extra space

O(sqrt(n)) to form "squares", which has length ~sqrt(n).
Main loop iterates at most 3 times (by Lagrange's 4-square theorem).
Each of the two nested, inner loops is at most O(sqrt(n)).
The 3 nested loops together is at most O(n).
"""
class Solution3:
    def numSquares(self, n: int) -> int:
        n_sqrt = int(n**0.5)
        if n_sqrt*n_sqrt == n:
            return 1

        squares = [i*i for i in range(1, n_sqrt + 1)] # O(sqrt(n)) time
        prev_sums = squares
        count = 1 # count of number of squares added together so far

        while True:
            count += 1 # new number of squares added together
            new_sums = [] # integers that we can form with new sums of squares

            for prev_sum in prev_sums: # O(sqrt(n)) time
                for sq in squares: # O(sqrt(n)) time
                    new_sum = prev_sum + sq
                    if new_sum == n: 
                        return count
                    if new_sum > n: 
                        break

                    new_sums.append(new_sum)

            prev_sums = new_sums

        return -1 # this point is never reached

###############################################################################
"""
Solution 4: tabulation (very slow; ~4200ms).

Start off with count[0] = 0.
After first iteration (outer loop i=1), count[1] = 1 + count[1 - 1] = 1.
After 2nd iteration (i=2), count[2] = 1 + count[2 - 1] = 2.
After more iterations...
count[3] = 1 + count[3 - 1] = 1 + count[2] = 3.

i = 4, j = 1:
    count[4] = min(inf, 1 + count[4 - 1*1]) min(inf, 4) = 4
    which represents 4 = 1+1+1+1.

i = 4, j = 2:
    count[4] = min(4, 1 + count[4 - 2*2]) = min(4, 1) = 1
    which represents 4 = 2*2.

https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)
"""
class Solution4:
    def numSquares(self, n: int) -> int:
        # value of "count" is number of squares that sum to index
        count = [float('inf')]*(n+1)
        count[0] = 0 # needed to build from; 0 is no sum of positive squares

        for i in range(1, n+1):
            i_sqrt = int(i**0.5) + 1
            
            for j in range(1, i_sqrt):
                count[i] = min(count[i], 1 + count[i - j*j])

        return count[n]

###############################################################################
"""
Solution 4b: tabulation like solution 4, but use a "static" count variable.
In Python, one way to do this is to make "class" a class variable.

Reduces solution 4's ~4200ms time to ~160ms.

https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)
"""
class Solution4b:
    def numSquares(self, n: int) -> int:
        count = [0] # count of squares that sum to each index

        while len(count) <= n:
            m = len(count)
            count_squares = float('inf')
            #count_squares = float(4)

            m_sqrt = int(m**0.5) + 1
            for i in range(1, m_sqrt):
                count_squares = min(count_squares, 1 + count[m - i*i])

            count.append(count_squares)

        return count[n]

###############################################################################
"""
Solution 5: Number theory.

Lagrange's 4-square thm: every nonnegative integer is the sum of at most
4 squares.  Can take these to be all positive squares.

Legendre's 3-square thm: a nonnegative integer is the sum of 3 squares
(incl. 0 squares) <=> it's not of the form (4^a)(8b+7).

This implies a positive integer of this form must be a sum of 4 squares.

We can check given integer n in this order:
1. If n is a square, return 1.
2. If n has the Legendre form, return 4.
3. Use iteration to check if n is a sum of 2 squares.  If so, return 2.
4. The only remaining possibility is 3.
"""
class Solution5:
    # Checks whether given integer n has form (4^a)*(8b+7).
    def sum_of_four_squares(self, n: int) -> bool:
        while (n & 3) == 0: # n % 4 == 0
            n >>= 2 # n //= 4

        return (n & 7) == 7 # n % 8 == 7

    def numSquares(self, n: int) -> int:
        n_sqrt = int(n**0.5)
        if n_sqrt * n_sqrt == n:
            return 1

        if self.sum_of_four_squares(n):
            return 4

        for i in range(1, n_sqrt + 1):
            x = n - i*i
            x_sq = int(x**0.5)

            if x_sq * x_sq == x:
                return 2

        return 3      

###############################################################################

if __name__ == "__main__":
    def test(n, comment=None):
        solutions = [
            #Solution(), # simple recursion; very slow
            #Solution2(), # memoization w/ cache a class var; stack overflow...
            Solution3(), # tabulation/BFS
            #Solution4(), # tabulation; very slow
            Solution4b(), # tabulation w/ "count" a class var
            Solution5(), # number theory
            ] 

        res = [s.numSquares(n) for s in solutions]

        print("="*80)
        if comment:
            print(comment, "\n")
        print(n)

        print(f"\nSolutions: {res}\n")

    def test_legendre(): 
        print("\nTesting part of Legendre's three-square theorem.")
        print("Verifying that integers of the form (4**a)*(8*b+7)")
        print("are the sum of 4 positive squares.\n")

        #ints = [7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71] # n=(4^a)(8b+7)
        ints = sorted([(4**a)*(8*b+7) for a in range(5) for b in range(11)])

        #s = Solution3() # tabulation/BFS
        s = Solution4b() # tabulation w/ "count" a class var
        #s = Solution5() # number theory

        for i in ints:
            n_sq = s.numSquares(i)
            print(f"{i} is the sum of {n_sq} squares.")

    def test_up_to(n=100):
        print("="*80)
        
        #s = Solution3() # tabulation/BFS
        #s = Solution4b() # tabulation w/ "count" a class var
        s = Solution5() # number theory
        
        d = {1: [], 2: [], 3: [], 4: []}

        for i in range(1, n+1):
            n_sq = s.numSquares(i)
            d[n_sq] += [i]
            
            #print(f"{i}: {n_sq}", end=", ")
        
        print("\n")   
        print("="*80)

        for n_sq, lst in d.items():
            print(f"\nSum of {n_sq} square(s):")
            print(lst)
            print()

    ###
    #import sys
    #recursion_limit = sys.getrecursionlimit() # I get 1000
    #sys.setrecursionlimit(5000)

    test_cases = [
        (7, "answer = 4 (4+1+1+1) (Legendre)"),
        (13, "LC ex2; answer = 2 (4+9)"),
        (12, "LC ex1; answer = 3 (4+4+4)"),
        (18, "answer = 2 (9+9, not 16+1+1)"),
        (25, "answer = 1 (25=5*5)"),

        ### Following for faster solutions only.
        (45, "LC ex2; TLE for simple recursion; answer = 2 (36+9)"),
        (100, "answer = 1 (100=10*10)"),
        (240, "answer = 4 (Legendre)"),
        (640, "answer = 2 (576+64)"),

        ### Following only for iterative tabulation.
        ### May get "maximum recursion depth exceeded" if use recursion.
        (1337, "answer = 3"),
        (5056, "answer = 4 (Legendre)"),
        (14000, "answer = 3"),
    ]

    #for n, comment in test_cases:
    #    test(n, comment)

    test_legendre()

    #test_up_to(1000)
