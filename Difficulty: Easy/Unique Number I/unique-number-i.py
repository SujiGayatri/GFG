class Solution:
    def findUnique(self, arr):
        # code here 
        result = 0
        for num in arr:
            result ^= num
        return result