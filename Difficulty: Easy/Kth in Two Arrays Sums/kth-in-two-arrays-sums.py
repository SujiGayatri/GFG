class Solution:
    def kthItem(self, a, b, k):
        # code here
        sums = set()
        for x in a:
            for y in b:
                sums.add(x + y)
        sums = sorted(sums)
        if k > len(sums):
            return -1
        return sums[k - 1]