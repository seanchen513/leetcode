"""
328. Odd Even Linked List
Medium

Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_ll

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

###############################################################################
"""
Solution:

Iterate on "even and even.next".
"odd" stops at tail of odd linked list.

Relative order of nodes preserved.

O(n) time, single pass
O(1) extra space
"""
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # alternatively, if not head or not head.next: return head
        if not head:
            return None

        odd = head
        even = head.next
        even_head = even

        while even and even.next: # 2 and 2.next (3)
            odd.next = even.next # 1.next = 3
            odd = odd.next # 1 becomes 3

            even.next = odd.next # 2.next = 3.next = 4 or None
            even = even.next # 2 becomes 4 or None

        """
        If even number of nodes, "while" loop stops when "even.next" is None.
        Afterwards, "even" is tail of orig list, and "odd" is node just before tail.
        The even list is auto terminated with None since "even" stopped at the
        tail of the orig list.

        1 -> 2 -> 3 -> 4 -> None
                 odd  even  even.next

        ###
        If odd number of nodes, "while" loop stops when "even" is None.
        Afterwards, "odd" is tail of orig list, and "even" is None.
        The "even" list was terminated with None.
        
        1 -> 2 -> 3 -> None
                 odd   even
        """

        # In both cases, "odd" is tail of odd linked list.
        odd.next = even_head 

        return head

###############################################################################
"""
Solution 2:

O(n) time, single pass
O(1) extra space
"""
class Solution2:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # alternatively, if not head or not head.next: return head
        if not head: 
            return None
        
        odd = head
        even = head.next
        even_head = even
        prev_odd = None
        
        while odd and even: # 1 and 2
            odd.next = even.next # 1.next = 2.next = 3
            
            prev_odd = odd
            odd = odd.next # 1 becomes 3 or None
            
            if odd: # 3 exists
                even.next = odd.next # 2.next = 3.next = 4
                even = even.next # 2 becomes 4

        # Two cases:
        # odd None: 1 2 None, odd = None, even = 2
        # even None: 1 2 3 None, odd = 3, even = None
        
        if odd:
            odd.next = even_head
        else:
            prev_odd.next = even_head
        
        return head
        

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)

        head, _ = build_ll(arr)

        print(f"\narr = {arr}")

        res = sol.oddEvenList(head)

        print(f"\nres = {res}\n")


    sol = Solution() # 
    #sol = Solution2() # 

    comment = "LC ex1; answer = 1 3 5 2 4"
    arr = [1,2,3,4,5]
    test(arr, comment)

    comment = "LC ex2; answer = 2 3 6 7 1 5 4"
    arr = [2,1,3,5,6,4,7]
    test(arr, comment)

    comment = "LC TC; answer = None"
    arr = []
    test(arr, comment)

    comment = "; answer = 1"
    arr = [1]
    test(arr, comment)

    comment = "; answer = 1 2"
    arr = [1, 2]
    test(arr, comment)

    comment = "; answer = 1 3 2"
    arr = [1, 2, 3]
    test(arr, comment)

    comment = "; answer = 1 3 2 4"
    arr = [1, 2, 3, 4]
    test(arr, comment)
