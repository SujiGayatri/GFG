class Solution:
    def minOperation(self, s): 
        #code here
        n = len(s)
        ans = n
        for i in range(1, n // 2 + 1):
            if s[:i] == s[i:2 * i]:
                ans = min(ans, n - i + 1)
        return ans