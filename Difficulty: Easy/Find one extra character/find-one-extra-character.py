class Solution: 
    def extraChar(self,s1, s2):
        # code here
        x = 0
        for ch in s1:
            x ^= ord(ch)
        for ch in s2:
            x ^= ord(ch)
        return chr(x)