"""
212. Word Search II
Hard

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 
Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""

import sys
sys.path.insert(1, '../../leetcode/trie')
sys.path.insert(1, '../../') # for DAFSA files

from typing import List

from trie import TrieNode, Trie # sol 1, 1b
#from trie_word import TrieNode, Trie # sol 1c
#from trie_array import TrieNode, Trie # sol 1d

from dafsa import DafsaNode, Dafsa # sol 2
#from dafsa_word import DafsaNode, Dafsa # sol 2b

"""
Notes:

1. Sol 1c using trie_word.py is best. Trie works better than DAFSA for
dictionary of this small size.

2. It's faster to check bounds and board sentinel right before calling the 
backtrack fn recursively rather than checking at the start of the fn.

3. It's much faster to backtrack by passing trie nodes rather than strings
(the words being built up from the board). This avoids having to 
constantly concatenate strings. This also allows us to deal with duplicate
strings found on the board without having to use a set (see #5).

4. More efficient to call a trie method that returns the node. That way,
we can check if a key/word has been found, and what it is. This also allows
us to pass a trie node to the backtrack fn rather than a string.

Alternative to calling 2 methods (but doesn't help the other issue) is
to call a method to check if the prefix exists, and another method to check
if the word exists. (This problem can be eliminated if we change 
starts_with() to return None, False, or True.)

5. Duplicate words can be found on the board. One way to deal with this is
to use a set for results, and convert it to a list when returning.
We can avoid using a set. When a word is found in the trie, we can reset
the trie node sentinel to indicate that a word is no longer there.

###

???
Using backtracking for each word would result in overall O(w * mn * 4^w) time.

"""

###############################################################################
"""
Solution: build trie from words, then search board for words.
Do this by forming words from board using backtracking, and checking if
the formed words are in the trie.

The current branch of backtracking is stopped if the word formed so far 
cannot be found as a prefix in the trie.

O(n*s) time to build trie, where there are n words, and s is the max word size.
    - Inserting a word is O(m) time, where m is length of word.

O() time for backtracking

Runtime: 868 ms, faster than 8.87% of Python3 online submissions
Memory Usage: 37.1 MB, less than 41.67% of Python3 online submissions
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def rec(r, c, word=""):
            if not (0 <= r < m and 0 <= c < n):
                return False

            if board[r][c] == '#':
                return

            word += board[r][c]

            if not trie.starts_with(word):
                return

            if trie.search(word):
                res.add(word)
                # need to continue searching

            board[r][c] = '#'

            rec(r-1, c, word)
            rec(r+1, c, word)
            rec(r, c-1, word)
            rec(r, c+1, word)

            board[r][c] = word[-1]
            
        trie = Trie()

        for w in words:
            trie.insert(w)

        m = len(board)
        n = len(board[0])
        res = set()

        for i in range(m):
            for j in range(n):
                rec(i, j)

        return list(res)

"""
Solution 1b: same as sol 1, but optimized.

Note: we can avoid adding duplicate words found on the board to the output
list by first outputing to a set, and then converting that set to a list at
the very end. Alternatively, we can avoid using a set by setting the end of
word sentinel indicator in the trie node to False after adding a word to the
output list.

Moved checks for bounds and board sentinel:
Runtime: 816 ms, faster than 9.45% of Python3 online submissions
Memory Usage: 37.1 MB, less than 41.67% of Python3 online submissions

Above, and using different trie class where search() returns node, and trie
uses boolean marker rather than counter:
Runtime: 632 ms, faster than 14.02% of Python3 online submissions
Memory Usage: 36.8 MB, less than 41.67% of Python3 online submissions

This improves slightly if use regular dict instead of defaultdict in TrieNode class:
Runtime: 604 ms, faster than 15.05% of Python3 online submissions
Memory Usage: 32 MB, less than 91.67% of Python3 online submissions
"""
class Solution1b:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def rec(r, c, word=""):
            word += board[r][c]

            node = trie.find_node(word)
            if not node:
                return
            if node.is_key:
                #res.add(word) # if using set() for output
                res.append(word)
                node.is_key = False # alternative to using set() for 

            board[r][c] = '#'

            if r >= 1 and board[r-1][c] != '#':
                rec(r-1, c, word)
            if r+1 < m and board[r+1][c] != '#':
                rec(r+1, c, word)
            if c >= 1 and board[r][c-1] != '#':
                rec(r, c-1, word)
            if c+1 < n and board[r][c+1] != '#':
                rec(r, c+1, word)

            board[r][c] = word[-1]
            
        trie = Trie()

        for w in words:
            trie.insert(w)

        m = len(board)
        n = len(board[0])
        #res = set()
        res = []

        for i in range(m):
            for j in range(n):
                rec(i, j)

        #return list(res)
        return res

"""
Solution 1c: Pass the trie node instead of the board word to the backtrack function.
The trie sentinel is the word itself.

Runtime: 260 ms, faster than 88.14% of Python3 online submissions
Memory Usage: 36.9 MB, less than 41.67% of Python3 onine submissions
"""
class Solution1c:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def rec(r, c, node):
            ch = board[r][c]
            if ch not in node.children:
                return
            node = node.children[ch]

            if node.key:
                #res.add(word) # if using set() for output
                res.append(node.key)
                node.key = "" # alternative to using set() for 

            board[r][c] = '#'

            if r >= 1 and board[r-1][c] != '#':
                rec(r-1, c, node)
            if r+1 < m and board[r+1][c] != '#':
                rec(r+1, c, node)
            if c >= 1 and board[r][c-1] != '#':
                rec(r, c-1, node)
            if c+1 < n and board[r][c+1] != '#':
                rec(r, c+1, node)

            board[r][c] = ch
            
        trie = Trie()

        for w in words:
            trie.insert(w)

        m = len(board)
        n = len(board[0])
        #res = set()
        res = []

        for i in range(m):
            for j in range(n):
                rec(i, j, trie.root)

        #return list(res)
        return res

"""
Solution 1d: same as sol 1c, but use trie w/ array-based nodes

SLOWER than dict-based nodes.

Runtime: 296 ms, faster than 82.19% of Python3 online submissions
Memory Usage: 37.9 MB, less than 41.67% of Python3 online submissions
"""
class Solution1d:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def rec(r, c, node):
            ch = board[r][c]
            i = ord(ch) - 97
            if node.children[i] is None:
                return
            node = node.children[i]

            if node.key:
                #res.add(word) # if using set() for output
                res.append(node.key)
                node.key = "" # alternative to using set() for 

            board[r][c] = '#'

            if r >= 1 and board[r-1][c] != '#':
                rec(r-1, c, node)
            if r+1 < m and board[r+1][c] != '#':
                rec(r+1, c, node)
            if c >= 1 and board[r][c-1] != '#':
                rec(r, c-1, node)
            if c+1 < n and board[r][c+1] != '#':
                rec(r, c+1, node)

            board[r][c] = ch
            
        trie = Trie()

        for w in words:
            trie.insert(w)

        m = len(board)
        n = len(board[0])
        #res = set()
        res = []

        for i in range(m):
            for j in range(n):
                rec(i, j, trie.root)

        #return list(res)
        return res

###############################################################################
"""
Solution: use DAFSA/MAFSA/DAWG.

Runtime: 652 ms, faster than 14.10% of Python3 online submissions
Memory Usage: 37.3 MB, less than 41.67% of Python3 online submissions
"""
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def rec(r, c, word=""):
            word += board[r][c]

            node = dafsa.find_node(word)
            if not node:
                return
            
            if node.final:
                #res.add(word) # if using set() for output
                res.append(word)
                node.final = False # alternative to using set() for output

            board[r][c] = '#'

            if r >= 1 and board[r-1][c] != '#':
                rec(r-1, c, word)
            if r+1 < m and board[r+1][c] != '#':
                rec(r+1, c, word)
            if c >= 1 and board[r][c-1] != '#':
                rec(r, c-1, word)
            if c+1 < n and board[r][c+1] != '#':
                rec(r, c+1, word)

            board[r][c] = word[-1]
            
        dafsa = Dafsa()
        words.sort()

        for w in words:
            dafsa.insert(w)

        #dafsa.finish()

        m = len(board)
        n = len(board[0])
        #res = set()
        res = []

        for i in range(m):
            for j in range(n):
                rec(i, j)

        #return list(res)
        return res

"""
Solution 2b: same, but pass the trie node instead of the board word to the
backtrack function. The trie sentinel is the word itself.

O() time overall...
O(n log n) time for sorting

O() extra space: for DAFSA

Runtime: 316 ms, faster than 75.45% of Python3 online submissions
Memory Usage: 37.2 MB, less than 41.67% of Python3 online submissions
"""
class Solution2b:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def rec(r, c, node):
            ch = board[r][c]

            if ch not in node.edges:
                return
            
            node = node.edges[ch]

            if node.key:
                #res.add(node.key) # if using set() for output
                res.append(node.key)
                node.key = "" # alternative to using set() for output

            board[r][c] = '#'

            if r >= 1 and board[r-1][c] != '#':
                rec(r-1, c, node)
            if r+1 < m and board[r+1][c] != '#':
                rec(r+1, c, node)
            if c >= 1 and board[r][c-1] != '#':
                rec(r, c-1, node)
            if c+1 < n and board[r][c+1] != '#':
                rec(r, c+1, node)

            board[r][c] = ch
            
        dafsa = Dafsa()
        words.sort()

        for w in words:
            dafsa.insert(w)

        #dafsa.finish()

        m = len(board)
        n = len(board[0])
        #res = set()
        res = []

        for i in range(m):
            for j in range(n):
                rec(i, j, dafsa.root)

        #return list(res)
        return res

###############################################################################
"""
Solution: build trie from board...

TLE
"""
class Solution3:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def rec(r, c, word=""):
            if not (0 <= r < m and 0 <= c < n):
                return False

            if board[r][c] == '#':
                return False

            word += board[r][c]
            
            if len(word) == max_len:
                add(word)

            board[r][c] = '#'

            res = not (rec(r-1, c, word) or
                rec(r+1, c, word) or
                rec(r, c-1, word) or
                rec(r, c+1, word)
                )
            if res and (min_len <= len(word) <= max_len):
                add(word)


            board[r][c] = word[-1]

            return not res

        def add(word):
            end = min(len(word), max_len)
            node = trie

            for i in range(end):
                c = word[i]
                if c not in node:
                    node[c] = {}

                node = node[c]

        def search(word):
            node = trie

            for c in word:
                if c not in node:
                    return False
                
                node = node[c]

            return True

        m = len(board)
        n = len(board[0])
        #max_len = len(max(words, key=len))
        max_len = max([len(w) for w in words] + [0])
        min_len = min([len(w) for w in words] + [0])
        #print(f"\nmax_len = {max_len}")

        trie = {}
        for i in range(m):
            for j in range(n):
                    rec(i, j)

        res = []

        for w in words:
            if search(w):
                res.append(w)

        return res

###############################################################################

if __name__ == "__main__":
    def test(board, words, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print()
        for row in board:
            for ch in row:
                print(f"{ch}", end=" ")
            print()

        print(f"\nwords = {words}")

        res = sol.findWords(board, words)

        print(f"\nres = {res}\n")


    sol = Solution() # build trie from words
    #sol = Solution1b() # optimized
    #sol = Solution1c() # backtrack w/ trie node instead of board word
    #sol = Solution1d() # trie w/ array-based nodes
    
    #sol = Solution2() # DAFSA
    #sol = Solution2b() # DAFSA< backtrack with trie node instead of board word

    #sol = Solution3() # build trie from board... TLE

    comment = 'LC example; answer = ["eat","oath"]'
    board = [
        ['o','a','a','n'],
        ['e','t','a','e'],
        ['i','h','k','r'],
        ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    test(board, words, comment)

    comment = 'LC TC; answer = []'
    board = [
        ['a']
    ]
    words = []
    test(board, words, comment)

    comment = 'LC TC; answer = ["abcdefg","befa","eaabcdgfa","gfedcbaaa"]'
    board = [["a","b","c"],["a","e","d"],["a","f","g"]]
    words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]
    test(board, words, comment)

    comment = 'LC TC; answer = ["abbbababaa"]'
    board = [
        ["b","b","a","a","b","a"],
        ["b","b","a","b","a","a"],
        ["b","b","b","b","b","b"],
        ["a","a","a","b","a","a"],
        ["a","b","a","a","b","b"]]
    words = ["abbbababaa"]
    test(board, words, comment)

    # Good test case for making sure we don't end backtracking early
    # If "aaa" is already found, we can't stop since we still need to look
    # for "aaab" and "aaaa".
    comment = 'LC TC; answer = ["aaa","aaab","aaba","aba","baa"]'
    board = [["a","b"],["a","a"]]
    words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
    test(board, words, comment)
