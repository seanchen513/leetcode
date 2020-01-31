"""
437. Path Sum III
Easy

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
"""

import sys
sys.path.insert(1, '../tree/')

from binary_tree import print_tree, array_to_bt

###############################################################################
"""
Solution #1: use double recursion.

O(n) time for outer recursion
O(k) (linear tree) for inner recursion (O(log k) if balanced tree)
where k is number of nodes in subtree at which inner recursion si called.
O(n^2) time overall. (O(n log n) if balanced tree)

O(n) extra space for recursion stack.  O(log n) (balanced tree).
"""
def num_path_sum(root, target_sum):
    # Look at sums starting at given node.
    def num_path_sum_rooted(node, target_sum, count=0):
        if not node:
            return 0

        count += (target_sum == node.val) \
            + num_path_sum_rooted(node.left, target_sum - node.val, count) \
            + num_path_sum_rooted(node.right, target_sum - node.val, count)

        return count

    def dfs(node, target_sum, total_count=0):
        if not node:
            return total_count

        total_count += num_path_sum_rooted(node, target_sum)
        
        total_count = dfs(node.left, target_sum, total_count)
        total_count = dfs(node.right, target_sum, total_count)
        
        #dfs(node.left, target_sum)
        #dfs(node.right, target_sum)

        return total_count

    return dfs(root, target_sum)
    
###############################################################################
"""
Solution #2: use double BFS using lists.
"""
def num_path_sum2(root, target_sum):
    # Look at sums starting at given node.
    def num_path_sum_rooted(node, target_sum, count=0):
        if not node:
            return 0
        
        count = 0
        level = [(node, 0)]
        
        while level:
            next_level= []

            for curr, sum_so_far in level:
                if curr:
                    sum_so_far += curr.val

                    if sum_so_far == target_sum:
                        count += 1

                    next_level.extend([
                        (curr.left, sum_so_far), 
                        (curr.right, sum_so_far) ])
            
            level = next_level

        return count

    total_count = 0
    level = [root]

    while level:
        next_level = []

        for node in level:
            if node:
                total_count += num_path_sum_rooted(node, target_sum)
                next_level.extend([node.left, node.right])

        level = next_level

    return total_count
    
###############################################################################
"""
Solution #3: Single BFS using lists, and use dict to track path sums.

Keep dicts that map starting node -> path sum starting from that node
to the current node.  These dict values are updated as the paths expand.
If a node branches to both the left and right, the node's dict is
passed to one side, and a copy is passed to the other side.
"""
def num_path_sum3(root, target_sum):
    if not root:
        return 0

    count = 0
    level = [(root, {})] # 2nd elt is dictionary of node -> sum

    while level:
        next_level = []

        for node, dic in level:
            # add new sum starting from current node to dict
            dic[node] = 0 

            val = node.val

            for k, v in dic.items():
                v += val
                if v == target_sum:
                    count += 1

                # update sum starting from node k to new value v
                dic[k] = v 

            # Do these checks to avoid costly dict copying
            if node.left:
                if node.right:
                    next_level.extend([
                        (node.left, dic),
                        (node.right, dic.copy())])
                else:
                    next_level.append((node.left, dic))
            elif node.right:
                next_level.append((node.right, dic))

        level = next_level

    return count

###############################################################################
"""
Solution #3b: same as sol #3 but using a list of sums instead of dict
"""
def num_path_sum3b(root, target_sum):
    if not root:
        return 0

    count = 0
    level = [(root, [])] # 2nd elt is list of sums

    while level:
        next_level = []

        for node, sums in level:
            sums.append(0) # add new sum starting at current node
            val = node.val
            n = len(sums)

            for i in range(n):
                sums[i] += val
                if sums[i] == target_sum:
                    count += 1

            # Do these checks to avoid costly copying
            if node.left:
                if node.right:
                    next_level.extend([
                        (node.left, sums[:]),
                        (node.right, sums) ])
                else:
                    next_level.append((node.left, sums))
            elif node.right:
                next_level.append((node.right, sums))

        level = next_level

    return count

###############################################################################
"""
Solution #3c: same as sol #3 but using a single master dict

Uses a lot of memory.
"""
import collections

def num_path_sum3c(root, target_sum):
    if not root:
        return 0

    count = 0
    dic = {}
    #dic = collections.defaultdict(dict)
    level = [(root, None)]

    while level:
        next_level = []

        for node, parent in level:
            if node:
                # make copy...
                if parent: 
                    dic[node] = dic[parent].copy()
                else: 
                    dic[node] = {}
                
                dic[node][node] = 0

                val = node.val

                for start, v in dic[node].items():
                    v += val
                    if v == target_sum:
                        count += 1

                    dic[node][start] = v

                next_level.extend([
                    (node.left, node),
                    (node.right, node)
                ])

        level = next_level

    return count

###############################################################################
"""
Solution #4: use memoization.

Use dict to map rooted path sums -> number of times that sum has happened
up to the current node.

Check non-rooted path sums by checking differences of current path sum 
vs old path sums (ie, path sums already in dict).  

Do this indirectly by calculating what an old_path_sum should be for there 
to be a non-rooted path with the target sum: curr_path_sum - target_sum.
This makes it easy to check in the dict.

VERY FAST.

https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)
"""
def num_path_sum4(root, target_sum):
    if not root:
        return 0
    
    def dfs(node, target_sum, cache={0: 1}, curr_path_sum=0, count=0):
        if not node:
            return count

        curr_path_sum += node.val
        old_path_sum = curr_path_sum - target_sum

        # update count and cache
        count += cache.get(old_path_sum, 0)
        cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1

        # recurse
        count = dfs(node.left, target_sum, cache, curr_path_sum, count)
        count = dfs(node.right, target_sum, cache, curr_path_sum, count)
        
        # when move to a different branch, the curr_path_sum is no
        # longer available, so remove one.
        cache[curr_path_sum] -= 1
        
        return count
    
    return dfs(root, target_sum)

"""
Solution #4b: Just like sol #4, but don't use inner function.

This seems to work fine on repeated calls.  So do we really need to make
it an inner function?  Seems to be ok here because only mutable default
arg is cache, and all its values are 0 when the final return is made.

On LeetCode, an inner function is used because LC gives a predefined
function signature:

def pathSum(self, root: TreeNode, target_sum: int) -> int:    

"""
def num_path_sum5(node, target_sum, cache={0: 1}, curr_path_sum=0, count=0):
    if not node:
        return count, cache

    curr_path_sum += node.val
    old_path_sum = curr_path_sum - target_sum

    # update count and cache
    count += cache.get(old_path_sum, 0)
    cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1

    # recurse
    count, cache = num_path_sum5(node.left, target_sum, cache, curr_path_sum, count)
    count, cache = num_path_sum5(node.right, target_sum, cache, curr_path_sum, count)
    
    # when move to a different branch, the curr_path_sum is no
    # longer available, so remove one.
    cache[curr_path_sum] -= 1
    
    return count, cache

###############################################################################

if __name__ == "__main__":
    def test(root, target_sum):
        print("\n" + "#"*80)
        print_tree(root)

        print(f"\ntarget sum = {target_sum}")

        n = num_path_sum(root, target_sum)
        n2 = num_path_sum2(root, target_sum)  
        n3 = num_path_sum3(root, target_sum)  
        n3b = num_path_sum3b(root, target_sum)  
        n3c = num_path_sum3c(root, target_sum) 
        n4 = num_path_sum4(root, target_sum)  
        n5, cache = num_path_sum5(root, target_sum)  

        print(f"\nnumber of paths with sum {target_sum} (sol #1) is {n}")
        print(f"number of paths with sum {target_sum} (sol #2) is {n2}")
        print(f"number of paths with sum {target_sum} (sol #3) is {n3}")
        print(f"number of paths with sum {target_sum} (sol #3b) is {n3b}")
        print(f"number of paths with sum {target_sum} (sol #3c) is {n3c}")
        print(f"number of paths with sum {target_sum} (sol #4) is {n4}")
        print(f"number of paths with sum {target_sum} (sol #5) is {n5}")


    # LC example
    arr = [10, 5,-3, 3,2,None,11, 3,-2,None,1]
    root = array_to_bt(arr)[0]
    target_sum = 8
    test(root, target_sum)

    # LC test; answer = 1
    arr = [1, 2,None]
    root = array_to_bt(arr)[0]
    target_sum = 2
    test(root, target_sum)

    ### LC test; answer = 3
    arr = [5, 4,8, 11,None,13,4, 7,2,None,None,5,1]
    root = array_to_bt(arr)[0]
    target_sum = 22
    test(root, target_sum)

    #
    arr = [1, 1,1, 1,1,1,1, 1,1,1,1,1,1,1,1]
    root = array_to_bt(arr)[0]
    target_sum = 4
    test(root, target_sum)

    # perfect tree with 7 elements, 4 full paths, 6 paths of length 1.
    # total 7+4+6 = 17 paths
    arr = [0, 0,0, 0,0,0,0]
    root = array_to_bt(arr)[0]
    target_sum = 0
    test(root, target_sum)
