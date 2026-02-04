#User function Template for python3

class Solution:
    def checkYear (self, n):
        # code here
        if(n%100!=0 and n%4==0) or (n%400==0):
            return True
        else:
            return False