class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        first_occurrence = {}
        max_d = 0

        for i, num in enumerate(arr):
            if num not in first_occurrence:
                first_occurrence[num] = i
            else:
                distance = i - first_occurrence[num]
                max_d = max(max_d, distance)
        return max_d