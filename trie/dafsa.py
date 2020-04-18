"""
dafsa.py: this file uses boolean sentinels for DAFSA nodes.

DAFSA/MAFSA/DAWG

Deterministic
Acyclic
Finite
State
Automaton

aka, DAWG = Directed Acyclic Word Graph
DAWG also refers to related DS that functions as suffix index

http://stevehanov.ca/blog/?id=115
"""

###############################################################################

class DafsaNode:
    next_id = 0

    def __init__(self):
        self.id = DafsaNode.next_id
        DafsaNode.next_id += 1

        self.final = False # aka, final, is_key, is_end, is_word
        #self.key = ""
        
        self.edges = {}

class Dafsa:
    def __init__(self):
        self.prev_word = ""
        self.root = DafsaNode()

        self.unchecked_nodes = [] # not yet checked for duplication
        self.minimized_nodes = {} # unique nodes that have been checked for duplication

    def insert(self, word):
        # if word < self.prev_word:
        #     raise Exception("Error: words must be inserted in lex order.")

        # find common prefix between word and previous word
        common_prefix = 0
        for i in range( min(len(word), len(self.prev_word)) ):
            if word[i] != self.prev_word[i]:
                break

            common_prefix += 1

        # check the unchecked_nodes for redundant nodes, proceeding from
        # last one down to the common prefix size. Then truncate the list
        # at that point.
        self._minimize(common_prefix)

        # add the suffix, starting from the correct node midway through graph
        if len(self.unchecked_nodes) == 0:
            node = self.root
        else:
            node = self.unchecked_nodes[-1][2]

        for ch in word[common_prefix:]:
            next_node = DafsaNode()
            node.edges[ch] = next_node
            self.unchecked_nodes.append((node, ch, next_node))
            node = next_node

        node.final = True
        #node.key = word

        self.prev_word = word

    def finish(self):
        # minimize all unchecked_nodes
        self._minimize(0)

    def _minimize(self, down_to):
        # proceed from leaf up to a certain point
        for i in range(len(self.unchecked_nodes) - 1, down_to - 1, -1):
            parent, letter, child = self.unchecked_nodes[i]

            if child in self.minimized_nodes:
                # replace the child with the previously encountered one
                parent.edges[letter] = self.minimized_nodes[child]
            else:
                # add the state to the minimzed nodes
                self.minimized_nodes[child] = child
            
            self.unchecked_nodes.pop()

    def lookup(self, word): # aka, search()
        node = self.root

        for ch in word:
            if ch not in node.edges:
                return False

            node = node.edges[ch]

        return node.final
        #return node.key

    def find_node(self, word):
        node = self.root

        for ch in word:
            if ch not in node.edges:
                return None

            node = node.edges[ch]

        return node

    def node_count(self):
        return len(self.minimized_nodes)

    def edge_count(self):
        count = 0
        for node in self.minimized_nodes:
            count += len(node.edges)

        return count

###############################################################################
# original

class DafsaNode2:
    next_id = 0

    def __init__(self):
        self.id = DafsaNode.next_id
        DafsaNode.next_id += 1

        self.final = False
        self.edges = {}

class Dafsa2:
    def __init__(self):
        self.prev_word = ""
        self.root = DafsaNode()

        self.unchecked_nodes = [] # not yet checked for duplication
        self.minimized_nodes = {} # unique nodes that have been checked for duplication

    def insert(self, word):
        if word < self.prev_word:
            raise Exception("Error: words must be inserted in lex order.")

        # find common prefix between word and previous word
        common_prefix = 0
        for i in range( min(len(word), len(self.prev_word)) ):
            if word[i] != self.prev_word[i]:
                break

            common_prefix += 1

        # check the unchecked_nodes for redundant nodes, proceeding from
        # last one down to the common prefix size. Then truncate the list
        # at that point.
        self._minimize(common_prefix)

        # add the suffix, starting from the correct node midway through graph
        if len(self.unchecked_nodes) == 0:
            node = self.root
        else:
            node = self.unchecked_nodes[-1][2]

        for ch in word[common_prefix:]:
            next_node = DafsaNode()
            node.edges[ch] = next_node
            self.unchecked_nodes.append((node, ch, next_node))
            node = next_node

        node.final = True
        self.prev_word = word

    def finish(self):
        # minimize all unchecked_nodes
        self._minimize(0)

    def _minimize(self, down_to):
        # proceed from leaf up to a certain point
        for i in range(len(self.unchecked_nodes) - 1, down_to - 1, -1):
            parent, letter, child = self.unchecked_nodes[i]

            if child in self.minimized_nodes:
                # replace the child with the previously encountered one
                parent.edges[letter] = self.minimized_nodes[child]
            else:
                # add the state to the minimzed nodes
                self.minimized_nodes[child] = child
            
            self.unchecked_nodes.pop()

    def lookup(self, word):
        node = self.root

        for ch in word:
            if ch not in node.edges:
                return False

            node = node.edges[ch]

        return node.final

    def find_node(self, word):
        node = self.root

        for ch in word:
            if ch not in node.edges:
                return None

            node = node.edges[ch]

        return node

    def node_count(self):
        return len(self.minimized_nodes)

    def edge_count(self):
        count = 0
        for node in self.minimized_nodes:
            count += len(node.edges)

        return count
