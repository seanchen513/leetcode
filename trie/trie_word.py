"""
trie_word.py: this file uses string sentinels for trie nodes.

Keys and prefixes are strings. Keys are words. 
Children/edges are letters (one-char strings).

- Use TrieNode class
- children field can be {} or defaultdict(TrieNode)
    - ony affects insert()
    - doesn't seem worth it to use defaultdict().
- sentinel can be a count, a boolean, the key/word itself, or some data
    structure associated with the key/word

search, starts_with, find_node, and delete are 
O(m) time, O(1) space, where m is key length.

insert is O(m) time, O(m) space.
"""

import collections

class TrieNode:
    def __init__(self):
        self.children = {}
        #self.children = collections.defaultdict(TrieNode)
        
        #self.is_key = False # aka, final, is_key, is_end, is_word
        #self.count = 0
        self.key = ""
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        # if ch not in node.children, defaultdict will create an entry
        for ch in word: 
            if ch not in node.children: # not needed if using defaultdict()
                node.children[ch] = TrieNode()

            node = node.children[ch]

        #node.is_key = True
        #node.count += 1
        node.key = word

    #def search(self, word: str) -> bool:
    #def search(self, word: str) -> int:
    def search(self, word: str) -> str:
        node = self.root

        for ch in word:
            if ch not in node.children:
                #return False # for boolean sentinel
                #return 0 # for int counter sentinel
                return "" # for string sentinel
                #return None # for any sentinel

            node = node.children[ch]
 
        #return node.is_key
        #return node.count
        return node.key

    def starts_with(self, prefix: str) -> bool: # search prefix
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
    
            node = node.children[ch]
            
        return True

    def find_node(self, word: str) -> TrieNode:
        node = self.root

        for ch in word:
            if ch not in node.children:
                return None

            node = node.children[ch]
 
        return node

    """
    What about tracing up the tree and deleting all nodes that don't
    have descendents that are keys?
    """
    #def delete(self, word: str) -> bool:
    #def delete(self, word: str) -> int:
    def delete(self, word: str) -> str:
        node = self.root

        for ch in word:
            if ch not in node.children:
                #return False # for boolean sentinel
                #return 0 # for int counter sentinel
                return "" # for string sentinel
                #return None # for any sentinel

            node = node.children[ch]
            
        #node.is_key = False
        #node.count = 0
        node.key = ""
