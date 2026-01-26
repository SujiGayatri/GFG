'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def postOrder(self, root):
        # code here
        ans=[]
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            dfs(node.right)
            ans.append(node.data)
        dfs(root)
        return ans
        
        