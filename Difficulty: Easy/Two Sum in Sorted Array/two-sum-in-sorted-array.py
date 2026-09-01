class Solution:
    def twoSum(self, arr, target):
        #code here
        left = 0
        right = len(arr) - 1
        while left < right:
            total = arr[left] + arr[right]
            if total == target:
                return [left + 1, right + 1]  
            elif total < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]