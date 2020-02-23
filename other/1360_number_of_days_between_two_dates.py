"""
1360. Number of Days Between Two Dates
Easy

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

from datetime import datetime

###############################################################################
"""
Solution: for each year, calculate days since year 0.
"""
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            
            if m == 1 or (m == 2 and d < 29):
                if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
                    d -= 1

            d += sum(days_in_months[:m-1])

            d += 365*y + y//4 - y//100 + y//400

            return d

        days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]

        return abs(f(date1) - f(date2))

###############################################################################
"""
Solution 2: for each year, calculate days since year 0.  Use magic formula
to deal with days.

When m = 1 or 2 (Jan or Feb), let m = 13 or 14, resp., and decrease y by 1.

https://leetcode.com/problems/number-of-days-between-two-dates/discuss/517582/Python-Magical-Formula
"""
class Solution2:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def f(date):
            y, m, d = map(int, date.split('-'))
            if m == 1 or m == 2:
                m += 12
                y -= 1
            
            return 365*y + y//4 + y//400 - y//100 + d + (153 * m + 8) // 5

        return abs(f(date1) - f(date2))

###############################################################################
"""
Solution 3: use datetime.datetime.strptime(date, "%Y-%m-%d").
"""
class Solution3:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        
        return abs((d2-d1).days)

###############################################################################

if __name__ == "__main__":
    def test(date1, date2, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(date1)
        print(date2)

        res = sol.daysBetweenDates(date1, date2)

        print(f"\nres = {res}")

    sol = Solution() # count days
    sol = Solution2() # count days w/ magic trick
    sol = Solution3() # use datetime.datetime.strptime(date, "%Y-%m-%d")

    comment = "LC ex1; answer = 1"
    date1 = "2019-06-29"
    date2 = "2019-06-30"
    test(date1, date2, comment)

    comment = "LC ex2; answer = 15"
    date1 = "2020-01-15"
    date2 = "2019-12-31"
    test(date1, date2, comment)

    comment = "LC test case; answer = 7699"
    date1 = "2023-01-13"
    date2 = "2044-02-11"
    test(date1, date2, comment)
