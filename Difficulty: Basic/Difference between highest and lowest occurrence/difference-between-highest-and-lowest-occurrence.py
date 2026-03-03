#User function Template for python3

class Solution:
    def findDiff(self, arr):
        # code here
        if not arr:
            return 0
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        if len(freq) == 1:
            return 0
        max_freq = max(freq.values())
        min_freq = min(freq.values())
        return max_freq - min_freq