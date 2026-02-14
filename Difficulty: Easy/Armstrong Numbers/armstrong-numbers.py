#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        a = n // 100
        b = (n // 10) % 10
        c = n % 10
        return (a**3 + b**3 + c**3) == n