class Solution:
    def sumOfDigits(self, n):
        # code here
        temp=n
        s=0
        dig=0
        while temp>0:
            dig=temp%10
            s=s+dig
            temp//=10
        return s
