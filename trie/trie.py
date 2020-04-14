"""
Trie

- Use TrieNode class.
- children field is defaultdict(TrieNode)

search, starts_with, and delete are O(m) time, O(1) space, where m is key length.
insert is O(m) time, O(m) space.
"""

import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0
        #self.is_key = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.trie

        # if ch not in node.children, defaultdict will create an entry
        for ch in word: 
            node = node.children[ch]

        node.count += 1
        #node.is_key = True

    def search(self, word: str) -> bool:
        node = self.trie

        for ch in word:
            if ch not in node.children:
                return 0

            node = node.children[ch]
 
        return node.count # or return node or node info if this sentinel is True
        #return node.is_key

    def starts_with(self, prefix: str) -> bool: # search prefix
        node = self.trie

        for ch in prefix:
            if ch not in node.children:
                return False
    
            node = node.children[ch]
            
        return True

    def delete(self, word: str) -> bool:
        node = self.trie

        for ch in word:
            if ch not in node.children:
                return False # no such word
    
            node = node.children[ch]
            
        node.count = 0
        #node.is_end = False
