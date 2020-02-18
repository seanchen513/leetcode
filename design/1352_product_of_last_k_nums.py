"""
1352. Product of the Last K Numbers
Medium

Implement the class ProductOfNumbers that supports two methods:

1. add(int num)

Adds the number num to the back of the current list of numbers.
2. getProduct(int k)

Returns the product of the last k numbers in the current list.
You can assume that always the current list has at least k numbers.
At any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
 
Constraints:

There will be at most 40000 operations considering both add and getProduct.
0 <= num <= 100
1 <= k <= 40000
"""

from typing import List
import collections
import functools

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

###############################################################################
"""
Solution: Keep list of numbers added and list of running products.

Start list of running products with dummy 1 to simplify code.
Reset list of running products to [1] if 0 is added.

add(): O(1) time
getProduct(): O(1) time

Note: Don't need self.q or self.q.append(num) to pass LC submission, but
it's part of the problem statement.

Runtime: 304 ms, faster than 71.02% of Python3 online submissions
Memory Usage: 28 MB, less than 100.00% of Python3 online submissions
"""
class ProductOfNumbers:
	def __init__(self):
		self.q = [] # list of numbers added
		self.p = [1] # list of running products
		
	def add(self, num: int) -> None:
		self.q.append(num)

		if num == 0: # reset the list of running products
			self.p = [1] # Use a dummy 1.
		else:
			self.p.append(num * self.p[-1])

	def getProduct(self, k: int) -> int:
		if k >= len(self.p):
			return 0

		return self.p[-1] // self.p[-1-k]

"""
Example:
2 3 4 5

2 6 24 120

n = len(p) = 4

last k=1: 5 = 120 // 24 = p[-1] // p[-2] = p[-1] // p[2]
last k=2: 20 = 120 // 6 = p[-1] // p[-3] = p[-1] // p[1]
last k=3: 60 = 120 // 2 = p[-1] // p[-4] = p[-1] // p[0]
last k=4: 120 = 120 // 1 = p[-1]

last k: p[-1] // p[-k-1] = p[-1] // p[n-k-1]

Example: START WITH DUMMY 1.
2 3 4 5

*1* 2 6 24 120

n = len(p) = 5

last k=1: 5 = 120 // 24 = p[-1] // p[-2] = p[-1] // p[3]
last k=2: 20 = 120 // 6 = p[-1] // p[-3] = p[-1] // p[2]
last k=3: 60 = 120 // 2 = p[-1] // p[-4] = p[-1] // p[1]
last k=4: 120 = 120 // 1 = p[-1] // p[-5] = p[-1] // p[0]

last k: p[-1] // p[-k-1] = p[-1] // p[n-k-2]
"""

###############################################################################
"""
Solution 2: original contest code.

Runtime: 312 ms, faster than 67.48% of Python3 online submissions
Memory Usage: 28.5 MB, less than 100.00% of Python3 online submissions
"""
class ProductOfNumbers2:
	def __init__(self):
		self.q = [] # list of numbers added
		self.p = [1] # list of running products
		self.last_zero = None
		
	def add(self, num: int) -> None:
		self.q.append(num)

		if num == 0:
			self.last_zero = len(self.q)

		if self.p:
			if self.p[-1] == 0:
				self.p.append(num)
			else:
				self.p.append(num * self.p[-1])
		else:
			self.p.append(num)

	def getProduct(self, k: int) -> int:
		if not self.p:
			return 0

		if k == 1:
			return self.q[-1]

		if self.last_zero and (len(self.q) - self.last_zero == k):
			return self.p[-1]

		if self.last_zero and (len(self.q) - self.last_zero < k):
			return 0

		return self.p[-1] // self.p[-1-k]

"""
Example:
2 3 4 5

*1*, 2 6 24 120

n = len(p) = len(q) + 1 = 5

last 1 - 5 = 120//24 = p[-1] // p[3]
last 2 - 20 = 120 // 6 = p[-1] // p[2]
last 3 - 60 = 120 // 2 = p[-1] // p[1]
last 4 - 120 = 120 // 1 = p[-1] // p[0]

last k = p[-1] // p[n-k-1]
"""

"""
Example:
3 0 2 5 4
3 0 0 0 0

modified: restart running product after a 0
3 0 2 10 40

last_zero = 2 (len of q at time of 0)
len(q) = 5

last 4 - 0: len(q) - last_zero = 5 - 2 = 3 < k
last 3 - 40 = 40//1 = NO... p[-1] // (p[-1-3]==0)
last 2 - 20 = 40//2 = p[-1] // p[-1-2]
last 1 - 4 = 40//10 = p[-1] // p[-1-1]
"""

###############################################################################

if __name__ == "__main__":
	p = ProductOfNumbers()

	p.add(3) # [3]
	p.add(0) # [3,0]
	p.add(2) # [3,0,2]
	p.add(5) # [3,0,2,5]
	p.add(4) # [3,0,2,5,4]
	
	res = p.getProduct(2) # 5 * 4 = 20
	print(f"res = {res}")
	
	res = p.getProduct(3) # 2 * 5 * 4 = 40
	print(f"res = {res}")
	
	res = p.getProduct(4) # 0 * 2 * 5 * 4 = 0
	print(f"res = {res}")

	p.add(8) # [3,0,2,5,4,8]
	
	res = p.getProduct(2) # 4 * 8 = 32 
	print(f"res = {res}")
