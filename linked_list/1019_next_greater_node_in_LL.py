"""
1019. Next Greater Node In Linked List
Medium

We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

Example 1:

Input: [2,1,5]
Output: [5,5,0]

Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
 
Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_ll
from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###############################################################################
"""
Solution: use non-increasing stack.

0 1 2 3 4 index
2 7 4 3 5 values
7 0 5 5 0 answer

non-inc stack

        stack   stack
i   x   before  after
0   2   []      [2]
1   7   [2]     [7]     pop 2
2   4   [7]     [7,4]
3   3   [7,4]   [7,4,3]
4   5   [7,4,3] [7,5]   pop 3,4


O(n) time: each value is added and popped from stack at most once
O(n) extra space: for output and for stack
"""
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []

        i = 0

        while head:
            while stack and stack[-1][0] < head.val:
                _, k = stack.pop()
                res[k] = head.val

            stack.append((head.val, i)) # i == len(res)
            res.append(0)

            i += 1
            head = head.next

        return res

###############################################################################
"""
Solution 2: same idea, but convert LL to array and then process array.
"""
class Solution2:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # Convert linked list to array.
        arr = []
        cur = head

        while cur:
            arr.append(cur.val)
            cur = cur.next

        # Solve problem for array.
        res = [0] * len(arr)
        stack = []

        for i, x in enumerate(arr):
            while stack and stack[-1][0] < x:
                _, k = stack.pop()
                res[k] = x

            stack.append((x, i))
            
        return res

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        head, _ = build_ll(arr)

        print()
        print(head)
        
        res = sol.nextLargerNodes(head)

        print(f"\n{res}\n")


    sol = Solution()
    #sol = Solution2() # convert LL to array first
    
    comment = "LC ex1; answer = [5,5,0]"
    arr = [2,1,5]
    test(arr, comment)

    comment = "LC ex2; answer = [7,0,5,5,0]"
    arr = [2,7,4,3,5]
    test(arr, comment)

    comment = "LC ex3; answer = [7,9,9,9,0,5,0,0]"
    arr = [1,7,5,1,9,2,5,1]
    test(arr, comment)
