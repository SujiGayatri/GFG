class Solution:
    def findMagicalNumber(self, arr):
        # code here
        n = len(arr)
        left, right = 0, n - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                ans = mid          
                right = mid - 1    
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1
        return ans