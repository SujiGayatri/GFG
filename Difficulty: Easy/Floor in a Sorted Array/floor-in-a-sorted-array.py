class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        low, high = 0, len(arr) - 1
        floor_index = -1  # Default case if no floor exists
    
        while low <= high:
            mid = (low + high) // 2
        
            if arr[mid] <= x:
                floor_index = mid  
                low = mid + 1  
            else:
                high = mid - 1  
    
        return floor_index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, x)
        print(ans)
        tc -= 1

# } Driver Code Ends