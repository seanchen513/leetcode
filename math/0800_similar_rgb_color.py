"""
800. Similar RGB Color
Easy

In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

Example 1:

Input: color = "#09f166"
Output: "#11ee66"
Explanation:  
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.

Note:

color is a string of length 7.
color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
Any answer which has the same (highest) similarity as the best answer will be accepted.
All inputs and outputs should use lowercase letters, and the output is 7 characters.
"""

###############################################################################
"""
Solution: round each component.

00
11
22
...
99
AA = 10 * 16 + 10 = 10 * 17 = 170
BB = 11 * 17 = 187
CC = 12 * 17 = 204
DD = 13 * 17 = 221
EE = 14 * 17 = 238
FF = 15 * 17 = 255

Runtime: 20 ms, faster than 98.72% of Python3 online submissions
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions
"""
class Solution:
    def similarRGB(self, color: str) -> str:
        x = int(color[1:3], 16)
        y = int(color[3:5], 16)
        z = int(color[5:], 16)

        x = round(x / 17) * 17
        y = round(y / 17) * 17
        z = round(z / 17) * 17
        
        # x1 = round(int(color[1:3], 16) / 17) * 17
        # y1 = round(int(color[3:5], 16) / 17) * 17
        # z1 = round(int(color[5:], 16) / 17) * 17

        return f"#{x:02x}{y:02x}{z:02x}"
        
###############################################################################
"""
Solution 2: brute force, minimizing over all possible values.
"""
class Solution2:
    def similarRGB(self, color: str) -> str:
        x = int(color[1:3], 16)
        y = int(color[3:5], 16)
        z = int(color[5:], 16)
        
        res = float('inf')

        for i in range(0, 256, 17):
            for j in range(0, 256, 17):
                for k in range(0, 256, 17):
                    sim = (x-i)**2 + (y-j)**2 + (z-k)**2
                    if sim < res:
                        res = sim
                        i1 = i
                        j1 = j
                        k1 = k
     
        return f"#{i1:0x}{j1:0x}{k1:0x}"
