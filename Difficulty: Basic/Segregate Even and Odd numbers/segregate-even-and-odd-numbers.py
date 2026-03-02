#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr):
		# code here
		evens = [x for x in arr if x % 2 == 0]
        odds = [x for x in arr if x % 2 != 0]
        evens.sort()
        odds.sort()
        arr[:] = evens + odds