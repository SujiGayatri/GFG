class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        first = float('inf')
        second = float('inf')
        for i in arr:
            if i < first:
                second = first
                first = i
            elif first < i < second:
                second = i
        if second == float('inf'):
            return [-1]
        return [first, second]