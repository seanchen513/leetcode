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
Solution: recursion.

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

Still very slow.
"""
class Solution2:
    def numSquares(self, n: int) -> int:
        def num_squares(m, min_count=float('inf')):
            nonlocal cache
            if min_count == 1:
                return 1

            if m in cache:
                return cache[m]

            i = 1
            while i*i <= m:
                count = 1 + num_squares(m - i*i, min_count)
                min_count = min(min_count, count)

                i += 1

            cache[m] = min_count

            return min_count

        cache = {0: 0}
        return num_squares(n)

###############################################################################
"""
Solution 3: tabulation

A lot faster than memoizaton here.

Avoid using number theory and math functions floor() and sqrt() here.
"""
class Solution3:
    def numSquares(self, n: int) -> int:
        if n in (0,1):
            return 1

        squares = []
        i = 1
        i_sq = 1
        while i_sq <= n:
            if i_sq == n:
                return 1
            
            squares.append(i_sq)
            i += 1
            i_sq = i*i

        min_count = [0]*(n+1)

        for i in squares:
            min_count[i] = 1

        prev = squares
        
        count = 1

        while True:
            count += 1
            next = []

            for i in prev:
                for j in squares:
                    k = i + j
                    if k == n:
                        return count
                    if k > n:
                        break
                    if min_count[k] == 0:
                        min_count[k] = count
                        next.append(k)

            prev = next

        return min_count[n]

###############################################################################
"""
Solution 4: combine tabulation with some number theory.
"""
class Solution4:
    def sum_of_four_squares(self, n): # aka, if legendre_form()
        # Checks whether given integer n has form (4^a)*(8b+7).
        if n < 7:
            return False

        while n % 4 == 0:
            n //= 4

        return (n - 7) % 8 == 0

    def numSquares(self, n: int) -> int:
        n_sqrt = int(n**0.5)
        if n_sqrt * n_sqrt == n:
            return 1

        if self.sum_of_four_squares(n):
            return 4

        squares = []
        i = 1
        i_sq = 1
        while i_sq <= n:
            if i_sq == n:
                return 1
            
            squares.append(i_sq)
            i += 1
            i_sq = i*i

        min_count = [0]*(n+1)

        for i in squares:
            min_count[i] = 1

        prev = squares
        
        count = 1

        while True:
            count += 1
            if count == 4: # by Lagrange's four-square theorem
                return 4

            next = []

            for i in prev:
                for j in squares:
                    k = i + j
                    if k == n:
                        return count
                    if k > n:
                        break
                    if min_count[k] == 0:
                        min_count[k] = count
                        next.append(k)

            prev = next

        return min_count[n]

###############################################################################
"""
Solution 5: Number theory.
"""
class Solution5:
    def sum_of_four_squares(self, n: int) -> bool: # aka, if legendre_form()
        # Checks whether given integer n has form (4^a)*(8b+7).
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
        #solutions = [Solution(), Solution1b(), Solution2(), Solution2b()] 
        
        #solutions = [Solution2(), Solution3(), Solution4()] # memo and tabulation

        solutions = [Solution3(), Solution4(), Solution5()] # tabulation and math

        res = [s.numSquares(n) for s in solutions]

        print("="*80)
        if comment:
            print(comment, "\n")
        print(n)

        print(f"\nSolutions: {res}\n")

    def test_legendre(): 
        print("\nTesting part of Legendre's three-square theorem.\n")

        #ints = [7, 15, 23, 28, 31, 39, 47, 55, 60, 63, 71] # n=(4^a)(8b+7)
        ints = sorted([(4**a)*(8*b+7) for a in range(4) for b in range(10)])

        #s = Solution2() # memoization
        s = Solution3() # tabulation

        for i in ints:
            n_sq = s.numSquares(i)
            print(f"{i} is the sum of {n_sq} squares.")

    def test_up_to(n=100):
        print("="*80)
        
        s = Solution3() # tabulation
        
        d = {1: [], 2: [], 3: [], 4: []}

        for i in range(n+1):
            n_sq = s.numSquares(i)
            d[n_sq] += [i]
            
            #print(f"{i}: {n_sq}", end=", ")
        
        print("\n")   
        print("="*80)

        for n_sq, lst in d.items():
            print(f"\nSum of {n_sq} square(s):")
            print(lst)
            print()


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

    for n, comment in test_cases:
        test(n, comment)

    #test_legendre()

    #test_up_to(1000)
