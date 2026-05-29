class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        total_moves = 0
        for c, p in zip(chairs, passengers):
            total_moves += abs(c - p)
        return total_moves
