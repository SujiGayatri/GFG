class Solution:

	def nextGreatest(self,arr):
		# code  here
		n = len(arr)
        max_so_far = -1
        for i in range(n - 1, -1, -1):
            temp = arr[i]
            arr[i] = max_so_far
            max_so_far = max(max_so_far, temp)
        return arr