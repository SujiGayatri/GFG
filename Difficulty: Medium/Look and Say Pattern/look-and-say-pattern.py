class Solution:
    def countAndSay(self, n):
        # code here
        if n==1:
            return "1"
        res="1"
        for _ in range(n-1):
            cur=[]
            i=0
            while i<len(res):
                c=1
                while i+1<len(res) and res[i]==res[i+1]:
                    i+=1
                    c+=1
                cur.append(str(c))
                cur.append(res[i])
                i+=1
            res="".join(cur)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countAndSay(n))

        print("~")
# } Driver Code Ends