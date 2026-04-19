from typing import List


class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        # code here
        total = sum(A)
        need = (total + N - 1) // N
        ans = float('inf')
        for x in A:
            if x >= need:
                ans = min(ans, x)
        return ans