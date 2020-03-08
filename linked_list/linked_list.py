"""
Linked list.

"""

class ListNode():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    # Assumes linked list is not circular.
    def __repr__(self):
        return f"{self.val}, {self.next.__repr__()}"

    # Needed for sorted merge of k sorted linked lists.
    def __lt__(self, other):
        return self.val < other.val

"""
Check if two given linked lists are equal.
"""
def ll_equals(l1: ListNode, l2: ListNode) -> bool:
    while l1 and l2:
        if l1.val != l2.val:
            return False
        
        l1 = l1.next
        l2 = l2.next

    if l1 or l2:
        return False

    return True

"""
Convert from linked list to array (Python list).
"""
def ll_to_array(head: ListNode) -> list:
    curr = head
    arr = []

    while curr:
        arr.append(curr.val)
        curr = curr.next

    return arr


"""
Build singly-linked list of length k, with values 1 through k
Returns both head and tail
"""
def build_ll_k(k: int) -> (ListNode, ListNode):
    if k == 0:
        return None, None

    head = ListNode(1)
    tail = head

    for i in range(2, k+1):
        tail.next = ListNode(i)
        tail = tail.next

    return head, tail

"""
Build singly-linked list using values from given iterator "it".
Returns both head and tail.

IDEAS:
1. option to return tail or not
2. option to build singly or doubly linked list
3. version where args are used as values; eg, build_ll(2,3,4,5)

"""
def build_ll(it) -> (ListNode, ListNode):
    if it is None:
        return None, None

    # works for dict and set, but it's probably not well-defined behavior
    if type(it) in [range, list]:
        it = iter(it)

    header = ListNode() # dummy header node
    tail = header

    val = next(it, None)
    while val is not None: # "is not None" is necessary since val might be 0
        tail.next = ListNode(val)
        tail = tail.next
        val = next(it, None)

    return header.next, tail

def build_dll(it) -> (ListNode, ListNode):
    if it is None:
        return None, None

    # works for dict and set, but it's probably not well-defined behavior
    if type(it) in [range, list]:
        it = iter(it)

    header = ListNode() # dummy header node
    tail = header

    val = next(it, None)
    while val is not None: # "is not None" is necessary since val might be 0
        tail.next = ListNode(val)
        tail.next.prev = tail # extra line needed for doubly linked list
        tail = tail.next
        val = next(it, None)

    header.next.prev = None # extra line needed for doubly linked list

    return header.next, tail

"""
"pos" represents the position (0-indexed) in the linked list where tail
connects to.  If pos is -1, then there is no cycle in the linked list.
"""
def build_circular_ll(it, pos: int) -> (ListNode, ListNode):
    head, tail = build_ll(it)

    if pos >= 0:
        node = head
        while pos > 0:
            node = node.next
            pos -= 1
        tail.next = node
            
    return head, tail

###############################################################################

# Does linked list have even number of nodes?
def even_num_nodes(head: ListNode) -> bool:
    fast = head
    while fast and fast.next:
        fast = fast.next.next

    #return False if fast else True

    if fast:
        return True

    return False

###############################################################################

"""
Reverses singly linked list in-place.
O(n) time.

Other names:
    lag = prev
    scout = temp

tail = head
prev = None
while head:
    temp = head.next
    head.next = prev
    prev = head
    head = temp
"""
def reverse_ll(head: ListNode) -> (ListNode, ListNode):
    tail = head # for return; not needed for algo
    lag = None
    
    # start of each loop: head = scout, and lag is behind by one node
    while head:
        # temp var to hold head.next, because head.next will be modified
        scout = head.next

        # reverse "next" pointer
        head.next = lag 
        
        # advance the pointers without using "next" fields
        lag = head
        head = scout

    return lag, tail


###############################################################################

"""
Used by ll_insertion_sort().
Inserts node into sorted position in sorted linked list given by head.
"""
def sorted_insert(head: ListNode, node: ListNode) -> ListNode:
    if (head is None) or (head.val > node.val):
        node.next = head
        head = node
    else:
        # find node such that: curr < new_node < curr.next
        curr = head
        while curr.next and (curr.next.val < node.val):
            curr = curr.next

        node.next = curr.next
        curr.next = node

        # if node.next is None:
        #     tail = node

    return head


def ll_insertion_sort(head: ListNode) -> ListNode:
    sorted = None # head of sorted linked list that we will build
    curr = head

    while curr:
        next = curr.next # save for later
        sorted = sorted_insert(sorted, curr)
        curr = next
    
    return sorted




###############################################################################

"""
Sorted merge of l1 and l2, each of which is sorted.
Don't create a new list.
Iterative version.
O(n) time, O(1) space
"""
def merge_sorted(l1: ListNode, l2: ListNode) -> ListNode:
    header = ListNode() # dummy header node for merged list
    curr = header

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            curr = l1
            l1 = l1.next
        else:
            curr.next = l2
            curr = l2
            l2 = l2.next

        #curr = curr.next

    curr.next = l1 if l1 else l2

    return header.next

"""
Sorted merge of l1 and l2, each of which is sorted.
Don't create a new list.
Recursive version.
O(n) time, O(1) space
"""
def merge_sorted_rec(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
        return l2
    
    if l2 is None:
        return l1

    if l1.val <= l2.val:
        l1.next = merge_sorted(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted(l1, l2.next)
        return l2

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

"""
LC876 easy - Middle of the Linked List

Returns middle node (if odd number of nodes),
or the *second* node of the two middle ones (if even number of nodes).
"""
def get_middle2(head: ListNode) -> ListNode:
    if head is None:
        return head

    slow = head # for readability; could use head directly instead
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

"""
Mergesort for linked list using recursion.
O(n log n) time
O(log n) extra space
"""
def ll_mergesort(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    middle = get_middle(head)
    right = middle.next
    middle.next = None

    head = ll_mergesort(head) # left half
    right = ll_mergesort(right) # right half

    return merge_sorted(head, right)

###############################################################################

def test_reverse():
    head, tail = build_dll(range(9, 0, -1))
    print(head)

    node = tail
    while node:
        print(node.val, end=", ")
        node = node.prev

    print()
    head, tail = reverse_ll(head)
    print(head)


def test_middle():
    head, _ = build_dll(range(1, 2))
    print(f"\nhead = {head}")

    mid = get_middle(head)
    print(f"mid = {mid}")

    #
    head, _ = build_dll(range(1, 3))
    print(f"\nhead = {head}")

    mid = get_middle(head)
    print(f"mid = {mid}")

    #
    head, _ = build_dll(range(1, 8))
    print(f"\nhead = {head}")

    mid = get_middle(head)
    print(f"mid = {mid}")

    #
    head, _ = build_dll(range(1, 9))
    print(f"\nhead = {head}")

    mid = get_middle(head)
    print(f"mid = {mid}")

def test_middle2():
    head, _ = build_dll(range(1, 2))
    print(f"\nhead = {head}")

    mid = get_middle2(head)
    print(f"mid = {mid}")

    #
    head, _ = build_dll(range(1, 3))
    print(f"\nhead = {head}")

    mid = get_middle2(head)
    print(f"mid = {mid}")

    #
    head, _ = build_dll(range(1, 8))
    print(f"\nhead = {head}")

    mid = get_middle2(head)
    print(f"mid = {mid}")

    #
    head, _ = build_dll(range(1, 9))
    print(f"\nhead = {head}")

    mid = get_middle2(head)
    print(f"mid = {mid}")


###############################################################################

if __name__ == "__main__":
    #test_reverse()
    test_middle()
    #test_middle2()

    # head = ll_insertion_sort(head)
    # print(head)




