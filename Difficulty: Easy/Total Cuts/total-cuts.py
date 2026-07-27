class Solution:
    def totalCuts(self, a: list[int], k: int) -> int:
        # code here
        n = len(a)
        suffixMin = [0] * n
        suffixMin[-1] = a[-1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(a[i], suffixMin[i + 1])
        count = 0
        prefixMax = a[0]
        for i in range(n - 1):
            prefixMax = max(prefixMax, a[i])
            if prefixMax + suffixMin[i + 1] >= k:
                count += 1
        return count