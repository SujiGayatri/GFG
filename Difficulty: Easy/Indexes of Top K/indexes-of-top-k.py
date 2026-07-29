class Solution:
    def topKIndices(self, arr, k):
        # code here
        top_marks = set(sorted(set(arr), reverse=True)[:k])
        res = []
        for i, mark in enumerate(arr):
            if mark in top_marks:
                res.append((-mark, i))  
        res.sort()
        return [idx for _, idx in res]