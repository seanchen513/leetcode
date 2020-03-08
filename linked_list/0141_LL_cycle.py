"""
141. Linked List Cycle
Easy

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_circular_ll

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###############################################################################
"""
Solution: use slow and fast pointers.

O(n) time
O(1) extra space
"""
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
                    
###############################################################################

if __name__ == "__main__":
    def test(arr, pos, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print()
        print(arr)
        print(f"pos = {pos}")

        head, _ = build_circular_ll(arr, pos)
        
        res = sol.hasCycle(head)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = True"
    head = [3,2,0,-4]
    pos = 1
    test(head, pos, comment)
    
    comment = "LC ex2; answer = True"
    head = [1,2]
    pos = 0
    test(head, pos, comment)
    
    comment = "LC ex3; answer = False"
    head = [1]
    pos = -1
    test(head, pos, comment)
    