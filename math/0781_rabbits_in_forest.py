"""
781. Rabbits in Forest
Medium

In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5

Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0

Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
"""

from typing import List
import collections

###############################################################################
"""
Solution: use dict to count.

O(m) time, where m = len(answers)
O(m) extra space: for dict
1 pass
"""
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = collections.Counter()
        count = 0

        for k in answers:
            if d[k] % (k + 1) == 0: # start a new group of k+1 rabbits
                count += k + 1

            d[k] += 1

        return count

###############################################################################
"""
Solution: use dict to count.

Rabbits can only be same color if they give the same answer.
Converse is not true.
Rabbits can only tell us info about rabbits of the same color.
We can count the number of rabbits of each color (answer) separately.

Greedily group as many rabbits giving same answer together (to be same color) 
as possible. 
For incomplete groups, find how many additional rabbits are needed.

If cnt rabbits answer num_other, then the total number of rabbits answering
num_other must be a multiple of num_other + 1.  We greedily take the smallest
multiple that is >= cnt.

Let size of complete group be n = num_other + 1.
Size of incomplete group = cnt % n
Number to add to get complete group = n - (cnt % n) if cnt % n != 0.
Smallest multiple of n that is >= cnt: cnt + n - (cnt % n) if cnt % n != 0.

To avoid checking if cnt % n != 0, note that:

Number to add to get complete group = -cnt % n
Smallest multiple of n that is >= cnt: (-cnt % n) + cnt

Example:

d[5] = 13
num_other = 5
cnt = 13

6 rabbits can be red
6 rabbits can be blue
Greedily assume these 6+6=12 rabbits are among the 13.
1 leftover rabbit must be another color, say, green.
There must be at least 5 other green rabbits.
There must be a total of 6k rabbits answering 5.
The smallest multiple >= 13 is 18.

###

O(m) time, where m = len(answers)
O(m) extra space

"""
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = collections.Counter(answers)
        
        count = 0

        for num_other, cnt in d.items():
            n = num_other + 1
            count += -cnt % n + cnt
            
        return count

        #return sum(-cnt % (num_other + 1) + cnt for num_other, cnt in d.items())

###############################################################################
"""
Solution: same, but count minimum additional rabbits needed for each color/group.

If cnt rabbits answered num_other, then there must be at least these many
additional rabbits:

additional = (n - (cnt % n)) % n
where n = num_other + 1.

O(m) time, where m = len(answers)
O(m) extra space
"""
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d = collections.Counter(answers)
        
        count = len(answers)

        for num_other, cnt in d.items():
            # if num_other == 0:
            #     continue

            n = num_other + 1
            count += (n - (cnt % n)) % n
            
        return count
            
"""
answer = 5
[1,0,1,0,0]

d[0] = 3
num_other = 0 
cnt = 3
additional = 0

d[1] = 2
num_other = 1
cnt = 2
additional = 0

Max number of 1's with same color is 2.

What if d[1] = 3 ?
Then can group two of them together for one color.
One left, so additional = 1 = 3 % 2.

"""

"""
answer = 5
[2,2,0,0,2]

cnt additional      cnt % 3
1   2 = num_other   1
2   1               2
3   0               0

4   2
5   1
6   0

additional = (n - (cnt % n)) % n

n = num_other + 1

d[0] = cnt
n = 1
additional = (1 - (cnt % 1)) % 1 = 1 % 1 = 0

Note: n % 1 = 0 for all n

"""


"""
answer = 7
[0,2,0,2,1]
 r   g 1 1

d[1] = 1
n = 2
additional = (2 - (1 % 2)) % 2 = 1 % 2 = 1

d[2] = 2
n = 3
additional = (3 - (2 % 3)) % 3 = 1 % 3 = 1

"""

"""
[10, 10, 10]
answer = 11

d[10] = 3: 
additional = 10 - 2 = 8
= num_other - (cnt - 1)

Max number of 10's with same color is 11.

What if d[10] = 12 ?
additional = 1 = 12 % 11.

What if d[10] = 11 + 3 = 14?
Then 11 of them can be same color.
That leaves 3 left over.
additional = 8 as before.

cnt additional
1   10 = num_other
2   9
3   8
4   7
5   6
6   5
7   4
8   3
9   2
10  1
11  0

12  10
13  9
14  8
...
21  1
22  0


"""
