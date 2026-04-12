#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        result = [s[0]]  
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                result.append(s[i])
        return ''.join(result)