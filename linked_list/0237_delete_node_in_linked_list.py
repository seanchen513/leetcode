"""
237. Delete Node in a Linked List
Easy

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linked_list import ListNode, build_ll

###############################################################################
"""
Solution 1: copy over next node's value, and set node.next to node.next.next,
skipping over the next node.

O(1) time
O(1) space
"""
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

###############################################################################
"""
Solution 2: starting with given node, copy over next node's value. To delete
the tail node, we want access to the node before the tail node. One way to
do this is to track "prev", the node before the current "node".

Given node isn't actually deleted. We're just copying over values, and
deleting the tail node instead. Since this is Python, we delete a node by
just setting the previous node's "next" field to None.

O(n) time
O(1) space
"""
class Solution2:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next: # ie, not the tail
            node.val = node.next.val
            prev = node
            node = node.next
        
        # We're given that the given node is not the tail, so the loop
        # iterates at least once, and "prev" becomes defined.

        # "node" is now the tail
        # "prev" is the node before the tail

        prev.next = None

###############################################################################

if __name__ == "__main__":
    def test(arr, node_val, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        print(arr)

        head, _ = build_ll(arr)
        print(head)
        print(f"\nhead = {head}")

        node = head
        while node.val != node_val:
            node = node.next
        print(f"\nnode value = {node_val}")

        sol.deleteNode(node)

        print(head)
        print()


    sol = Solution() # copy over next node's value, and set node.next to skip over next node
    #sol = Solution2() # shift over values of all nodes to right, and delete tail

    comment = "LC ex1; answer = [4,1,9]"
    arr = [4,5,1,9]
    node_val = 5
    test(arr, node_val, comment)

    comment = "LC ex2; answer = [4,5,9]"
    arr = [4,5,1,9]
    node_val = 1
    test(arr, node_val, comment)
