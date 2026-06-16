class Solution:
    def maxNumber(self, arr):
        #code here.
        arr.sort(reverse=True)
        return ''.join(map(str, arr))