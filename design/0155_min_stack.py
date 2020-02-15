"""
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 
Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

###############################################################################
"""
Solution: store running min with each element that is pushed.  Otherwise, 
would have to recalculate min after an element was popped, which is O(n).
"""
class MinStack:
	def __init__(self):
		self.stack = []
		#self.min = float('inf')

	def push(self, x: int) -> None:
		m = min(self.stack[-1][1], x) if self.stack else x		
		self.stack.append((x, m))
		
	# Assume stack is not empty.
	def pop(self) -> None:
		self.stack.pop()

	def top(self) -> int:
		return self.stack[-1][0] if self.stack else None

	def getMin(self) -> int:
		return self.stack[-1][1] if self.stack else None

###############################################################################

if __name__ == "__main__":
	def test(s, comment=None):
		print("="*80)
		if comment:
			print(comment)
		print()

		print("Pushing -2, 0, -3")
		s.push(-2)
		s.push(0)
		s.push(-3)
		
		m = s.getMin()
		print(f"min = {m}")
		
		print("Popping...")
		s.pop()
		
		t = s.top()
		print(f"top = {t}")

		m = s.getMin()
		print(f"min = {m}")


	stack = MinStack()

	comment = "LC example"
	test(stack, comment)
