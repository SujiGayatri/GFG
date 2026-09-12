class Solution:
    def findEvenOccurrences(self, arr):
        # code here
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        ans = []
        added = set()
        for num in arr:
            if freq[num] % 2 == 0 and num not in added:
                ans.append(num)
                added.add(num)
        return ans if ans else [-1]