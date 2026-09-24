class Solution:
    def countArray(self, arr, x):
        # code here
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        result = []
        for num in arr:
            avg = (num + x) // 2
            result.append(freq.get(avg, 0))
        return result