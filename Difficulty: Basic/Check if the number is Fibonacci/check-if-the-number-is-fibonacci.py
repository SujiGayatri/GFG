class Solution:
    def isFibonacci(self, n):
        # code here
        a, b = 0, 1

        while a <= n:
            if a == n:
                return True
            a, b = b, a + b
        return False