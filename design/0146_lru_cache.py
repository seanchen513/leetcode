"""
146. LRU Cache
Medium

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

import sys
sys.path.insert(1, '../../leetcode/linked_list/')

from linked_list import ListNode
import collections

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

###############################################################################
"""
Solution 1: use dict to hold key/value pairs, and use doubly linked list to
hold order of keys.

Can do:
- Can use dummy head and tail for linked list.
- Linked list helper methods.

get(): O(1) time
put(): O(1) 

O(capacity) extra space: for dict and doubly linked list

Runtime: 204 ms, faster than 66.84% of Python3 online submissions
Memory Usage: 22.5 MB, less than 6.06% of Python3 online submissions
"""
# class ListNode():
#     def __init__(self, val=None, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev

class LRUCache:
    def __init__(self, capacity: int): # Assume capacity > 0
        self.d = {}
        self.head = None 
        self.tail = None
        self.capacity = capacity        

    def __repr__(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(str(curr.val))
            curr = curr.next

        return '->'.join(arr)

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        val, node = self.d[key]
        
        if self.tail == node:
            return val

        if self.head == node and node.next:
            self.head = node.next
        
        # Remove node from doubly linked list.
        temp = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = temp

        # Add node to end of doubly linked list.
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.get(key) # desired side effect of moving node to end of DLL
            self.d[key][0] = value
            return

        if len(self.d) == self.capacity: # Assume > 0
            k = self.head.val
            del self.d[k]

            self.head = self.head.next
            if self.head:
                self.head.prev = None
                    
        node = ListNode(key)

        if not self.tail: # linked list is empty
            self.head = self.tail = node
        else: # add node to end of linked list
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.d[key] = [value, node]

"""
Solution 1b: same as sol 1, but use self as dummy head and tail of doubly
linked list.
"""
class LRUCache1b:
    def __init__(self, capacity: int): # Assume capacity > 0
        self.d = {}
        self.prev = self.next = self # self as dummy head and tail of DLL
        self.capacity = capacity        

    def __repr__(self):
        arr = []
        curr = self.next
        while curr != self:
            arr.append(str(curr.val))
            curr = curr.next

        return '->'.join(arr)

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        val, node = self.d[key]

        if self.prev != node: # if node isn't already tail of DLL
            # Move node with key value to end of DLL.
            self._remove(node)
            self._add(node)

        return val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            _, node = self.d[key]

            if self.prev != node: # if node isn't already tail of DLL
                # Move node with key value to end of DLL.
                self._remove(node)
                self._add(node)

            self.d[key][0] = value
            return

        if len(self.d) == self.capacity: # Assume > 0
            node = self.next # first node of DLL
            del self.d[node.val]
            self._remove(node) # remove first node of DLL
            node.val = key
        else:        
            node = ListNode(key)

        self._add(node)
        self.d[key] = [value, node]

    """
    Add given node to end of doubly linked list.

    p - node - self
    """
    def _add(self, node):
        p = self.prev
        p.next = node
        node.prev = p
        node.next = self
        self.prev = node

    """
    Remove given node from doubly linked list.

    p - node - n
    """
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

###############################################################################
"""
Solution 2: use dict to hold key/value pairs, and use deque to hold order of
keys.

get(): O(n) time if key already in cache, else O(1)
put(): O(n) time if key already in cache, else O(1)

O(capacity) extra space: for dict and deque

Runtime: 604 ms, faster than 10.39% of Python3 online submissions
Memory Usage: 22.3 MB, less than 6.06% of Python3 online submissions
"""
class LRUCache2:
    def __init__(self, capacity: int): # Assume capacity > 0
        self.d = {}
        self.keys = collections.deque([])
        self.capacity = capacity        

    def __repr__(self):
        return '->'.join(map(str, self.keys))

    def get(self, key: int) -> int:
        if key in self.d:
            self.keys.remove(key)
            self.keys.append(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:            
            self.keys.remove(key)
        elif len(self.d) == self.capacity: # Assume > 0
            k = self.keys.popleft()
            del self.d[k]
        
        self.d[key] = value
        self.keys.append(key)

###############################################################################
"""
Solution 3: use collections.OrderedDict().

O(1) time for get() and put()
O(capacity) extra space

Runtime: 176 ms, faster than 93.35% of Python3 online submissions
Memory Usage: 22.2 MB, less than 9.09% of Python3 online submissions
"""
class LRUCache3:
    def __init__(self, capacity: int): # Assume capacity > 0
        self.d = collections.OrderedDict()
        self.capacity = capacity        

    def __repr__(self):
        return '->'.join(map(str, self.d))

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:            
            self.d.move_to_end(key)
        elif len(self.d) == self.capacity: # Assume > 0
            self.d.popitem(last=False)
        
        self.d[key] = value

"""
Solution 3b: same as sol 3, but inherit from OrderedDict instead of having
an instance of it as a class member.

Runtime: 172 ms, faster than 97.24% of Python3 online submissions
Memory Usage: 22.2 MB, less than 7.57% of Python3 online submissions
"""
class LRUCache3b(collections.OrderedDict):
    def __init__(self, capacity: int): # Assume capacity > 0
        self.capacity = capacity        

    def __repr__(self):
        return '->'.join(map(str, self))

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self:            
            self.move_to_end(key)
        elif len(self) == self.capacity: # Assume > 0
            self.popitem(last=False)
        
        self[key] = value

###############################################################################

if __name__ == "__main__":
    #cache = LRUCache(2) # use dict and doubly linked list
    cache = LRUCache1b(2) # use dict and DLL; self of DLL is dummy head/tail
    
    #cache = LRUCache2(2) # use dict and deque
    
    #cache = LRUCache3(2) # use collections.OrderedDict
    #cache = LRUCache3b(2) # inherit from OrderedDict
    
    ### LC146 example
    cache.put(1, 10)
    
    print(f"\nput(1,10): {cache}") # Only shows keys in LRU order.
    
    cache.put(2, 20)
    print(f"\nput(2,20): {cache}")

    res = cache.get(1)
    print(f"get(1): {res} (expect 10)")

    cache.put(3, 30)
    print(f"\nput(3,30): {cache}")

    res = cache.get(2)
    print(f"get(2): {res} (expect -1)")

    cache.put(4, 40)
    print(f"\nput(4,40): {cache}")

    res = cache.get(1)
    print(f"get(1): {res} (expect -1)")

    res = cache.get(3)
    print(f"get(3): {res} (expect 30)")

    res = cache.get(4)
    print(f"get(4): {res} (expect 40)")
