"""
148. Sort List
Medium

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

"""
dcp169

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode, build_ll

###############################################################################
"""
Solution: merge sort for linked list, recursive.

O(n log n) time
O(log n) extra space: for recursion
""" 
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if (head is None) or (head.next is None):
            return head

        # if even num nodes, middle should be first of two middle nodes
        middle = get_middle(head)
        right = middle.next
        middle.next = None

        head = self.sortList(head) # left half
        right = self.sortList(right) # right half

        return merge_sorted(head, right)
        #return merge_sorted_rec(head, right)

def merge_sorted_rec(l1, l2):
    if l2 is None:
        return l1
    
    if l1 is None:
        return l2

    if l1.val <= l2.val:
        l1.next = merge_sorted(l1.next, l2) 
        return l1
    else:
        l2.next = merge_sorted(l1, l2.next) 
        return l2

def merge_sorted(l1, l2):
    header = ListNode() # dummy header for merged list
    node = header

    while l1 and l2:
        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next

        node = node.next

    #node.next = l1 if l1 else l2
    node.next = l1 or l2

    return header.next

"""
Returns middle node (if odd number of nodes),
or the *first* node of the two middle ones (if even number of nodes).
"""
def get_middle(head: ListNode) -> ListNode:
    if head is None:
        return head

    slow = head # for readability; could use head directly instead
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

###############################################################################
"""
Solution 2: bottom-up mergesort for linked lists

O(n log n) time
O(1) extra space
"""
class Solution2:
    def sortList(self, head: ListNode) -> ListNode:    
        if (head is None) or (head.next is None):
            return head

        # get length of linked list
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        header = ListNode() # dummy header node
        header.next = head
        step = 1

        while step < n:
            curr = header.next
            tail = header

            while curr:
                left = curr
                right = split(left, step)
                curr = split(right, step)
                tail = merge(left, right, tail)

            #step *= 2
            step <<= 1

        return header.next

"""
Divide the linked list into two sublists, where the 1st one contains
k nodes.  Return the head of the 2nd sublist.
"""
def split(head, k):
    i = 1
    while i < k and head:
        head = head.next
        i += 1

    if not head:
        return None
    
    second = head.next
    head.next = None

    return second

"""
Merge linked lists l1 and l2, then append the merged list to
linked list given by head.  Return the tail.
"""
def merge(l1, l2, head):
    curr = head

    while l1 and l2:
        if l1.val > l2.val:
            curr.next = l2
            l2 = l2.next
        else:
            curr.next = l1
            l1 = l1.next

        curr = curr.next

    #curr.next = l1 if l1 else l2
    curr.next = l1 or l2
    
    while curr.next:
        curr = curr.next
    
    return curr

###############################################################################

if __name__ == "__main__":
    def test(arr, comment=None):
        print("="*80)
        if comment:
            print(comment)
        
        print(f"\narr = {arr}")

        head, _ = build_ll(arr)
        
        res = sol.sortList(head)

        print(f"\n{res}\n")


    sol = Solution()
    sol = Solution2() # bottom-up mergesort

    comment = "LC ex1"
    arr = [4,2,1,3]
    test(arr, comment)

    comment = "LC ex2"
    arr = [-1,5,3,4,0]
    test(arr, comment)
