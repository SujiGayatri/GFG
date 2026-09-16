class Solution:
    def kthDigit(self, a, b, k):
        # code here
        num = a ** b
        answer = int(str(num)[-k])
        return answer