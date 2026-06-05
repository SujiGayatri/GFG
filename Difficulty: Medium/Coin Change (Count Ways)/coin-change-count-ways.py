class Solution:
    def count(self, coins, sum):
        # code here 
        dp = [0] * (sum + 1)
        dp[0] = 1
        for coin in coins:
            for s in range(coin, sum + 1):
                dp[s] += dp[s - coin]
        return dp[sum]