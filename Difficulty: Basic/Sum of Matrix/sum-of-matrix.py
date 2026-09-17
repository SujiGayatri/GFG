class Solution:
    def sumOfMatrix(self, mat: list[list[int]]) -> int:
        # code here
        total = 0
        for row in mat:
            for num in row:
                total += num
        return total