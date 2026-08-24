class Solution:
    def longestConsecutive(self, arr):
        # code here
        if not arr:
            return 0
        nums_set=set(arr)
        ans=0
        for num in nums_set:
            if num-1 not in nums_set:
                current_num=num
                current_sum=1
                while (current_num+1) in nums_set:
                    current_num+=1
                    current_sum+=1
                ans=max(ans,current_sum)
        return ans