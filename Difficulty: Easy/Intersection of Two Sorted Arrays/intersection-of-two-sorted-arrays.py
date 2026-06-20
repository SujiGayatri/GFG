class Solution:
    def intersection(self,a, b):
        # code here
        i, j = 0, 0
        ans = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                if not ans or ans[-1] != a[i]:
                    ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        return ans