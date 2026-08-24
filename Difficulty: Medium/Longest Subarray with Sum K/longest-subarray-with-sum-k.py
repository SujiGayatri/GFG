class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        firstindex={}
        prefixSum=0
        ans=0
        for i, num in enumerate(arr):
            prefixSum+=num
            if prefixSum==k:
                ans=i+1
            if prefixSum-k in firstindex:
                length=i-firstindex[prefixSum-k]
                ans=max(ans,length)
            if prefixSum not in firstindex:
                firstindex[prefixSum]=i
        return ans