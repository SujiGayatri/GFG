class Solution:
    def countOccurence(self,arr, k):
        # code here
        n = len(arr)
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        count = 0
        limit = n // k
        for val in freq.values():
            if val > limit:
                count += 1
        return count