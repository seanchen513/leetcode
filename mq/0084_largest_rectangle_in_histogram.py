"""
84. Largest Rectangle in Histogram
Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

from typing import List

###############################################################################
"""
Solution: use stack of indices with increasing heights.

When a lower height is encountered, it forms the outside right boundary of
any rectangles we will consider. Each index popped from the stack represents
a bar with a height, and is associated with a rectangle of that same height.
The outside left border of this rectangle is the index now on top of the stack.

This rectangle is trivial (the bar itself, so has width 1) if the top of the 
stack represents the bar to the immediate left of the current bar.
However, the top of the stack might represent a bar further to the left if
there were intermediate bars that disrupted the increasing height pattern.

Eg, 1 5 6 2 3. 

O(n) time
O(n) extra space: for stack

References:
https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
https://www.informatik.uni-ulm.de/acm/Locals/2003/html/histogram.html
https://www.informatik.uni-ulm.de/acm/Locals/2003/html/judge.html

"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        mx = 0

        stack = [] # holds indices

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                ht = heights[stack.pop()]
                left = stack[-1] if stack else -1

                mx = max(mx, ht * (i - left - 1))

            stack.append(i)

        while stack:
            ht = heights[stack.pop()]
            left = stack[-1] if stack else -1

            mx = max(mx, ht * (n - left - 1))

        return mx

"""
Solution 1b: same, but use dummy values: start stack with -1, and append 0
to heights.

1. Start stack with dummy value of -1 to avoid having to check if the stack is
empty in the loop condition and when setting "left". This value of -1 represents
the outside left border of any rectangle calculated in the last iteration.

This dummy value is never popped: if stack[-1] is -1, then 
heights[stack[-1]] = heights[-1] is 0, 
and no element in heights satisfies heights[i] < 0.
Therefore, the loop isn't entered.

2. Temporarily append 0 to input array "heights". This allows us to have
just a single loop. In the last iteration, i = n and heights[i] = 0.
Therefore, the condition heights[i] < heights[stack[-1]] is satisfied for
all remaining elements on the stack except for the dummy value of stack[0] = -1.

https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms

"""
class Solution1b:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights) + 1
        mx = 0

        heights.append(0) # add temporary dummy value of 0
        stack = [-1] # holds indices; -1 is dummy value

        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                ht = heights[stack.pop()]

                # outside right boundary is i
                # outside left boundary is stack[-1]
                width = i - stack[-1] - 1 

                mx = max(mx, ht * width)

            stack.append(i)

        heights.pop() # remove temporary dummy value

        return mx

"""
LC example:
2 1 5 6 2 3 | 0

stack = [-1]

        stack
i   h   before    after
0   2   -1       -1 0(2)              don't enter loop
1   1   -1 0     -1 1(1)              pop 0, h=2, w=1-(-1)-1=1, area=2*1=2
2   5   -1 1     -1 1(1) 2(5)
3   6   -1 1 2   -1 1(1) 2(5) 3(6)

4   2            -1 1(1) 2(5)         pop 3, h=6, w=4-(2)-1=1, area=6*1=6
                 -1 1(1) 4(2)         pop 2, h=5, w=4-(1)-1=2, area=5*2=10

5   3            -1 1(1) 4(2) 5(3)

6   0*           -1 1(1) 4(2)         pop 5, h=3, w=6-(4)-1=1, area=3*1=3
                 -1 1(1)              pop 4, h=2, w=6-(1)-1=4, area=2*4=8
                 -1                   pop 1, h=1, w=6-(-1)-1=6, area=1*6=6

    
"""

###############################################################################
"""
Solution 2: precalculate for each bar how many bars to left and right are
higher. Traverse forward for "left", and traverse backwards for "right".
These precalculations can be done in O(n) time by making use of previous
calculations and index jumping.

O(n) time
O(n) extra space

https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28963/Python-solution-without-using-stack.-(with-explanation)
"""
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # How many bars to the left/right are higher than current bar,
        # Default value 1 is for the current bar itself.
        left = [1] * n
        right = [1] * n
        mx = 0

        # calculate left
        for i in range(1, n):
            j = i - 1

            while j >= 0:
                if heights[j] < heights[i]:
                    break

                left[i] += left[j]
                j -= left[j]

        # calculate right
        for i in range(n-2, -1, -1):
            j = i + 1

            while j < n:
                if heights[j] < heights[i]:
                    break

                right[i] += right[j]
                j += right[j]

        print(f"\nleft = {left}")
        print(f"right = {right}")

        for i in range(n):
            mx = max(mx, heights[i] * (left[i] + right[i] - 1))

        return mx

"""
LC example:
2 1 5 6 2 3

1 2 1 1 3 1 left
1 5 2 1 2 1 right

How left is calculated:

i       
0   2   left[0] = 1
1   1   left[1] += left[0], so left[1] = 1 + 1 = 2

2   5   left[2] = 1, don't add anything since bar to left is lower   

3   6   left[3] = 1, don't add anything since bar to left is lower

4   2   j = 3:
        left[4] += left[3], so left[4] = 1 + 1 = 2 (this bar 4 and 6)
        j -= left[j], ie, j = 3 - left[3] = 3 - 1 = 2
        heights[2] = 5
        
        j = 2:
        left[4] += left[2], so left[4] = 2 + 1 = 3
        j -= left[j], ie, j = 2 - left[2] = 2 - 1 = 1
        heights[1] = 1 is lower than 2, so stop

5   3   j = 4:
        left[5] = 1, don't add anything since bar to left is lower

"""

###############################################################################
"""
NOT DONE
Solution 3: divide & conquer

O(n log n) time
O() space

https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28910/Simple-Divide-and-Conquer-AC-solution-without-Segment-Tree
https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1

"""
class Solution3:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass

###############################################################################
"""
NOT DONE
Solution 4: segment tree

O(n log n) time
O() space

https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28941/Segment-tree-solution-just-another-idea-O(N*logN)-Solution

"""
class Solution4:
    def largestRectangleArea(self, heights: List[int]) -> int:
        pass

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
              
        print(f"\nheights = {arr}")

        res = sol.largestRectangleArea(arr)

        print(f"\nresult = {res}\n")


    sol = Solution() # increasing stack
    sol = Solution1b() # same, but w/ dummy values
    
    sol = Solution2() # precalc left and right bars higher than current

    comment = "LC example; answer = 10"
    arr = [2,1,5,6,2,3]
    test(arr, comment)

    comment = "LC example; answer = 1"
    arr = [1]
    test(arr, comment)

    comment = "LC TC; answer = 3"
    arr = [2,1,2]
    test(arr, comment)

    comment = "g4g; answer = 12"
    arr = [6,2,5,4,5,1,6]
    test(arr, comment)
