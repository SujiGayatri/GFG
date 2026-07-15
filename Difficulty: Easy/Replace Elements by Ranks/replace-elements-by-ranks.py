class Solution:
    def replaceWithRank(self, arr):
        # code here
        n = len(arr)
        temp = [(arr[i], i) for i in range(n)]
        temp.sort(key=lambda x: x[0])
        for rank, (_, idx) in enumerate(temp):
            arr[idx] = rank