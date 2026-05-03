class Solution:
    def find(self, arr, x):
        # code here
        n = len(arr)
        low, high = 0, n - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == x:
                first = mid
                high = mid - 1   
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        low, high = 0, n - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] == x:
                last = mid
                low = mid + 1   
            elif arr[mid] < x:
                low = mid + 1
            else:
                high = mid - 1
        return [first, last]