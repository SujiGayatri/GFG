class Solution:
	def divisibleBy4 (self, s):
		# code here
		if len(s) == 1:
            return int(s) % 4 == 0

        last_two = int(s[-2:])
        return last_two % 4 == 0