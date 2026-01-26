'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def preOrder(self, root):
    # code here
        ans=[]
        def dfs(node):
            if not node:
                return None
            ans.append(node.data)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans