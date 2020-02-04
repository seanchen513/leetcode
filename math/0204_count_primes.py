"""
204. Count Primes
Easy

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4

Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

from typing import List

###############################################################################

"""
Solution 1: Use assignment of list slices.
This is solution 2 with some optimizations:

1. Use ints 0 and 1 instead of booleans True and False.
2. Move out the case i = 2.  This way, we can loop over odd i only.
3. Since i is odd, with the slicing, we can increment by 2*i instead 
of just i.
4. Instead of using len(sieve[...]), use len(range(...)) or calculate directly.

LeetCode Feb 3, 2020:
Runtime: 84 ms, faster than 99.63% of Python3 online submissions for Count Primes.
Memory Usage: 35.8 MB, less than 58.62% of Python3 online submissions for Count Primes.
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: 
            return 0

        #end = int((n-1)**0.5) + 1
        end = int(n**0.5) + 1
        sieve = [1]*n
        sieve[0] = sieve[1] = 0

        #sieve[4: n: 2] = [0] * len(range(4, n, 2))
        sieve[4: n: 2] = [0] * ((n-5)//2 + 1)

        for i in range(3, end, 2):
            if sieve[i]:
                #sieve[i*i: n: 2*i] = [0] * len(range(i*i, n, 2*i))
                sieve[i*i: n: 2*i] = [0] * ((n-i*i-1)//(2*i) + 1)
                 
        return sum(sieve)

###############################################################################
"""
Solution 2: Use assignment of list slices.  This is a lot faster than
using a loop.

Sieve is list with indices 0 to n.  Value of sieve[i] is 0 if 
sieve[i] is definitely not a prime.  At the end, sieve[i] is 1
if sieve[i] is a prime.

https://leetcode.com/problems/count-primes/discuss/57595/Fast-Python-Solution
"""
class Solution2:
    def countPrimes(self, n: int) -> int:
        if n < 3: 
            return 0

        end = int((n-1)**0.5) + 1
        sieve = [True]*n
        sieve[0] = sieve[1] = 0

        for i in range(2, end):
            if sieve[i]:
                sieve[i*i: n: i] = [False] * len(sieve[i*i: n: i])

        return sum(sieve)

###############################################################################
"""
Solution 3: Sieve of Eratosthenes

Finds all primes up to and including given integer n.

Initialize "sieve" set to store potential primes.
Start with odd integers >= 3 to save time and space.

This is essentially doing some precalculations to save space and time.
"""
class Solution3:
    def countPrimes(self, n: int) -> int:
        if n < 3: # eg, if n is 2, there are 0 primes less than 2
            return 0

        end = int((n-1)**0.5) + 1
        sieve = set(range(3, n, 2)) # set of potential primes
        sieve.add(2)

        for i in range(3, end, 2):
            # If i was already eliminated in a previous pass, than so were
            # all it's multiples.  So no need to deal with i.
            # We increment by 2*i since i is odd and i*i is odd.
            # So i*i + i would be even, while i*i + 2i would be odd.
            # We only want to consider odd integers.

            if i in sieve:
                # sieve -= set(range(i*i, n, 2*i)) # this is slower

                # Suffices to start at i*i since smaller multiples of i were
                # already crossed out in a previous iteration of i.
                for j in range(i*i, n, 2*i):
                    sieve.discard(j)

        return len(sieve)

###############################################################################
"""
Solution 4:

Every prime > 3 has form 6k-1 or 6k+1.

Forms 6k, 6k+2, and 6k+4 are even, so can't be prime unless 2.
Form 6k+3 is divisible by 3, so can't be prime unless 3.
That leaves forms 6k+1 and 6k-1 (ie, 6k+5).

Therefore, initialize our sieve of potential primes with 
forms 6k-1 and 6k+1.  It's missing only primes 2 and 3.

Don't need to check for multiples of 2 or 3.
"""
class Solution4:
    def countPrimes(self, n: int) -> int:
        from itertools import chain
        if n < 3: # eg, if n is 2, there are 0 primes less than 2
            return 0
        if n == 3:
            return 1

        end = int((n-1)**0.5) + 1

        # "sieve" starts out as set of potential primes
        # doesn't include primes 2 and 3
        sieve = set(chain(range(7, n, 6), range(5, n, 6)))
        sieve.add(2)
        sieve.add(3)

        for i in range(5, end, 2):
            if i in sieve:
                for j in range(i*i, n, 2*i):
                    sieve.discard(j)

        return len(sieve)

###############################################################################
"""
Solution 5:

All primes > 5 have form 30k+d for d in (1,7,11,13,17,19,23,29).
Initialize sieve with these potential primes.

Sieve size is 8/30 = 26.7% size of original, or 80% of size if we took
possible primes of form 6+1 and 6k+5.
"""
class Solution5:
    def countPrimes(self, n: int) -> int:
        from itertools import chain
        if n < 3: # eg, if n is 2, there are 0 primes less than 2
            return 0
        if n == 3:
            return 1
        if n == 4 or n == 5:
            return 2

        end = int((n-1)**0.5) + 1

        # "sieve" starts out as set of potential primes
        # doesn't include primes 2, 3, and 5
        sieve = set(chain(
            range(7, n, 30), 
            range(11, n, 30),
            range(13, n, 30),
            range(17, n, 30),
            range(19, n, 30),
            range(23, n, 30),
            range(29, n, 30),
            range(31, n, 30),
            ))
        sieve.add(2)
        sieve.add(3)
        sieve.add(5)

        for i in range(7, end, 2):
            if i in sieve:
                for j in range(i*i, n, 2*i):
                    sieve.discard(j)

        return len(sieve)

###############################################################################
"""
Solution 6: Use a count.

Avoid updating array values for even integers by starting count at n // 2.
We don't care about the actual sieve values for even indices now (so no need
to invert the boolean values).

Sieve values start as 1 (True).  With the loop, whenever a sieve value needs
to be changed to 0 (False), decrement the count.

We can't easily do assignment of list slices because we want to deal with
the count.

https://leetcode.com/problems/count-primes/discuss/57593/12-ms-Java-solution-modified-from-the-hint-method-beats-99.95
"""
class Solution6:
    def countPrimes(self, n: int) -> int:
        if n < 3: 
            return 0

        #end = int((n-1)**0.5) + 1
        end = int(n**0.5) + 1
        count = n // 2

        sieve = [1]*n
        #sieve[0] = sieve[1] = 0

        #sieve[4: n: 2] = [0] * len(range(4, n, 2))
        #sieve[4: n: 2] = [0] * ((n-5)//2 + 1)

        for i in range(3, end, 2):
            if sieve[i]:
                #sieve[i*i: n: 2*i] = [0] * len(range(i*i, n, 2*i))
                #sieve[i*i: n: 2*i] = [0] * ((n-i*i-1)//(2*i) + 1)
                
                for j in range(i*i, n, 2*i):
                    if sieve[j]:
                        count -= 1
                        sieve[j] = 0
                 
        return count

###############################################################################

if __name__ == "__main__":
    def test_ints(ints):
        s = Solution()
        #s2 = Solution2()
        #s3 = Solution3()
        #s4 = Solution4()
        #s5 = Solution5()
        #s6 = Solution6()

        res = {}
        for n in ints:
            res[n] = s.countPrimes(n)

        print(res)

    def test(n=100):
        solutions = [Solution(), Solution2(), Solution3(), Solution4(), 
            Solution5(), Solution6()]

        res = []
        for s in solutions:
            res += [s.countPrimes(n)]

        print("="*80)
        print(f"Testing results of solutiosn for n = {n}\n")
        print(res)

    def test_times(n=100):
        from timeit import default_timer as timer

        solutions = [Solution(), Solution2(), Solution3(), Solution4(), 
            Solution5(), Solution6()]

        times = []

        for s in solutions:
            start = timer()
            s.countPrimes(n)
            t = timer() - start
            times += [t]

        print("="*80)
        print(f"\nTesting times for solutions with n = {n}\n")
        for i in range(len(times)):
            print(times[i])

    #ints = [0, 1, 2, 3, 4, 10, 11, 12, 13, 10000000]
    #test_ints(ints)

    #test(1000)
    test_times(1000000)
