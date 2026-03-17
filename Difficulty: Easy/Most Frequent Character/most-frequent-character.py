class Solution:
    def getMaxOccurringChar(self, s):
        #code here
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        max_freq = -1
        result = ''
        for ch in sorted(freq.keys()):
            if freq[ch] > max_freq:
                max_freq = freq[ch]
                result = ch
        return result