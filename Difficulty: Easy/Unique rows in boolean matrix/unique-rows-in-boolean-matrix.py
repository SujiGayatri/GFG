class Solution:
  
    def uniqueRow(self, mat):
        # code here
        seen = set()
        ans = []
        for row in mat:
            t = tuple(row) 
            if t not in seen:
                seen.add(t)
                ans.append(row)
        return ans