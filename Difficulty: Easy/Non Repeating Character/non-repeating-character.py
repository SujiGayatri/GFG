class Solution:
    def nonRepeatingChar(self,s):
        #code here
        freq = [0] * 26
        for i in s:
            freq[ord(i) - ord('a')] += 1
        for ch in s:
            if freq[ord(ch) - ord('a')] == 1:
                return ch
        return '$'