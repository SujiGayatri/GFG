#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        max_val = max(max(a), max(b))
        freq = [0] * (max_val + 1)
        for x in b:
            freq[x] += 1
        for i in range(1, max_val + 1):
            freq[i] += freq[i-1]
        res = []
        for x in query:
            val_in_a = a[x]
            res.append(freq[val_in_a])
        return res