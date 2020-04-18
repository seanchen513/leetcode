"""
trie_array.py: this file uses array-based trie nodes with alphabet being
the lowercase English letters.

Keys and prefixes are strings. Keys are words. 
Children/edges are letters (one-char strings).

- Use TrieNode class
- children field is 26-length array/list (not dict).
- sentinel can be a count, a boolean, the key/word itself, or some data
    structure associated with the key/word

search, starts_with, find_node, and delete are 
O(m) time, O(1) space, where m is key length.

insert is O(m) time, O(m) space.

TO DO:
- generalize alphabet?
"""

import collections

class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # aka, edges; or [-1] ?
        
        #self.is_key = False # aka, final, is_key, is_end, is_word
        #self.count = 0
        self.key = ""
    
    # not sure this is useful
    def child(self, ch): # aka, edge()
        return self.children[ord(ch) - 97] # ord('a') is 97

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word: 
            i = ord(ch) - 97 
            if node.children[i] is None:
                node.children[i] = TrieNode()

            node = node.children[i]

        #node.is_key = True
        #node.count += 1
        node.key = word

    def search(self, word: str): # return type can be bool, int, str, ...
        node = self.root

        for ch in word:
            i = ord(ch) - 97 
            if node.children[i] is None:
                #return False # for boolean sentinel
                #return 0 # for int counter sentinel
                return "" # for string sentinel
                #return None # for any sentinel

            node = node.children[i]
 
        #return node.is_key
        #return node.count
        return node.key

    def starts_with(self, prefix: str) -> bool: # search prefix
        node = self.root

        for ch in prefix:
            i = ord(ch) - 97 
            if node.children[i] is None:
                return False
    
            node = node.children[i]
            
        return True

    def find_node(self, word: str) -> TrieNode:
        node = self.root

        for ch in word:
            i = ord(ch) - 97 
            if node.children[i] is None:
                return None

            node = node.children[i]
 
        return node

    """
    What about tracing up the tree and deleting all nodes that don't
    have descendents that are keys?
    """
    def delete(self, word: str): # return type can be bool, int, str, ...
        node = self.root

        for ch in word:
            i = ord(ch) - 97 
            if node.children[i] is None:
                return False # for boolean sentinel
                #return 0 # for int counter sentinel
                #return "" # for string sentinel
                #return None # for any sentinel

            node = node.children[i]
            
        node.is_key = False
        #node.count = 0
        #node.key = ""
