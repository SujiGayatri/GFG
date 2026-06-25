class Solution:
    def countOnes(self, arr):
        #code here
        left, right = 0, len(arr) - 1
        ans = len(arr)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == 0:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans