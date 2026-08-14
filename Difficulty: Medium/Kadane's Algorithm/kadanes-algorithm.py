class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        curr_s=max_s=arr[0]
        for num in arr[1:]:
            curr_s=max(num,curr_s+num)
            max_s=max(max_s,curr_s)
        return max_s