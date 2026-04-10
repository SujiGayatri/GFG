from typing import List


class Solution:
    def chocolates(self, n : int, arr : List[int]) -> int:
        # code here
        left, right = 0, n - 1
        while left < right:
            if arr[left] > arr[right]:
                left += 1
            else:
                right -= 1
        return arr[left]