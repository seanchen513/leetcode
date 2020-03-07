"""
Graph.

Related:
LC133 Clone Graph
"""

###############################################################################
"""
"""
#class GraphNode:
class Node:
    # dangerous to use default [] for neighbors
    def __init__(self, val=0, neighbors=None): 
        self.val = val
        if not neighbors:
            neighbors = []
        self.neighbors = neighbors


"""
Assume nodes are labeled by integer indices, starting with index_base.
Returns node indexed by index_base.

LC133 uses this format with index_base = 1.
"""
def graph_from_adj_list(adj_list, index_base=0):
    if not adj_list:
        return None # or empty dict?

    visited = {}

    for i, nbrs in enumerate(adj_list):
        if i + index_base in visited:
            curr = visited[i + index_base]
        else:
            #curr = GraphNode(i + index_base)
            curr = Node(i + index_base)
            visited[i + index_base] = curr
        
        for nbr in nbrs:
            if nbr not in visited:
                #visited[nbr] = GraphNode(nbr)
                visited[nbr] = Node(nbr)
            curr.neighbors.append(visited[nbr])

    return visited[index_base]

"""
Returns dict mapping node labels to corresponding graph nodes.
"""
def graph_from_adj_dict(adj_dict):
    if not adj_dict:
        return None # or empty dict?

    visited = {}

    for i, nbrs in adj_dict.items():
        if i in visited:
            curr = visited[i]
        else:
            #curr = GraphNode(i)
            curr = Node(i)
            visited[i] = curr

        for nbr in nbrs:
            if nbr not in visited:
                #visited[nbr] = GraphNode(nbr)
                visited[nbr] = Node(nbr)
            curr.neighbors.append(visited[nbr])

    return visited

"""
Given node in graph, returns adjacency dict for nodes reachable from
given node.  The adjacency dict maps each node label to a list of incident
node labels.  
"""
def node_to_adj_dict(node):
    def visit(node):
        if node.val not in visited:
            visited[node.val] = []

            for nbr in node.neighbors:
                visited[node.val].append(nbr.val)
                visit(nbr)

    if not node:
        return None # or empty dict?

    visited = {}
    visit(node)

    return visited

"""
Given node in graph, returns adjacency list for nodes reachable from
given node.  The indices of the adjacency list and the node labels are
offset by index_base.
"""
def node_to_adj_list(node, index_base=0):
    visited = node_to_adj_dict(node)
    n = len(visited)
    lst = [[] for _ in range(n)]

    for i in range(n):
        lst[i] = visited[i + index_base]

    return lst
    
###############################################################################

if __name__ == "__main__":
    def print_adj_list(adj_list, index_base=0):
        for i, row in enumerate(adj_list):
            #print(f'{i + index_base}: ' + ' '.join(map(str, row)))
            print(f'{i + index_base}: ', end='')
            print(row)
        print()

    def print_adj_dict(adj_dict):
        if not adj_dict:
            print("empty (None)")
            return

        for node, nbrs in adj_dict.items():
            print(f"{node}: {nbrs}")

    def test(adj_list, index_base=0, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print("\nAdjacency list (given):")
        print_adj_list(adj_list, index_base)

        graph = graph_from_adj_list(adj_list, index_base)

        #print_graph(graph)

        adj_dict = node_to_adj_dict(graph)
        print("Adjacency dict from graph:")
        print_adj_dict(adj_dict)

        graph2 = graph_from_adj_dict(adj_dict)

        if graph2:
            adj_dict = node_to_adj_dict(graph2[index_base])
            print("\nAdjacency dict from graph2:")
            print_adj_dict(adj_dict)

            adj_list2 = node_to_adj_list(graph2[index_base], index_base)
            print("\nAdjacency list from graph2:")
            print_adj_list(adj_list2, index_base)


    comment = "LC133 example"
    adj_list = [[2,4],[1,3],[2,4],[1,3]]
    index_base = 1
    test(adj_list, index_base, comment)

    comment = "No nodes, no edges"
    adj_list = []
    index_base = 1
    test(adj_list, index_base, comment)

    comment = "Single node with no edges"
    adj_list = [[]]
    index_base = 1
    test(adj_list, index_base, comment)

    comment = "Single node with one self-cycle"
    adj_list = [[1]]
    index_base = 1
    test(adj_list, index_base, comment)

    comment = "Node 1 with no outgoing edges: adjacency list for it omitted"
    adj_list = [[1]]
    index_base = 0
    test(adj_list, index_base, comment)

    comment = "Node 1 with no outgoing edges: adjacency list for it is empty list"
    adj_list = [[1], []]
    index_base = 0
    test(adj_list, index_base, comment)

    # comment = ""
    # adj_list = [[2,4,5],[1,3],[2,4],[1,3,5],[1,4]]
    # index_base = 1
    # test(adj_list, index_base, comment)
