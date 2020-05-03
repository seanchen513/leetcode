"""
1436. Destination City
Easy

You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
 
Constraints:

1 <= paths.length <= 100
paths[i].length == 2
1 <= cityAi.length, cityBi.length <= 10
cityAi != cityBi
All strings consist of lowercase and uppercase English letters and the space character.
"""

from typing import List
import collections

###############################################################################
"""
Solution: use set to hold starting cities. Then check for destination city
that is not in set.

O(n) time
O(n) extra space: for set
"""
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set(src for src, _ in paths)

        for _, dest in paths:
            if dest not in s:
                return dest
"""
Same, but use set to hold destination cities. Then remove all starting cities.
Remaining city in set is answer.
"""
class Solution1b:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set(dest for _, dest in paths)

        # There may be a starting city that is not also a destination city.
        # So it will not be in the set.
        for src, _ in paths:
            s.discard(src) # use discard() instead of remove() to avoid KeyError

        return s.pop()

"""
Same, but use two sets, and set subtraction.
"""
class Solution1c:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dest = map(set, zip(*paths))
        return (dest - src).pop()

###############################################################################
"""
Solution 2: use dict to count.
"""
class Solution2:
    def destCity(self, paths: List[List[str]]) -> str:
        d = collections.Counter()
        
        for x, y in paths:
            d[x] += 1
            d[y] -= 1
            
        for x in d:
            if d[x] == -1:
                return x

"""
Same but also delete dict entries.
"""
class Solution2b:
    def destCity(self, paths: List[List[str]]) -> str:
        d = collections.Counter()
        
        for x, y in paths:
            d[x] += 1
            d[y] -= 1
            if d[x] == 0:
                del d[x]
            if d[y] == 0:
                del d[y]

        # There can be an entry with d[x] == 1.
        for x in d:
            if d[x] == -1:
                return x

###############################################################################

if __name__ == "__main__":
    #def test(arr, comment=None):
    def test(arr, k, comment=None):
        print("="*80)
        if comment:
            print(comment)

        #lst = build_ll(arr)[0]
        #root = array_to_bt_lc(arr)
        #graph = graph_from_adj_list(adj_list, index_base)
        #adj_dict = node_to_adj_dict(graph)

        print()
        print(f"\narr={arr}")
        #print(lst)
        #print_tree(root)


        res = sol.(arr)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC ex1; answer = "
    arr = 
    k = 
    #test(arr, comment)
    test(arr, k, comment)

    comment = "LC ex2; answer = "
    arr = 
    k = 
    #test(arr, comment)
    test(arr, k, comment)

    comment = "LC ex3; answer = "
    arr = 
    k = 
    #test(arr, comment)
    test(arr, k, comment)

    comment = "LC ex4; answer = "
    arr = 
    k = 
    #test(arr, comment)
    test(arr, k, comment)
    
