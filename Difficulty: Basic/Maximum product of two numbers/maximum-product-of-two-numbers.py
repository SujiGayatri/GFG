#User function Template for python3
class Solution:

	def maxProduct(self,arr):
		# code here
		m1 = 0
        m2 = 0
        for num in arr:
            if num > m1:
                m2 = m1
                m1 = num
            elif num > m2:
                m2 = num
        return m1 * m2