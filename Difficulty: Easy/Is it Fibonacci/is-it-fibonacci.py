class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        if N <= K:
            return GeekNum[N - 1]
        window_sum = sum(GeekNum)
        for i in range(K, N):
            GeekNum.append(window_sum)
            window_sum += GeekNum[i]
            window_sum -= GeekNum[i - K]
        return GeekNum[N - 1]