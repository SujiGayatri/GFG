from collections import Counter
class Solution:
    def isFrequencyUnique(self, arr):
        # code here
        freq = Counter(arr)
        seen = set()
        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)
        return True