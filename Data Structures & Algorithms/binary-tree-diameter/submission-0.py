# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDeiameter = 0
        def calculateDepth(root):
            if root is None:
                return 0
            left_subtree = calculateDepth(root.left)
            right_subtree =calculateDepth(root.right)
            self.maxDeiameter = max(self.maxDeiameter,left_subtree + right_subtree)
        

            return 1 + max(left_subtree , right_subtree)
        calculateDepth(root)    

        return self.maxDeiameter
        

        