class Solution:
    def totalTime(self, arr, penalty):
        # code here
        seen = {arr[0]}   
        total = 0
        for i in range(1, len(arr)):
            if arr[i] in seen:
                total += penalty[arr[i]]
            else:
                total += 1
                seen.add(arr[i])
        return total