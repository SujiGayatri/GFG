#User function Template for python3
class Solution:
    def getMoreAndLess(self, arr, target):
		# code here
		n = len(arr)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        count_le = left  
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid
        count_ge = n - left  
        return count_le, count_ge