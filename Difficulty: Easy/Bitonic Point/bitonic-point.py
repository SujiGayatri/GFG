#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		low, high = 0, len(arr) - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid
        return arr[low]