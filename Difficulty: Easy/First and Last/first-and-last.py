#User function Template for python3
class Solution: 
    def firstAndLast(self, x, arr): 
        # Code here
        def findFirst():
            low, high = 0, len(arr) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                
                if arr[mid] == x:
                    ans = mid
                    high = mid - 1   
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        def findLast():
            low, high = 0, len(arr) - 1
            ans = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    ans = mid
                    low = mid + 1  
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        first = findFirst()
        if first == -1:
            return [-1]
        last = findLast()
        return [first, last]