"""
208. Implement Trie (Prefix Tree)
Medium

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

import collections

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

###############################################################################
"""
Solution: use array for children.

Runtime: 224 ms, faster than 30.97% of Python3 online submissions
Memory Usage: 33 MB, less than 7.41% of Python3 online submissions
"""
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie

        for ch in word:
            child = node.children[ord(ch) - ord('a')]
            if not child:
                child = node.children[ord(ch) - ord('a')] = TrieNode()

            node = child

        node.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie

        for ch in word:
            child = node.children[ord(ch) - ord('a')]
            if not child:
                return False

            node = child

        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie

        for ch in prefix:
            child = node.children[ord(ch) - ord('a')]
            if not child:
                return False

            node = child

        return True

###############################################################################
"""
Solution:

Nodes are [{}, False], where:
1st component is a dict that maps characters to nodes, and
2nd component is a boolean indicating whether the current key (root to current
node) is a trie key (word).

Runtime: 164 ms, faster than 76.12% of Python3 online submissions
Memory Usage: 28.6 MB, less than 62.96% of Python3 online submissions
"""
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = [{}, False] # children = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie

        for ch in word:
            if ch not in node[0]:
                node[0][ch] = [{}, False]

            node = node[0][ch]

        node[1] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie

        for ch in word:
            if ch not in node[0]:
                return False

            node = node[0][ch]
 
        return node[1]

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie

        for ch in prefix:
            if ch not in node[0]:
                return False
    
            node = node[0][ch]
            
        return True


###############################################################################
"""
Solution: same, but use TrieNode class.

Runtime: 176 ms, faster than 70.95% of Python3 online submissions
Memory Usage: 31.1 MB, less than 11.11% of Python3 online submissions
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.trie

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.trie

        for ch in word:
            if ch not in node.children:
                return False # or return None

            node = node.children[ch]
 
        return node.is_end # or return node or node info if this sentinel is True

    def startsWith(self, prefix: str) -> bool:
        node = self.trie

        for ch in prefix:
            if ch not in node.children:
                return False
    
            node = node.children[ch]
            
        return True

###############################################################################
"""
Solution: same, but use defaultdict for children field in TrieNode class.

Simplifies insert().

Runtime: 188 ms, faster than 57.14% of Python3 online submissions
Memory Usage: 32.6 MB, less than 7.41% of Python3 online submissions
"""
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_end = False

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.trie

        # if ch not in node.children, defaultdict will create an entry
        for ch in word: 
            node = node.children[ch]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.trie

        for ch in word:
            if ch not in node.children:
                return False # or return None

            node = node.children[ch]
 
        return node.is_end # or return node or node info if this sentinel is True

    def startsWith(self, prefix: str) -> bool:
        node = self.trie

        for ch in prefix:
            if ch not in node.children:
                return False
    
            node = node.children[ch]
            
        return True

###############################################################################
"""
Solution: same, but instead of is_end boolean, use key/word counter.

Runtime: 180 ms, faster than 67.65% of Python3 online submissions
Memory Usage: 32.4 MB, less than 7.41% of Python3 online submissions
"""
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.count = 0

class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        node = self.trie

        # if ch not in node.children, defaultdict will create an entry
        for ch in word: 
            node = node.children[ch]

        node.count += 1

    def search(self, word: str) -> bool:
        node = self.trie

        for ch in word:
            if ch not in node.children:
                return 0

            node = node.children[ch]
 
        return node.count # or return node or node info if this sentinel is True

    def startsWith(self, prefix: str) -> bool:
        node = self.trie

        for ch in prefix:
            if ch not in node.children:
                return False
    
            node = node.children[ch]
            
        return True
