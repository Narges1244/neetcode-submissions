# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def find_depth(root):
            if root is None:
                return 0
           
            left_branch = find_depth(root.left)
            if left_branch == -1:
                return -1
         
            right_branch = find_depth(root.right)
            if right_branch == -1:
                return -1

            if abs(left_branch - right_branch)>1:
                return -1
            return 1+ max(left_branch ,right_branch)
        
        return find_depth(root) != -1
        