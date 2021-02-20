class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s;
        else:
            p1 = 0
            p2 = len(s) - 1
            if s[p1] == s[p2]:
                i1 = p1
                i2 = p2
                
            while p1 < p2:
                if s[p1] == s[p2]:
                    return len
