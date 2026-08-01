class Solution:
    def minSum(self, arr):
        # code here
        if len(arr) <= 1:
            return 0
        heapq.heapify(arr)
        total = 0
        while len(arr) > 1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            curr = first + second
            total += curr
            heapq.heappush(arr, curr)
        return total