
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] != arr[right]:
                return False
            left+=1
            right-=1
        return True