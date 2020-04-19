"""
1418. Display Table of Food Orders in a Restaurant
Medium

Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.

Example 1:

Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
Explanation:
The displaying table looks like:
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
For the table 5: Carla orders "Water" and "Ceviche".
For the table 10: Corina orders "Beef Burrito". 

Example 2:

Input: orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
Output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
Explanation: 
For the table 1: Adam and Brianna order "Canadian Waffles".
For the table 12: James, Ratesh and Amadeus order "Fried Chicken".

Example 3:

Input: orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
Output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
 
Constraints:

1 <= orders.length <= 5 * 10^4
orders[i].length == 3
1 <= customerNamei.length, foodItemi.length <= 20
customerNamei and foodItemi consist of lowercase and uppercase English letters and the space character.
tableNumberi is a valid integer between 1 and 500.
"""

from typing import List
import collections

###############################################################################
"""
Solution: use list of dicts. Use sets to track unique foods and tables,
and sort them. Then build result.

d[table][food] = count

O(n + T log T + F log F) time, where n is num orders, T is num tables, and F is num foods
O(T * F) extra space

"""
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = [collections.defaultdict(int) for _ in range(501)]
        tables = set()
        foods = set()

        for _, tb, food in orders:
            d[int(tb)][food] += 1
            tables.add(int(tb))
            foods.add(food)

        tables = sorted(tables) 
        foods = sorted(foods)

        res = [["Table"] + foods ] # start with header

        for t in tables:
            row = [str(t)]
            dt = d[t]
            
            for f in foods:
                row.append(str(dt[f]))
            
            res.append(row)
            
        return res

"""
Solution 2: same, but use dict of dicts. Use set to track unique foods.
Sort foods. Then build result, processing tables and foods in sorted order.

d[table][food] = count
"""
class Solution2:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = collections.defaultdict(collections.Counter)
        foods = set()

        for _, tb, food in orders:
            d[tb][food] += 1
            foods.add(food)

        foods = sorted(foods)

        res = [["Table"] + foods ] # start with header

        for tb in sorted(d, key=int):
            row = [tb]
            dt = d[tb]
            
            for f in foods:
                row.append(str(dt[f]))
            
            res.append(row)
            
        return res

###############################################################################

if __name__ == "__main__":
    def test(orders, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\norders = {orders}")

        res = sol.displayTable(orders)

        print(f"\nres = {res}\n")


    sol = Solution()
    sol = Solution2() # use dict of dicts

    comment = "LC ex1; answer = "
    orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
    test(orders, comment)

    comment = "LC ex2; answer = "
    orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
    test(orders, comment)

    comment = "LC ex3; answer = "
    orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
    test(orders, comment)
    