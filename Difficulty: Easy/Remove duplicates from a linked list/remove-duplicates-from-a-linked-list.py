'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        seen = set()
        curr = head
        prev = None
        while curr:
            if curr.data in seen:
                prev.next = curr.next
            else:
                seen.add(curr.data)
                prev = curr
            curr = curr.next
        return head