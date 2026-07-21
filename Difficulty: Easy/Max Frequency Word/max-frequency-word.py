class Solution:
    def maximumFrequency(self, s):
        # Code here
        words = s.split()
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        max_freq = max(freq.values())
        for word in words:
            if freq[word] == max_freq:
                return f"{word} {max_freq}"