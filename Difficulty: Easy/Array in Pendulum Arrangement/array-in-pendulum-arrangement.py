class Solution:

	def pendulumArrangement(self, arr):
		# code here
		arr.sort()
        n = len(arr)
        res = [0] * n
        mid = (n - 1) // 2
        res[mid] = arr[0]
        left = mid - 1
        right = mid + 1
        for i in range(1, n):
            if i % 2 == 1:      
                res[right] = arr[i]
                right += 1
            else:              
                res[left] = arr[i]
                left -= 1
        return res