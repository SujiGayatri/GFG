class Solution:
    def cutRod(self, price):
        #code here
        n = len(price)
        dp = [0] * (n + 1)
        for length in range(1, n + 1):
            for cut in range(1, length + 1):
                dp[length] = max(dp[length], price[cut - 1] + dp[length - cut])
        return dp[n]