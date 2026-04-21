#User function Template for python3
from collections import Counter
class Solution:
	def countPairs(self, arr, k):
    	# code here
        freq = Counter(arr)
        cnt = 0
        for i in freq:
            if i + k in freq:
                cnt += freq[i] * freq[i + k]
        return cnt
