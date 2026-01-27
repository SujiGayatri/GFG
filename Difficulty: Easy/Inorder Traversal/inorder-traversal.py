'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self, root):
        # code here
        ans=[]
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            ans.append(node.data)
            dfs(node.right)
        dfs(root)
        return ans
        