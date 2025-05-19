#User function Template for python3

class Solution:

    def findMinDiff(self, arr,m):

        # code here
        if m == 0 or len(arr) < m:
            return 0  

        arr.sort()
        min_diff = float('inf')

        for i in range(len(arr) - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)

        return min_diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        A = [int(x) for x in input().split()]
        M = int(input())

        solObj = Solution()

        print(solObj.findMinDiff(A, M))
        print("~")

# } Driver Code Ends