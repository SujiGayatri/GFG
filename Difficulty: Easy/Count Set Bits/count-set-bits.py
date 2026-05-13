#User function Template for python3
class Solution:
	def setBits(self, n):
		# code here
		count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count