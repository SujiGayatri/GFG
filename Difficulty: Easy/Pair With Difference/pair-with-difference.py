
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # code here
        seen = set()
        for num in arr:
            if num - x in seen or num + x in seen:
                return True
            seen.add(num)
        return False
