class Solution:
	def maxRepeating(self,k, arr):
		# code here
		freq = [0] * k
        for num in arr:
            freq[num] += 1
        ans = 0
        max_freq = freq[0]
        for i in range(1, k):
            if freq[i] > max_freq:
                max_freq = freq[i]
                ans = i

        return ans