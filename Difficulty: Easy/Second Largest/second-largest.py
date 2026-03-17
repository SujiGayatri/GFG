class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        first = float('-inf')
        second = float('-inf')
        for i in arr:
            if i > first:
                second = first
                first = i
            elif first > i > second:
                second = i
        return second if second != float('-inf') else -1