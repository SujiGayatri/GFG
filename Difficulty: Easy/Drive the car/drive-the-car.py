class Solution:
    def required(self, arr, k):
        # code here
        max_track = max(arr)
        if k >= max_track:
            return -1
        return max_track - k