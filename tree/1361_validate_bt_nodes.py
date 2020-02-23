"""
1361. Validate Binary Tree Nodes
Medium

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Example 4:

Input: n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output: false

Constraints:

1 <= n <= 10^4
leftChild.length == rightChild.length == n
-1 <= leftChild[i], rightChild[i] <= n - 1
"""

from typing import List
import collections

"""
ex1: every pos # shows up exactly once in combined child arrays, except root 0

ex2: two parents for 3... 3 shows up in both leftChild and rightChild

ex3: cycle 0 <-> 1 within leftChild

ex4: 3 is also a root, it doesn't show in either arrays

summary:

every number from 1 to len(leftChild) - 1 shows up exactly once
no 0 in leftChild or rightChild

Q:
does 0 have to be the root?

Cycles?
0 -> 1 -> 2 -> 0
leftChild = [1, 2, 0]

0 -> 1 -> 2 -> 3 -> 1
leftChild = [1, 2, 3, 1]

If assume 0 is the root, then to check that there are no cycles, it is a 
necessary but not sufficient condition that all other nodes have exactly 
one parent, and that 0 has no parent.  Ie, all positive value appear exactly 
once, and 0 doesn't appear.  However, also need to check that the positive 
numbers are in valid positions.

Example: leftChild = [-1,1,2,3]
Positive numbers appear exactly once, but have 3 components, each a self-loop.

Example: leftChild = [1,2,3,-1] is a valid BT.
Example: leftChild = [3,2,1,-1] has 2 components, 

If we don't assume 0 is the root, we can try checking that there are exactly
n-1 unique values other than -1.  But we also need to check that the positions
are valid.

Example: leftChild = [1,2,0,-1] has n-1 = 3 unique values, but is a cycle.

"""
###############################################################################
"""
Solution: Find if there is only one possible root first, then use BFS traversal
to check if we can visit all nodes from that root.  
Use set to track seen elements.

I posted here:
https://leetcode.com/problems/validate-binary-tree-nodes/discuss/518458/Python3-Check-if-there-is-only-one-possible-root-then-use-BFS-to-try-to-visit-all-nodes

O(n) time
O(n) extra space: for set.

Runtime: 308 ms, faster than 100.00% of Python3 online submissions
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions
""" 
class Solution:
    def validateBinaryTreeNodes(self, 
        n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        # First, check for a root, ie, a node with no parents.
        # At the same time, check the necessary condition that there must be
        # exactly n-1 unique nonnegative values.  The root is the missing
        # nonnegative value.
        seen = set()
        
        for arr in (leftChild, rightChild):
            for x in arr:
                if x != -1:
                    if x in seen: # has two parents
                        return False
                    seen.add(x)

        # If == n, then every node has a parent, so there are no roots.
        # If < n - 1, then there are more than one parentless node (ie, root),
        # or there are nodes with more than one parent (already returned).
        if len(seen) != n - 1:
            return False

        root = (set(range(n)) - seen).pop() # only one possible element
        #print(f"root = {root}")

        # Note: we still might have cases with:
        # - more than one component
        # - cycles
        # However, the component with the root cannot have a cycle.  
        # If it did, there would be a node with two parents (a case we
        # already eliminated), or the root would have a parent (impossible
        # by how we picked a root by definition).  Self-cycles are also
        # eliminated.  Therefore, if we're able to visit every node from the 
        # root, then this implies there is only one component and that there 
        # are no cycles.

        # Now, check if we can visit all nodes from the root, using BFS.
        # Instead of using a set, can just use a simple counter (or decrement n
        # and check if it's 0 at the end) since we already checked uniqueness.
        q = collections.deque([root])

        while q:
            x = q.popleft()
            n -= 1

            if leftChild[x] != -1:
                q.append(leftChild[x])
            if rightChild[x] != -1:
                q.append(rightChild[x])

        # If n == 0, then we visited n nodes.
        return True if n == 0 else False

###############################################################################
"""
NOT Solution: use set...  This passes OJ, though.

Don't assume the root has to be 0.

O(n) time
O(n) extra space
"""
class SolutionNOT:
    def validateBinaryTreeNodes(self, 
        n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        s = set()
        
        for x in leftChild:
            if x != -1:
                if x in s:
                    return False

                s.add(x)

        for x in rightChild:
            if x != -1:
                if x in s:
                    return False

                s.add(x)

        if len(s) != n - 1:
            return False

        return True            

###############################################################################

if __name__ == "__main__":
    def test(n, leftChild, rightChild, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(f"n = {n}")
        print(f"leftChild = {leftChild}")
        print(f"rightChild = {rightChild}")

        res = sol.validateBinaryTreeNodes(n, leftChild, rightChild)

        print(f"\nres = {res}")


    sol = Solution() # traversal, with set to track seen elements.
    #sol = SolutionNOT() # use set
    #sol = Solution2() #

    comment = "LC ex1; answer = True"
    n = 4
    leftChild = [1,-1,3,-1]
    rightChild = [2,-1,-1,-1]
    test(n, leftChild, rightChild, comment)

    comment = "LC ex2; answer = False"
    n = 4
    leftChild = [1,-1,3,-1]
    rightChild = [2,3,-1,-1]
    test(n, leftChild, rightChild, comment)

    comment = "LC ex3; answer = False"
    n = 2
    leftChild = [1,0]
    rightChild = [-1,-1]
    test(n, leftChild, rightChild, comment)

    comment = "LC ex4; answer = False"
    n = 6
    leftChild = [1,-1,-1,4,-1,-1]
    rightChild = [2,-1,-1,5,-1,-1]
    test(n, leftChild, rightChild, comment)
    
    comment = "Has cycle 0->1->2->0"
    n = 4
    leftChild = [1,2,0,-1]
    rightChild = [-1,-1,-1,-1]
    test(n, leftChild, rightChild, comment)
    
    comment = "Has cycle 0->1->0"
    n = 3
    leftChild = [1,0,-1]
    rightChild = [-1,-1,-1]
    test(n, leftChild, rightChild, comment)

    comment = "Has cycle 1->2->1"
    n = 4
    leftChild = [1,2,1,-1]
    rightChild = [-1,-1,-1,-1]
    test(n, leftChild, rightChild, comment)

    comment = "answer = False"
    n = 3
    leftChild = [2, 1, -1]
    rightChild = [-1, -1, -1]
    test(n, leftChild, rightChild, comment)

    comment = "answer = False"
    n = 3
    leftChild = [1,0,-1]
    rightChild = [-1,-1,-1]
    test(n, leftChild, rightChild, comment)

    comment = "answer = False"
    n = 4
    leftChild = [1, -1, -1, -1]
    rightChild = [2, -1, -1, -1]
    test(n, leftChild, rightChild, comment)
    
    comment = "answer = False"
    n = 4
    leftChild = [1, -1, 3, -1]
    rightChild = [-1, -1, -1, 2]
    test(n, leftChild, rightChild, comment)

    comment = "answer = True"
    n = 3
    leftChild = [2, 0, -1]
    rightChild = [-1, -1, -1]
    test(n, leftChild, rightChild, comment)

    comment = "trivial case; answer = True"
    n = 1
    leftChild = [1]
    rightChild = [-1]
    test(n, leftChild, rightChild, comment)

    comment = "trivial case w/ self-loop; answer = False"
    n = 1
    leftChild = [0]
    rightChild = [-1]
    test(n, leftChild, rightChild, comment)
