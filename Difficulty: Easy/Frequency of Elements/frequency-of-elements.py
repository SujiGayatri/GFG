class Solution:
    def countFreq(self, arr):
        #code here
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        ans = []
        for key in sorted(freq):
            ans.append([key, freq[key]])
        return ans