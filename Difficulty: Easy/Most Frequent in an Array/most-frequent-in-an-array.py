class Solution:
    def mostFreqEle(self, arr):
        # code here
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        max_count = max(freq.values())
        candidates = [num for num, count in freq.items() if count == max_count]
        return max(candidates)