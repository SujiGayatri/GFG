#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		# code here
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i-1][j]
                if j >= arr[i-1]:
                    dp[i][j] += dp[i-1][j - arr[i-1]]

        return dp[n][target]

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array input
        target = int(input().strip())  # Read the target sum
        ob = Solution()  # Create the Solution object
        print(ob.perfectSum(arr, target))  # Call perfectSum with 2 arguments
        tc -= 1  # Decrease test case count
        print("~")
# } Driver Code Ends