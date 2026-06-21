class Solution:
    def countSpecials(self, k, arr):
        # code here
        n = len(arr)
        target = n // k
        freq = Counter(arr)
        count = 0
        for f in freq.values():
            if f == target:
                count += 1
        return count