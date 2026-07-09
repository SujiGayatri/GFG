class Solution:
    def findDuplicate(self, arr):
        #code here
        n = len(arr)
        ans = 0
        for num in arr:
            ans ^= num
        for i in range(1, n):
            ans ^= i
        return ans