"""
203. Remove Linked List Elements
Easy

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_ll

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###############################################################################
"""
Solution: iteration

Some cases:
1. empty list
2. multiple nodes in a row with target value
3. head node has target value
4. head node and 1+ nodes following it has target value
5. all nodes have target value
6. last node has target value
7. none of the nodes have target value

O(n) time
O(1) extra space
"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        header = ListNode() # dummy header node
        header.next = head
        
        pre = header # last node that doesn't have target value
        
        while head:
            if head.val == val:
                pre.next = head.next    
            else:
                pre = head # pre.next

            head = head.next
            
        return header.next

###############################################################################
"""
Solution 2: recursion

O(n) time
O(n) extra space: for recursion stack
"""
class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next

        return head

###############################################################################

if __name__ == "__main__":
    def test(arr, val, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        head, _ = build_ll(arr)

        print()
        print(head)
        print(f"val = {val}")

        res = sol.removeElements(head, val)

        print(f"\nAfter: {res}\n")


    sol = Solution() # iteration
    #sol = Solution2() # recursion
    
    comment = "LC ex1; answer = 1, 2, 5"
    arr = [1,2,6,3,4,5,6]
    val = 6
    test(arr, val, comment)
    
    comment = "multiple nodes at start, end, and middle with target value"
    arr = [6,6,6,1,2,6,6,3,4,5,6,6]
    val = 6
    test(arr, val, comment)
    
    comment = "all nodes have target value"
    arr = [5,5,5]
    val = 5
    test(arr, val, comment)
    
    comment = "single-node list with target value"
    arr = [5]
    val = 5
    test(arr, val, comment)

    comment = "empty list"
    arr = []
    val = 5
    test(arr, val, comment)
