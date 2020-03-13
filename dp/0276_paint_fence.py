"""
276. Paint Fence
Easy

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
"""

"""
Example: (same as LC example)
n = 3, k = 2, answer = 6

1 1 2
1 2 1
1 2 2
2 1 1
2 1 2
2 2 1

Example:
n = 4, k = 2, answer = 10

1 1 2 1
1 2 1 1

1 1 2 2
1 2 2 1
1 2 1 2

2 2 1 2
2 1 2 2

2 2 1 1
2 1 1 2
2 1 2 1

Examples:
n = 1, k = k, answer = k
n = 2, k = 1, answer = 1
n > 2, k = 1, answer = 0

Example:
n = 2, k = 2, answer = 4

1 1
1 2
2 1
2 2

Example:
n = 2, k = 3, answer =  9

1 1
1 2
1 3

2 1
2 2
2 3

3 1
3 2
3 3

Example:
n = 3, k = 3, answer = 24

1 1 2   1 2
1 1 3   1 3
1 2 1
1 2 2   1 2
1 2 3
1 3 1
1 3 2
1 3 3   1 3

2 1 1   2 1
2 1 2
2 1 3
2 2 1   2 1
2 2 3   2 3
2 3 1
2 3 2
2 3 3   2 3

3 1 1   3 1
3 1 2
3 1 3
3 2 1
3 2 2   3 2
3 2 3
3 3 1   3 1
3 3 2   3 2
"""

###############################################################################
"""
Solution: use recurrence relation.

f(n) = ( f(n-1) + f(n-2) ) * (k-1)

f(n-1): pick a color for the nth fence post that is different from the
(n-1)st one.  There are k-1 choices for this.

f(n-2): pick the same color for the (n-1)st and nth fence post that is
different from the color of the (n-2)nd fence post.  There are k-1 choices.

O(n) time
O(1) extra space
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        if k == 1:
            return 1 if n <= 2 else 0 # return int(n < 3)
        if n == 1:
            return k

        a, b = k, k*k # f(1), f(2)

        for _ in range(n-2): # for _ in range(3, n+1):
            a, b = b, (a+b)*(k-1)

        return b

"""
Solution 1b: use explicit formula for Lucas sequence of 1st kind.

Lucas sequence:
f(n) = P f(n-1) - Q f(n-2)

where f(0)=0, f(1)=1, f(2)=P for Lucas sequence of first kind.

For this problem, P = k-1 and Q = 1-k = -P.
Also, we need to shift n since we want f(1)=P rather than f(2)=P.
Also, we need to scale so f(1)=k.

//
Discriminant D = P^2 - 4Q = (k-1)^2 - 4(1-k) = P*(P-4)
Also = 5*(k-1)^2 >= 0.

If k > 1, then there are distinct roots to characteristic equation
x^2 - Px + Q = 0, and we have:

f(n) = (a^n - b^n) / sqrt(D)

where a and b are the roots of the characteristic equation are:

a = (P + sqrt(D))/2
b = (P - sqrt(D))/2 = a - sqrt(D) = P - a

https://en.wikipedia.org/wiki/Lucas_sequence

"""
class Solution1b:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        if k == 1:
            return 1 if n <= 2 else 0 # return int(n < 3)

        P = k - 1
        D_sqrt = (P * (P + 4))**0.5
        
        a = (P + D_sqrt) / 2
        b = P - a

        return round( (a**(n+1) - b**(n+1)) / D_sqrt * k/P )

###############################################################################
"""
Solution 2: based on simpler problem:

What if no adjacent fence posts can have the same color?

n >= 1, k=2, res=2
1 2 1 2 ...
2 1 2 1 ...

n = 1, k=3, res=3

n = 2, k=3, res = 6
1 2
1 3
2 1
2 3
3 1
3 2

n = 3, k=3, res=12
1 2 1
1 2 3
1 3 1
1 3 2
2 1 2
2 1 3
2 3 1
2 3 2
3 1 2
3 1 3
3 2 1
3 2 3

g(n,k) = g(n-1,k) * (k-1)
= k * (k-1)^(n-1)

//
IDEA:

n=5, k=2, answer = 16

1 1 2 1 1   (1) 2 (1)   f(n-2,k)
1 1 2 1 2   (1) 2 1 2   (n-1,k)
1 1 2 2 1   (1) (2) 1   f(n-2,k)

1 2 1 1 2   1 2 (1) 2   f(n-1,k)
1 2 1 2 1   
1 2 1 2 2   1 2 1 (2)   f(n-1,k)
1 2 2 1 1   1 (2) (1)   f(n-2,k)
1 2 2 1 2   1 (2) 1 2   f(n-1,k)

f(n,k) = g(n,k) + f(n-2, k) * C(n-2,2) + f(n-1, k) * C(n-1,1)
= g(n,k) + f(n-2,k) * (n-2)! + f(n-1,k) * (n-1)

where g = no adjacent same color
//

n=6, k=2

1 1 2 2 1 1     (1) (2) (1)     f(n-3,k)
...

f(n,k) = g(n,k) + g(n-1,k) * C(n-1,1) + g(n-2,k) * C(n-2,2) + g(n-3,k) * C(n-3,3)

etc.
"""
import math
class Solution2:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 or k == 0:
            return 0
        # if k == 1:
        #     return 1 if n <= 2 else 0 # return int(n < 3)
        # if n == 1:
        #     return k

        # def nCr(n,r): # math.comb(n, r) is in Python 3.8
        #     f = math.factorial
        #     return f(n) // f(r) // f(n-r)

        # Ways to color m posts with r colors, if no two adjacent colors same
        def g(m, r):
            return r * ((r-1)**(m-1))

        res = g(n, k)

        for i in range(1, n//2 + 1 ):
            #res += g(n - i, k) * nCr(n-i,i)
            res += g(n - i, k) * math.comb(n-i,i)

        return res

###############################################################################

if __name__ == "__main__":
    def test(n, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\nn = {n}")
        print(f"k = {k}")

        res = sol.numWays(n, k)

        print(f"\nres = {res}\n")


    sol = Solution() # based on extending cases n-1,k and n-2,k
    #sol = Solution1b() # use explicit formula for Lucas sequence of 1st kind
    #sol = Solution2() # based on simpler problem of no adjacent colors same

    comment = "LC example; answer = 6"
    n = 3
    k = 2
    test(n, k, comment)

    comment = "LC test case; answer = 0"
    n = 0
    k = 0
    test(n, k, comment)

    comment = "LC test case; answer = 1"
    n = 1
    k = 1
    test(n, k, comment)

    comment = "LC test case; answer = 2"
    n = 1
    k = 2
    test(n, k, comment)

    comment = "LC test case; answer = 10"
    n = 4
    k = 2
    test(n, k, comment)

    comment = "answer = 16"
    n = 5
    k = 2
    test(n, k, comment)

    comment = "answer = 26"
    n = 6
    k = 2
    test(n, k, comment)

    comment = "answer = 42"
    n = 7
    k = 2
    test(n, k, comment)

    comment = "answer = 68"
    n = 8
    k = 2
    test(n, k, comment)

    comment = "answer = 24"
    n = 3
    k = 3
    test(n, k, comment)

    comment = "answer = 66"
    n = 4
    k = 3
    test(n, k, comment)

    comment = "answer = 180"
    n = 5
    k = 3
    test(n, k, comment)

    comment = "answer = 492"
    n = 6
    k = 3
    test(n, k, comment)
