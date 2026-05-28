class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        arr.sort()
        n = len(arr)
        ans = 0
        i = n - 1
        while i > 0:
            if arr[i] - arr[i - 1] < k:
                ans += arr[i] + arr[i - 1]
                i -= 2   
            else:
                i -= 1
        return ans