# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, biggest):
            if not root:
                return 0
            if root.val >= biggest:
                biggest = root.val
                count = 1
            else:
                count = 0
            count += dfs(root.left, biggest)
            count += dfs(root.right, biggest)
            return count
        return dfs(root, root.val)    

            
