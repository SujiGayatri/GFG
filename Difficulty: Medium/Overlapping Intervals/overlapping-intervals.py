class Solution:
	def mergeOverlap(self, arr):
		# Code here
	    if not arr:
	        return []
	    arr.sort(key=lambda x:x[0])
	    merged=[arr[0]]
	    for start,end in arr[1:]:
	        last_end=merged[-1][1]
	        if start<=last_end:
	            merged[-1][1]=max(last_end,end)
	        else:
	            merged.append([start,end])
	    return merged