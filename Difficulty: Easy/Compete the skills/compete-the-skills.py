class Solution:
    def scores(self, a, b):
        # code here
        scoreA = 0
        scoreB = 0
        for i in range(3):
            if a[i] > b[i]:
                scoreA += 1
            elif a[i] < b[i]:
                scoreB += 1
        return [scoreA, scoreB]