"""
716. Max Stack
Easy

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.

Example 1:

MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

 ###############################################################################
"""
Solution: Inherit from list.  
Store running max with each element that is pushed.

Use 2nd stack/list when doing popMax(), and use the class' own push() to push 
elements from 2nd stack/list back onto the main stack so that their running 
maxes will be re-calculated.

O(n) time for popMax().
O(1) time for others.

O(n) extra space.
"""
class MaxStack(list):
	def __init__(self):
		pass

	def push(self, x: int) -> None:
		m = max(self[-1][1], x) if self else x		
		self.append((x, m))
		
	# Assume stack is not empty.
	def pop(self) -> int:
		#return self.pop() # doesn't work
		return list.pop(self)[0]

	def top(self) -> int:
		return self[-1][0] if self else None
		
	def peekMax(self) -> int:
		return self[-1][1] if self else None
		
	def popMax(self) -> int:
		m = self[-1][1]
		s = [] # 2nd stack to use temporarily

		while self[-1][0] != m:
			s.append(self.pop())
		
		self.pop()

		# Using self.push also adds updated maxes for each one.
		#map(self.push, reversed(s)) # failed LC test case
		while s:
			self.push(s.pop())
		
		return m

###############################################################################

if __name__ == "__main__":
	def test(s, comment=None):
		print("="*80)
		if comment:
			print(comment)
		print()

		print("pushing 5, 1, 5")
		s.push(5)
		s.push(1)
		s.push(5)
		
		t = s.top()
		print(f"top = {t}")
		
		#print("popMax...")
		m = s.popMax()
		print(f"popMax = {m}")
		
		t = s.top()
		print(f"top = {t}")

		m = s.peekMax()
		print(f"max = {m}")

		#print("Popping...")
		p = s.pop()
		print(f"popped = {p}")
		
		t = s.top()
		print(f"top = {t}")

	def test2(s, comment=None):
		print("="*80)
		if comment:
			print(comment)
		print()

		print("pushing 5, 1")
		s.push(5)
		s.push(1)
		
		#print("popMax...")
		m = s.popMax()
		print(f"popMax = {m}")
		
		m = s.peekMax()
		print(f"max = {m}")


	comment = "LC example"
	stack = MaxStack()
	test(stack, comment)

	comment = "LC test case"
	stack = MaxStack()
	test2(stack, comment)
