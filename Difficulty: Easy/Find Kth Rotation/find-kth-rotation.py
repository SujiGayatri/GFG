#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        # code here
        low = 0
        high = len(arr) - 1

        while low <= high:
        # If the subarray is already sorted
            if arr[low] <= arr[high]:
                return low

            mid = (low + high) // 2
            next_ = (mid + 1) % len(arr)
            prev = (mid - 1 + len(arr)) % len(arr)
            if arr[mid] <= arr[next_] and arr[mid] <= arr[prev]:
                return mid
            if arr[mid] >= arr[low]:
                low = mid + 1  # Left part is sorted, go right
            else:
                high = mid - 1  # Right part is sorted, go left

        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.findKRotation(arr)
        print(res)
        print("~")
# } Driver Code Ends