class Solution:
    def fact(self,a):
        if a==1 or a==0:
            return 1
        return a*self.fact(a-1)
    def nCr(self, n, r):
        # code here
        if r>n: 
            return 0
        x=self.fact(n)//(self.fact(n-r)*self.fact(r))
        return x


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = int(input())
        ob = Solution()
        print(ob.nCr(n, r))
        print("~")
# } Driver Code Ends