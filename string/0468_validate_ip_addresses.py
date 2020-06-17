"""
468. Validate IP Address
Medium

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
"""

###############################################################################
"""
Solution:

IPv4:
- there must be exactly 4 parts (separated by ".")
- each part can only have decimal digits
- "0" cannot be a leading digit unless it is the entire part
- the integer value of the part must be from 0 to 255, inclusive

IPv6:
- there must be exactly 8 parts (separated by ":")
- each part can only have hex chars (lowercase or uppercase ok, and can be mixed)
- cannot have length 0 or length > 4
- ok to have part "0" or leading zeros
- ok to have parts with length 1, 2, 3, or 4
"""
class Solution:
    #def validIPAddress(self, IP: str) -> str:
    def validIPAddress(self, s: str) -> str:
        if len(s) > 39: # optional; to avoid checking extremely long inputs
            return "Neither"

        parts = s.split('.')

        if len(parts) == 4: # check if IPv4
            for p in parts:
                if len(p) == 0 or (p[0] == '0' and len(p) > 1):
                    return "Neither"
                
                # check if all digits
                if not all(ch.isdigit() for ch in p):
                    return "Neither"
                
                if int(p) < 0 or int(p) > 255:
                    return "Neither"
                
            return "IPv4"

        parts = s.split(':')

        if len(parts) == 8: # check if IPv6
            for p in parts:
                if len(p) == 0 or len(p) > 4:
                    return "Neither"
                
                # check if valid hex chars
                for ch in p:
                    if ch not in '0123456789abcdefABCDEF':
                        return "Neither"
                    
            return "IPv6"
            
        return "Neither"

###############################################################################
"""
Solution 2: basically the same, but uses string.find().
"""
class Solution2:
    #def validIPAddress(self, IP: str) -> str:
    def validIPAddress(self, s: str) -> str:
        if len(s) > 39: # optional; to avoid checking extremely long inputs
            return "Neither"

        if s.find('.') >= 0: # check if IPv4
            parts = s.split('.')
            if len(parts) != 4:
                return "Neither"
            
            for p in parts:
                if len(p) == 0 or (p[0] == '0' and len(p) > 1):
                    return "Neither"
                
                # check if all digits
                if not all(ch.isdigit() for ch in p):
                    return "Neither"
                
                if int(p) < 0 or int(p) > 255:
                    return "Neither"
                
            return "IPv4"

        elif s.find(':') >= 0: # check if IPv6
            parts = s.split(':')
            if len(parts) != 8:
                return "Neither"
            
            for p in parts:
                if len(p) == 0 or len(p) > 4:
                    return "Neither"
                
                # check if valid hex chars
                for ch in p:
                    if ch not in '0123456789abcdefABCDEF':
                        return "Neither"
                    
            return "IPv6"
            
        else:
            return "Neither"

###############################################################################

if __name__ == "__main__":
    def test(s, comment=None):
        print("="*80)
        if comment:
            print(comment)

        print(f"\ns = {s}")

        res = sol.validIPAddress(s)

        print(f"\nres = {res}\n")


    sol = Solution()
    #sol = Solution2()

    comment = "LC ex1; answer = IPv4"
    s = "172.16.254.1"
    test(s, comment)

    comment = "LC ex2; answer = IPv6"
    s = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    test(s, comment)
        
    comment = "LC ex3; answer = Neither"
    s = "256.256.256.256"
    test(s, comment)
        
    comment = "LC TC; answer = Neither"
    s = "1e1.4.5.6"
    test(s, comment)
        
    comment = "LC TC; answer = Neither"
    s = "2001:0db8:85a3:00000:0:8A2E:0370:7334" # neither because of 5 0's
    test(s, comment)

    comment = "LC TC; answer = Neither"
    s = "20EE:Fb8:85a3:0:0:8A2E:0370:7334:12" # neither because 9 parts
    test(s, comment)

    comment = "LC TC; answer = IPv6"
    s = "20EE:Fb8:85a3:0:0:8A2E:0370:7334" # note "Fb8" has length 3
    test(s, comment)
