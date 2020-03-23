"""
400. Nth Digit
Medium

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""

###############################################################################
"""
Solution: look at groups of integers with the same number of digits.

first = 10**(digits - 1) = first element of group
9 * first = size of group
9 * first * digits = number of digits in group

digits  first   gp size     num digits in group
1       1       9           9 digits
2       10      90          180
3       100     900         2700
4       1000    9000        36000
5       10k     90k         450k
6       100k    900k        5.4M
7       1M      9M          63M
8       10M     90M         720M
9       100M    900M        8.1B
10      1B      9B          90B
11      10B     90B         990B

https://leetcode.com/problems/nth-digit/discuss/88375/Short-Python%2BJava
"""
class Solution:
    def findNthDigit(self, n):
        for digits in range(1, 11):
            first = 10**(digits - 1) # first element of group

            if n <= 9 * first * digits:
                return int( str(first + (n-1) // digits)[(n-1) % digits] )
            
            # Since n > 9 * first * digits, then after subtraction, n >= 1.
            n -= 9 * first * digits # subtract number of digits in group
            

"""
Example:
n = 191 (200)

digits = 1
first = 1
n -= 9
    n = 191 - 9 = 182 (191)

digits = 2
first = 10
n -= 9 * 10 * 2
    n -= 180
    n = 2 (11)

digits = 3
first = 100
(n - 1) // digits = 1 // 3 = 0 (alt: 10 // 3 = 3)
first + (n-1)//digits = 100 + 0 = 100 (alt: 100 + 3 = 103)

(n - 1) % digits = 1 % 3 = 1 (alt: 10 % 3 = 1)
...

99 has nth digits 188 and 189
100 has nth digits 190, 191, 192
101 has nth digits 193, 194, 195

"""

"""
Solution 1b: same as sol 1, but n shifted down by 1.
"""
class Solution2b:
    def findNthDigit(self, n):
        n -= 1

        for digits in range(1, 11):
            first = 10**(digits - 1) # first element of group

            if n < 9 * first * digits:
                return int( str(first + n // digits)[n % digits] )
            
            n -= 9 * first * digits # subtract number of digits in group


"""
Example:
n = 513

digits = 1
first = 1
n -= 9

n = 513 - 9 = 504

digits = 2
first = 10
n -= 9 * 10 * 2

n = 504 - 180 = 324

digits = 3
first = 100
9 * first * digits = 9 * 100 * 3 = 2700
n / digits = 324 / 3 = 108
first + n/digits = 100 + 108 = 208

"""

###############################################################################
"""
Solution: brute force

TLE on n = 1000000000
"""
class Solution2:
    def findNthDigit(self, n: int) -> int:
        i = 0

        while n > 0:
            i += 1
            n -= len(str(i))
        
        #print(f"n = {n}")    
        
        if n == 0:
            return i % 10 # last digit

        # while n < 0:
        #     i //= 10
        #     n += 1

        # return i % 10

        # ..., -2, -1, 0
        return str(i)[n-1]

###############################################################################

if __name__ == "__main__":
    sol = Solution()
    #res = sol.findNthDigit(103) # 6
    res = sol.findNthDigit(513) # 7
    print(f"\nres = {res}")


"""
100 - 5
101 - 5
102 - 5
103 - 6

99 has nth digits 188 and 189
100 has nth digits 190, 191, 192
101 has nth digits 193, 194, 195

188 - 9
189 - 9
190 - 1
191 - 0
192 - 0
193 - 1
194 - 0
195 - 1

1000 - 3
1001 - 7
1002 - 0
1003 - 3
"""

"""
10  1
11  0
12  1
13  1
14  1
15  2
16  1
17  3
18  1
19  4
20  1
21  5
22  1
23  6
24  1
25  7
26  1
27  8
28  1
29  9
30  2
31  0
"""
