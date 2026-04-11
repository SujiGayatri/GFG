#User function Template for python3

class Solution:
    def secFrequent(self, arr, n):
        # code here
        from collections import Counter
        freq = Counter(arr)
        unique_freqs = list(set(freq.values()))
        if len(unique_freqs) < 2:
            return ""
        unique_freqs.sort(reverse=True)
        second_max = unique_freqs[1]
        for i in freq:
            if freq[i] == second_max:
                return i