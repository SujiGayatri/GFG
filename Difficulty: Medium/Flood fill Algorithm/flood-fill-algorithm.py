class Solution:
	def floodFill(self, image, sr, sc, newColor):
		# code here
        rows=len(image)
        cols=len(image[0])
        start_c=image[sr][sc]
        if start_c==newColor:
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if image[r][c]!=start_c:
                return
            image[r][c]=newColor
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        dfs(sr,sc)
        return image