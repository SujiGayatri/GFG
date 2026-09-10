class Solution:
	def findSum(self, n):
		# Code here
        odd_count = (n + 1) // 2
        even_count = n // 2

        odd_sum = odd_count * odd_count
        even_sum = even_count * (even_count + 1)
        return [odd_sum, even_sum]