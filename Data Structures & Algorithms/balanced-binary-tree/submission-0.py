# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        if root is None:
            return True
        ## returns height of root... 
        def dfs(curr):
            if curr is None:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            if left - right > 1 or left - right < -1:
                self.isBalanced = False
            return 1 + max(left, right)
            
        dfs(root)
        return self.isBalanced