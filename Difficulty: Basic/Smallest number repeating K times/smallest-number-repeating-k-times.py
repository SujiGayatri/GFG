#User function Template for python3

class Solution:
    def findDuplicate(self, arr, k):
        # code here
        counts = {}
        for i in arr:
            counts[i] = counts.get(i, 0) + 1
    
        candidates = []
        for i, count in counts.items():
            if count == k:
                candidates.append(i)
    
        if not candidates:
            return -1
        else:
            return min(candidates)