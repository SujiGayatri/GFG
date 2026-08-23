from collections import Counter
class Solution:
    def firstNonRepeating(self, arr): 
        # code here
        freq=Counter(arr)
        for i in arr:
            if freq[i]==1:
                return i
        return 0