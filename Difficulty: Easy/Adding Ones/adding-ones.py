class Solution:
    def update(self, A, n, updates, k):
        # Your code goes here
        for x in updates:
            A[x - 1] += 1
        for i in range(1, n):
            A[i] += A[i - 1]