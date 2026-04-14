#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        # code here
        frogs.sort()
        visited = [False] * (leaves + 1)
        processed = set()
        for frog_strength in frogs:
            if frog_strength == 1:
                return 0
            is_redundant = False
            for p in processed:
                if frog_strength % p == 0:
                    is_redundant = True
                    break
            if not is_redundant:
                processed.add(frog_strength)
                for i in range(frog_strength, leaves + 1, frog_strength):
                    visited[i] = True
        unvisited_cnt = 0
        for i in range(1, leaves + 1):
            if not visited[i]:
                unvisited_cnt += 1
        return unvisited_cnt