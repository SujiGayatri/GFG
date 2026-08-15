class Solution:
    def countIslands(self, grid):
        # code here
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if grid[r][c]=="W":
                return
            grid[r][c]="W"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c+1)
            dfs(r+1,c-1)
            dfs(r-1,c-1)
            dfs(r-1,c+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="L":
                    islands+=1
                    dfs(r,c)
        return islands