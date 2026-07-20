class Solution:
    def maxSum(self, arr, k):
        # code here
        max_sum = 0
        curr_sum = 0
        for num in arr:
            if num <= k:
                curr_sum += num
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0

        max_sum = max(max_sum, curr_sum)
        return max_sum