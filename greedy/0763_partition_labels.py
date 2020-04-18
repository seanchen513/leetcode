"""
763. Partition Labels
Medium

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
"""

from typing import List

###############################################################################
"""
Solution: greedily choose smallest partitions. Use "last" dict that maps
each char to the last index that it appears in string. 

Use 3 pointers. 
1st ptr = index of first elt of partition (variable for outer loop)
2nd ptr = index of tentative last elt of partition; initially last[1st ptr].
3rd ptr = checks all the chars in-between, extending the 2nd ptr when
last[3rd ptr] extends beyond the 2nd ptr.

Example:
qiejxqfnqceocmy
qiejxqfnq-ce-oc m y

O(n) time
O(26) extra space: for dict and output
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # dict that maps char to last index that it appears in s
        last = {ch: i for i, ch in enumerate(s)} 
        res = []

        n = len(s)
        i = 0 # index for s

        while i < n:
            # s[i] = first char of partition
            # last[s[i]] = the last index that this char appears
            # end = index for tentative last elt of partition
            end = last[s[i]] 

            # Check all the chars between the first and tentative last index.
            # If any has a "last" char that extends beyond end, then update end.
            j = i + 1
            while j < end:
                if last[s[j]] > end:
                    end = last[s[j]]
                
                j += 1

            res.append(end - i + 1) # size of partition
            i = end + 1

        return res

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")

        res = sol.partitionLabels(s)

        print(f"\nres = {res}\n")


    sol = Solution()

    comment = "LC example; answer = [9,7,8]"
    s = "ababcbacadefegdehijhklij"
    test(s, comment)
    
    comment = "LC TC; answer = [13,1,1]"
    s = "qiejxqfnqceocmy"
    test(s, comment)
