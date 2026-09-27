class Solution:
    def maxCuts(self, n):
        # code here
        return (n * (n + 1)) // 2 + 1