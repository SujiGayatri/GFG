'''
# Node Class:
class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def height(self, root):
        # code here
        if not root:
            return -1   
        left_depth = self.height(root.left)
        right_depth = self.height(root.right)
        return 1 + max(left_depth, right_depth)